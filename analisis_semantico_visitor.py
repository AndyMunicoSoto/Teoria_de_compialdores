from tabla_simbolos import TablaSimbolos, Simbolo
from ast_nodes import (
    Programa, NodoImprimir, NodoAsignacion, NodoCondicional, NodoBucle,
    NodoFuncion, NodoLlamadaFuncion, NodoExpresion, NodoIdentificador,
    NodoNumero, NodoCadena, NodoDeclaracion
)

class AnalisisSemanticoVisitor:
    def __init__(self):
        self.tabla_simbolos = TablaSimbolos()

    def visit(self, nodo):
        if nodo is None:
            raise Exception("Intento de visitar un nodo None")
        metodo = 'visit_' + nodo.__class__.__name__
        visitor = getattr(self, metodo, self.generic_visit)
        return visitor(nodo)

    def generic_visit(self, nodo):
        raise Exception(f"No se ha implementado el método de visita para {nodo.__class__.__name__}")

    def visit_Programa(self, nodo_programa):
        for instruccion in nodo_programa.instrucciones:
            self.visit(instruccion)

    def visit_NodoFuncion(self, nodo_funcion):
        nombre = nodo_funcion.nombre

        if self.tabla_simbolos.obtener(nombre):
            raise Exception(f"Función '{nombre}' ya está definida.")

        simbolo_funcion = Simbolo(nombre, 'void', nodo_funcion.parametros)
        self.tabla_simbolos.definir(simbolo_funcion)

        tabla_local = TablaSimbolos(padre=self.tabla_simbolos)
        self.tabla_simbolos = tabla_local

        for param in nodo_funcion.parametros:
            simbolo_param = Simbolo(param, 'string')
            self.tabla_simbolos.definir(simbolo_param)

        for instr in nodo_funcion.bloque:
            self.visit(instr)

        self.tabla_simbolos = tabla_local.padre

    def visit_NodoDeclaracion(self, nodo_declaracion):
        nombre = nodo_declaracion.nombre
        tipo = nodo_declaracion.tipo

        if self.tabla_simbolos.existe_en_ambito_actual(nombre):
            raise Exception(f"Variable '{nombre}' ya está declarada en este ámbito.")

        simbolo_variable = Simbolo(nombre, tipo)
        self.tabla_simbolos.definir(simbolo_variable)

    def visit_NodoAsignacion(self, nodo_asignacion):
        nombre = nodo_asignacion.identificador
        simbolo = self.tabla_simbolos.obtener(nombre)

        if not simbolo:
            raise Exception(f"Variable '{nombre}' no está declarada.")

        self.visit(nodo_asignacion.expresion)

    def visit_NodoImprimir(self, nodo_imprimir):
        self.visit(nodo_imprimir.mensaje)

    def visit_NodoLlamadaFuncion(self, nodo_llamada_funcion):
        nombre = nodo_llamada_funcion.nombre
        simbolo_funcion = self.tabla_simbolos.obtener(nombre)

        if not simbolo_funcion:
            raise Exception(f"Función '{nombre}' no está definida.")

        if len(nodo_llamada_funcion.argumentos) != len(simbolo_funcion.params):
            raise Exception(f"La función '{nombre}' espera {len(simbolo_funcion.params)} argumentos, pero se le pasaron {len(nodo_llamada_funcion.argumentos)}.")

        for arg in nodo_llamada_funcion.argumentos:
            self.visit(arg)

    def visit_NodoCondicional(self, nodo_condicional):
        self.visit(nodo_condicional.condicion)

        tabla_true = TablaSimbolos(padre=self.tabla_simbolos)
        self.tabla_simbolos = tabla_true

        for instr in nodo_condicional.bloque_true:
            if instr is not None:
                self.visit(instr)
            else:
                raise Exception("Instrucción en bloque verdadero es None")

        self.tabla_simbolos = tabla_true.padre

        if nodo_condicional.bloque_false:
            tabla_false = TablaSimbolos(padre=self.tabla_simbolos)
            self.tabla_simbolos = tabla_false

            for instr in nodo_condicional.bloque_false:
                if instr is not None:
                    self.visit(instr)
                else:
                    raise Exception("Instrucción en bloque falso es None")

            self.tabla_simbolos = tabla_false.padre

    def visit_NodoBucle(self, nodo_bucle):
        self.visit(nodo_bucle.condicion)

        tabla_bucle = TablaSimbolos(padre=self.tabla_simbolos)
        self.tabla_simbolos = tabla_bucle

        for instr in nodo_bucle.bloque:
            if instr is not None:
                self.visit(instr)
            else:
                raise Exception("Instrucción en bloque de bucle es None")

        self.tabla_simbolos = tabla_bucle.padre

    def visit_NodoExpresion(self, nodo_expresion):
        self.visit(nodo_expresion.izquierdo)
        if nodo_expresion.derecho:
            self.visit(nodo_expresion.derecho)

    def visit_NodoIdentificador(self, nodo_identificador):
        simbolo = self.tabla_simbolos.obtener(nodo_identificador.nombre)
        if not simbolo:
            raise Exception(f"Variable '{nodo_identificador.nombre}' no está declarada.")

    def visit_NodoNumero(self, nodo_numero):
        pass

    def visit_NodoCadena(self, nodo_cadena):
        pass
