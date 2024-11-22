from ast_nodes import (
    Programa, NodoImprimir, NodoAsignacion, NodoCondicional, NodoBucle,
    NodoFuncion, NodoLlamadaFuncion, NodoExpresion, NodoIdentificador,
    NodoNumero, NodoCadena, NodoDeclaracion
)
from aprendaParser import aprendaParser
from aprendaVisitor import aprendaVisitor

class ConstruirASTVisitor(aprendaVisitor):
    def visitPrograma(self, ctx: aprendaParser.ProgramaContext):
        print("Visitando Programa")
        instrucciones = [self.visit(instr) for instr in ctx.instruccion()]
        return Programa(instrucciones)

    def visitInstruccion(self, ctx: aprendaParser.InstruccionContext):
        if ctx.declaracion():
            return self.visit(ctx.declaracion())
        elif ctx.imprimir():
            return self.visit(ctx.imprimir())
        elif ctx.asignacion():
            return self.visit(ctx.asignacion())
        elif ctx.condicional():
            return self.visit(ctx.condicional())
        elif ctx.bucle():
            return self.visit(ctx.bucle())
        elif ctx.funcion():
            return self.visit(ctx.funcion())
        elif ctx.llamada_funcion():
            return self.visit(ctx.llamada_funcion())
        else:
            raise Exception("Instrucción no reconocida")

    def visitDeclaracion(self, ctx: aprendaParser.DeclaracionContext):
        tipo = ctx.tipo().getText()
        nombre = ctx.ID().getText()
        print(f"Declarando variable: {tipo} {nombre}")
        return NodoDeclaracion(tipo, nombre)

    def visitImprimir(self, ctx: aprendaParser.ImprimirContext):
        print("Visitando Imprimir")
        mensaje = self.visit(ctx.expr())
        print(f"Mensaje a imprimir: {mensaje}")
        return NodoImprimir(mensaje)

    def visitAsignacion(self, ctx: aprendaParser.AsignacionContext):
        identificador = ctx.ID().getText()
        print(f"Asignando a {identificador}")
        expresion = self.visit(ctx.expr())
        print(f"Valor de la asignación: {expresion}")
        return NodoAsignacion(identificador, expresion)

    def visitCondicional(self, ctx: aprendaParser.CondicionalContext):
        print("Visitando Condicional")
        condicion = self.visit(ctx.expr())
        print(f"Condición: {condicion}")
        bloque_true = self.visit(ctx.bloque())
        print(f"Bloque verdadero: {bloque_true}")
        bloque_false = self.visit(ctx.bloque(1)) if ctx.ELSE() else None
        if bloque_false:
            print(f"Bloque falso: {bloque_false}")
        return NodoCondicional(condicion, bloque_true, bloque_false)

    def visitBucle(self, ctx: aprendaParser.BucleContext):
        print("Visitando Bucle")
        condicion = self.visit(ctx.expr())
        print(f"Condición del bucle: {condicion}")
        bloque = self.visit(ctx.bloque())
        print(f"Bloque del bucle: {bloque}")
        return NodoBucle(condicion, bloque)

    def visitFuncion(self, ctx: aprendaParser.FuncionContext):
        nombre = ctx.ID(0).getText()
        if len(ctx.ID()) > 1:
            parametros = [param.getText() for param in ctx.ID()[1:]]
        else:
            parametros = []

        bloque = self.visit(ctx.bloque())
        print(f"Bloque de la función '{nombre}': {bloque}")
        return NodoFuncion(nombre, parametros, bloque)

    def visitLlamada_funcion(self, ctx: aprendaParser.Llamada_funcionContext):
        nombre = ctx.ID().getText()
        print(f"Llamando a función: {nombre}")
        argumentos = [self.visit(arg) for arg in ctx.expr()]
        print(f"Argumentos: {argumentos}")
        return NodoLlamadaFuncion(nombre, argumentos)

    def visitBloque(self, ctx: aprendaParser.BloqueContext):
        print("Visitando Bloque")
        instrucciones = [self.visit(instr) for instr in ctx.instruccion()]
        print(f"Instrucciones en el bloque: {instrucciones}")
        return instrucciones

    # Métodos para expresiones
    def visitExpresionComparacion(self, ctx: aprendaParser.ExpresionComparacionContext):
        operador = ctx.op.text
        print(f"Visitando ExpresionComparacion: {operador}")
        izquierdo = self.visit(ctx.expr(0))
        derecho = self.visit(ctx.expr(1))
        print(f"Expresión Comparación: {izquierdo} {operador} {derecho}")
        return NodoExpresion(operador, izquierdo, derecho)

    def visitExpresionSumaResta(self, ctx: aprendaParser.ExpresionSumaRestaContext):
        operador = ctx.op.text
        print(f"Visitando ExpresionSumaResta: {operador}")
        izquierdo = self.visit(ctx.expr(0))
        derecho = self.visit(ctx.expr(1))
        print(f"Suma/Resta: {izquierdo} {operador} {derecho}")
        return NodoExpresion(operador, izquierdo, derecho)

    def visitExpresionMultiplicacionDivision(self, ctx: aprendaParser.ExpresionMultiplicacionDivisionContext):
        operador = ctx.op.text
        print(f"Visitando ExpresionMultiplicacionDivision: {operador}")
        izquierdo = self.visit(ctx.expr(0))
        derecho = self.visit(ctx.expr(1))
        print(f"Multiplicación/División: {izquierdo} {operador} {derecho}")
        return NodoExpresion(operador, izquierdo, derecho)

    def visitExpresionUnaria(self, ctx: aprendaParser.ExpresionUnariaContext):
        operador = ctx.MINUS().getText()
        print(f"Visitando ExpresionUnaria: {operador}")
        expr = self.visit(ctx.expr())
        print(f"Expresión Unaria: {operador}{expr}")
        return NodoExpresion(operador, expr)

    def visitExpresionParentesis(self, ctx: aprendaParser.ExpresionParentesisContext):
        print("Visitando ExpresionParentesis")
        expr = self.visit(ctx.expr())
        print(f"Paréntesis: ({expr})")
        return expr

    def visitExpresionLlamadaFuncion(self, ctx: aprendaParser.ExpresionLlamadaFuncionContext):
        print("Visitando ExpresionLlamadaFuncion")
        return self.visit(ctx.llamada_funcion())

    def visitExpresionIdentificador(self, ctx: aprendaParser.ExpresionIdentificadorContext):
        nombre = ctx.ID().getText()
        print(f"Visitando ExpresionIdentificador: {nombre}")
        return NodoIdentificador(nombre)

    def visitExpresionNumero(self, ctx: aprendaParser.ExpresionNumeroContext):
        valor = int(ctx.NUMBER().getText())
        print(f"Visitando ExpresionNumero: {valor}")
        return NodoNumero(valor)

    def visitExpresionCadena(self, ctx: aprendaParser.ExpresionCadenaContext):
        cadena = ctx.STRING_LITERAL().getText()[1:-1]
        print(f"Visitando ExpresionCadena: {cadena}")
        return NodoCadena(cadena)
