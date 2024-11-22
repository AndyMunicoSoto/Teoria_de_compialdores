import traceback
from llvmlite import ir
from antlr4 import InputStream, CommonTokenStream
from aprendaLexer import aprendaLexer
from aprendaParser import aprendaParser
from construir_ast_visitor import ConstruirASTVisitor
from analisis_semantico_visitor import AnalisisSemanticoVisitor
from ast_nodes import (
    Programa, NodoImprimir, NodoAsignacion, NodoCondicional, NodoBucle,
    NodoFuncion, NodoLlamadaFuncion, NodoExpresion, NodoIdentificador,
    NodoNumero, NodoCadena, NodoDeclaracion
)

class GeneradorLLVM:
    def __init__(self):
        self.modulo = ir.Module(name="aprenda_modulo")
        self.builder = None
        self.funciones = {}
        self.variables = {}
        self.printf = None
        self.strcat = None
        self.strcpy = None
        self.cadena_contador = 0
        self.in_function = False
        self.setup_printf()

    def setup_printf(self):
        voidptr_ty = ir.IntType(8).as_pointer()
        printf_ty = ir.FunctionType(ir.IntType(32), [voidptr_ty], var_arg=True)
        self.printf = ir.Function(self.modulo, printf_ty, name="printf")

        strcat_ty = ir.FunctionType(voidptr_ty, [voidptr_ty, voidptr_ty])
        self.strcat = ir.Function(self.modulo, strcat_ty, name="strcat")

        strcpy_ty = ir.FunctionType(voidptr_ty, [voidptr_ty, voidptr_ty])
        self.strcpy = ir.Function(self.modulo, strcpy_ty, name="strcpy")

    def crear_cadena_global(self, texto, nombre):
        cadena_bytes = bytearray(texto.encode("utf8")) + b'\00'
        cadena_tipo = ir.ArrayType(ir.IntType(8), len(cadena_bytes))
        cadena_const = ir.Constant(cadena_tipo, cadena_bytes)
        cadena_global = ir.GlobalVariable(self.modulo, cadena_tipo, name=nombre)
        cadena_global.global_constant = True
        cadena_global.initializer = cadena_const
        cadena_global.linkage = 'private'
        return cadena_global

    def generar(self, ast):
        print("Generando LLVM IR...")
        for instr in ast.instrucciones:
            if isinstance(instr, NodoDeclaracion) or isinstance(instr, NodoFuncion):
                self.visit(instr)
        funcion_main = ir.Function(self.modulo, ir.FunctionType(ir.VoidType(), []), name="main")
        bloque_entry = funcion_main.append_basic_block(name="entry")
        self.builder = ir.IRBuilder(bloque_entry)

        self.funciones["main"] = funcion_main
        self.in_function = True
        for instr in ast.instrucciones:
            if not isinstance(instr, NodoDeclaracion) and not isinstance(instr, NodoFuncion):
                self.visit(instr)
        self.builder.ret_void()

        # Indicar que hemos salido de 'main'
        self.in_function = False
        print("Función 'main' finalizada")


    def visit(self, nodo):
        metodo = 'visit_' + nodo.__class__.__name__
        visitor = getattr(self, metodo, self.generic_visit)
        return visitor(nodo)

    def generic_visit(self, nodo):
        raise Exception(f"No se ha implementado el método de visita para {nodo.__class__.__name__}")

    def visit_Programa(self, nodo_programa):
        print("Visiting Programa")
        for instruccion in nodo_programa.instrucciones:
            self.visit(instruccion)

    def visit_NodoFuncion(self, nodo_funcion):
        nombre = nodo_funcion.nombre
        print(f"Generando función: {nombre}")
        tipo_funcion = ir.FunctionType(ir.VoidType(), [ir.IntType(8).as_pointer() for _ in nodo_funcion.parametros])
        funcion = ir.Function(self.modulo, tipo_funcion, name=nombre)
        self.funciones[nombre] = funcion

        bloque_entry = funcion.append_basic_block(name="entry")
        builder_func = ir.IRBuilder(bloque_entry)

        variables_previas = self.variables.copy()
        self.variables = {}
        for i, arg in enumerate(funcion.args):
            arg.name = nodo_funcion.parametros[i]
            print(f"Asignando parámetro: {arg.name}")
            ptr = builder_func.alloca(ir.IntType(8).as_pointer(), name=arg.name)
            builder_func.store(arg, ptr)
            self.variables[arg.name] = ptr

        builder_backup = self.builder
        self.builder = builder_func
        self.in_function = True

        for instr in nodo_funcion.bloque:
            self.visit(instr)

        self.builder.ret_void()
        print(f"Finalizada función: {nombre}")

        self.variables = variables_previas
        self.builder = builder_backup
        self.in_function = False


    def visit_NodoDeclaracion(self, nodo_declaracion):
        nombre = nodo_declaracion.nombre
        tipo = nodo_declaracion.tipo
        print(f"Generando declaración de variable: {tipo} {nombre}")

        if tipo == 'int':
            llvm_tipo = ir.IntType(32)
            init_valor = ir.Constant(llvm_tipo, 0)
        elif tipo == 'string':
            llvm_tipo = ir.IntType(8).as_pointer()
            init_valor = ir.Constant(llvm_tipo, None)
        else:
            raise Exception(f"Tipo '{tipo}' no soportado.")

        if self.in_function:
            ptr = self.builder.alloca(llvm_tipo, name=nombre)
            self.variables[nombre] = ptr
            print(f"Variable local '{nombre}' declarada de tipo '{tipo}'")
        else:
            if tipo == 'int':
                var = ir.GlobalVariable(self.modulo, llvm_tipo, name=nombre)
                var.initializer = init_valor
                var.linkage = 'common'
                var.global_constant = False
                print(f"Variable global '{nombre}' declarada de tipo '{tipo}'")
            elif tipo == 'string':
                var = ir.GlobalVariable(self.modulo, llvm_tipo, name=nombre)
                var.initializer = init_valor
                var.linkage = 'common'
                var.global_constant = False
                print(f"Variable global '{nombre}' declarada de tipo '{tipo}'")

    def visit_NodoAsignacion(self, nodo_asignacion):
        nombre = nodo_asignacion.identificador
        print(f"Generando asignación a variable: {nombre}")

        if nombre not in self.variables:
            raise Exception(f"Variable '{nombre}' no está declarada.")

        valor = self.visit(nodo_asignacion.expresion)
        ptr = self.variables[nombre]
        self.builder.store(valor, ptr)
        print(f"Variable '{nombre}' asignada con valor")

    def visit_NodoImprimir(self, nodo_imprimir):
        print("Generando instrucción de impresión")

        fmt = "%s\n"
        nombre_fmt = f"fstr{self.cadena_contador}"
        self.cadena_contador += 1
        c_fmt = self.crear_cadena_global(fmt, nombre_fmt)
        c_fmt_ptr = self.builder.gep(c_fmt, [ir.IntType(32)(0), ir.IntType(32)(0)], inbounds=True)
        print(f"Cadena de formato '{fmt}' creada como '{nombre_fmt}'")

        valor = self.visit(nodo_imprimir.mensaje)
        if isinstance(valor, ir.GlobalVariable):
            valor_ptr = self.builder.gep(valor, [ir.IntType(32)(0), ir.IntType(32)(0)], inbounds=True)
            print(f"Cadena para imprimir '{nodo_imprimir.mensaje}' convertida a i8*")
        else:
            valor_ptr = valor  # Suponemos que ya es i8*
            print(f"Valor para imprimir es i8* directamente")

        self.builder.call(self.printf, [c_fmt_ptr, valor_ptr], name="printf_call")
        print("Llamada a 'printf' generada")

    def visit_NodoLlamadaFuncion(self, nodo_llamada_funcion):
        nombre = nodo_llamada_funcion.nombre
        print(f"Llamando a función: {nombre}")

        if nombre not in self.funciones:
            raise Exception(f"Función '{nombre}' no está definida.")

        funcion = self.funciones[nombre]

        argumentos = []
        for arg in nodo_llamada_funcion.argumentos:
            valor = self.visit(arg)
            if isinstance(valor, ir.GlobalVariable):
                valor_ptr = self.builder.gep(valor, [ir.IntType(32)(0), ir.IntType(32)(0)], inbounds=True)
                print(f"Argumento de cadena '{arg}' convertido a i8*")
            else:
                valor_ptr = valor  # Suponemos que ya es i8*
                print(f"Argumento '{arg}' es i8* directamente")
            argumentos.append(valor_ptr)

        self.builder.call(funcion, argumentos, name=f"call_{nombre}")
        print(f"Llamada a función '{nombre}' generada")

    def visit_NodoCondicional(self, nodo_condicional):
        print("Generando estructura condicional")

        condicion = self.visit(nodo_condicional.condicion)

        cero = ir.Constant(ir.IntType(32), 0)
        cond_true = self.builder.icmp_signed('!=', condicion, cero, name='if_cond')

        bloque_true = self.modulo.append_basic_block(name="if_true")
        bloque_false = self.modulo.append_basic_block(name="if_false")
        bloque_continuacion = self.modulo.append_basic_block(name="if_continuation")

        self.builder.cbranch(cond_true, bloque_true, bloque_false)
        print("Bifurcación condicional creada")

        self.builder.position_at_end(bloque_true)
        for instr in nodo_condicional.bloque_true:
            self.visit(instr)
        self.builder.branch(bloque_continuacion)
        print("Bloque 'if_true' generado")

        self.builder.position_at_end(bloque_false)
        if nodo_condicional.bloque_false:
            for instr in nodo_condicional.bloque_false:
                self.visit(instr)
        self.builder.branch(bloque_continuacion)
        print("Bloque 'if_false' generado")

        self.builder.position_at_end(bloque_continuacion)
        print("Bloque de continuación generado")

    def visit_NodoBucle(self, nodo_bucle):
        print("Generando estructura de bucle")

        bloque_condicion = self.modulo.append_basic_block(name="loop_cond")
        bloque_cuerpo = self.modulo.append_basic_block(name="loop_body")
        bloque_continuacion = self.modulo.append_basic_block(name="loop_continuation")

        self.builder.branch(bloque_condicion)
        print("Saltando al bloque de condición del bucle")

        self.builder.position_at_end(bloque_condicion)
        condicion = self.visit(nodo_bucle.condicion)
        cero = ir.Constant(ir.IntType(32), 0)
        cond_true = self.builder.icmp_signed('!=', condicion, cero, name='loop_cond')
        self.builder.cbranch(cond_true, bloque_cuerpo, bloque_continuacion)
        print("Bifurcación condicional del bucle creada")
        self.builder.position_at_end(bloque_cuerpo)
        for instr in nodo_bucle.bloque:
            self.visit(instr)
        self.builder.branch(bloque_condicion)
        print("Bloque 'loop_body' generado y regresando a condición")
        self.builder.position_at_end(bloque_continuacion)
        print("Bloque de continuación del bucle generado")

    def visit_NodoExpresion(self, nodo_expresion):
        print(f"Generando expresión con operador: {nodo_expresion.operador}")
        izquierdo = self.visit(nodo_expresion.izquierdo)
        if isinstance(izquierdo, ir.GlobalVariable):
            izquierdo = self.builder.gep(izquierdo, [ir.IntType(32)(0), ir.IntType(32)(0)], inbounds=True)
            print("Convertido 'izquierdo' de [N x i8]* a i8* usando GEP")
        elif isinstance(izquierdo, ir.Instruction):
            print("Valor 'izquierdo' ya es i8*")
        else:
            raise Exception("Tipo inesperado para 'izquierdo' en expresión.")

        if nodo_expresion.derecho:
            derecho = self.visit(nodo_expresion.derecho)
            if isinstance(derecho, ir.GlobalVariable):
                derecho = self.builder.gep(derecho, [ir.IntType(32)(0), ir.IntType(32)(0)], inbounds=True)
                print("Convertido 'derecho' de [N x i8]* a i8* usando GEP")
            elif isinstance(derecho, ir.Instruction):
                print("Valor 'derecho' ya es i8*")
            else:
                raise Exception("Tipo inesperado para 'derecho' en expresión.")

            operador = nodo_expresion.operador
            if operador == '+':
                print("Generando concatenación de cadenas")
                buffer = self.builder.alloca(ir.ArrayType(ir.IntType(8), 256), name="buffer")  # Buffer de 256 bytes
                buffer_ptr = self.builder.bitcast(buffer, ir.IntType(8).as_pointer(), name="buffer_ptr")
                print("Buffer de concatenación asignado y convertido a i8*")
                self.builder.call(self.strcpy, [buffer_ptr, izquierdo], name="strcpy_call")
                print("Llamada a 'strcpy' generada")
                self.builder.call(self.strcat, [buffer_ptr, derecho], name="strcat_call")
                print("Llamada a 'strcat' generada")
                return buffer_ptr
            elif operador == '-':
                print("Generando operación de resta")
                return self.builder.sub(izquierdo, derecho, name="subtmp")
            elif operador == '*':
                print("Generando operación de multiplicación")
                return self.builder.mul(izquierdo, derecho, name="multmp")
            elif operador == '/':
                print("Generando operación de división")
                return self.builder.sdiv(izquierdo, derecho, name="divtmp")
            elif operador in ('==', '!=', '<', '>'):
                print(f"Generando comparación: {operador}")
                if operador == '==':
                    return self.builder.icmp_signed('==', izquierdo, derecho, name="cmptmp")
                elif operador == '!=':
                    return self.builder.icmp_signed('!=', izquierdo, derecho, name="cmptmp")
                elif operador == '<':
                    return self.builder.icmp_signed('<', izquierdo, derecho, name="cmptmp")
                elif operador == '>':
                    return self.builder.icmp_signed('>', izquierdo, derecho, name="cmptmp")
            else:
                raise Exception(f"Operador '{operador}' no soportado.")
        else:
            # Operador unario, por ejemplo, negativo
            operador = nodo_expresion.operador
            if operador == '-':
                print("Generando operación unaria de negación")
                return self.builder.neg(izquierdo, name="negtmp")
            else:
                raise Exception(f"Operador unario '{operador}' no soportado.")

    def visit_NodoIdentificador(self, nodo_identificador):
        nombre = nodo_identificador.nombre
        print(f"Generando acceso a variable: {nombre}")

        if nombre not in self.variables:
            raise Exception(f"Variable '{nombre}' no está declarada.")

        ptr = self.variables[nombre]
        loaded = self.builder.load(ptr, name=nombre)
        print(f"Variable '{nombre}' cargada")
        return loaded

    def visit_NodoNumero(self, nodo_numero):
        valor = nodo_numero.valor
        print(f"Generando constante numérica: {valor}")
        return ir.Constant(ir.IntType(32), valor)

    def visit_NodoCadena(self, nodo_cadena):
        cadena = nodo_cadena.valor
        nombre_cadena = f"str_{self.cadena_contador}"
        self.cadena_contador += 1
        cadena_global = self.crear_cadena_global(cadena, nombre_cadena)
        print(f"Cadena global '{cadena}' creada como '{nombre_cadena}'")
        return cadena_global


def imprimir_ast(nodo, indent=0):
    prefix = '  ' * indent
    if isinstance(nodo, list):
        for elem in nodo:
            imprimir_ast(elem, indent)
    elif hasattr(nodo, '__str__'):
        print(f"{prefix}{str(nodo)}")
    else:
        print(f"{prefix}{nodo}")

def construir_ast_custom(codigo_fuente):

    entrada = InputStream(codigo_fuente)
    lexer = aprendaLexer(entrada)
    stream = CommonTokenStream(lexer)
    parser = aprendaParser(stream)
    arbol = parser.programa()
    visitor = ConstruirASTVisitor()
    ast = visitor.visit(arbol)

    return ast

def analizar_semanticamente_custom(ast):
    analizador = AnalisisSemanticoVisitor()
    analizador.visit(ast)

if __name__ == "__main__":
    codigo = '''
    int contador;
    funcion saludar(nombre) {
        imprimir("Hola, " + nombre);
    }

    saludar("Mundo");
    '''

    try:
        ast = construir_ast_custom(codigo)
        print("\nAST Construido:")
        imprimir_ast(ast)

        analizar_semanticamente_custom(ast)
        print("\nAnálisis semántico completado con éxito.")

        generador = GeneradorLLVM()
        generador.generar(ast)
        llvm_ir = str(generador.modulo)
        print("\nLLVM IR Generado:\n")
        print(llvm_ir)

        with open("output.ll", "w") as f:
            f.write(llvm_ir)
        print("\nLLVM IR guardado en 'output.ll'.")

    except Exception as e:
        print(f"\nError durante el análisis: {e}")
        traceback.print_exc()
