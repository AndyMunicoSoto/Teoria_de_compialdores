from ast_nodes import (
    Programa, NodoImprimir, NodoAsignacion, NodoCondicional, NodoBucle,
    NodoFuncion, NodoLlamadaFuncion, NodoExpresion, NodoIdentificador,
    NodoNumero, NodoCadena, NodoDeclaracion
)
from aprendaParser import aprendaParser
from aprendaVisitor import aprendaVisitor

class ConstruirASTVisitor(aprendaVisitor):
    def visitPrograma(self, ctx: aprendaParser.ProgramaContext):
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
        return NodoDeclaracion(tipo, nombre)

    def visitImprimir(self, ctx: aprendaParser.ImprimirContext):
        mensaje = self.visit(ctx.expr())
        return NodoImprimir(mensaje)

    def visitAsignacion(self, ctx: aprendaParser.AsignacionContext):
        identificador = ctx.ID().getText()
        expresion = self.visit(ctx.expr())
        return NodoAsignacion(identificador, expresion)

    def visitCondicional(self, ctx: aprendaParser.CondicionalContext):
        condicion = self.visit(ctx.expr())
        bloque_true = self.visit(ctx.bloque())
        bloque_false = self.visit(ctx.bloque(1)) if ctx.ELSE() else None
        return NodoCondicional(condicion, bloque_true, bloque_false)

    def visitBucle(self, ctx: aprendaParser.BucleContext):
        condicion = self.visit(ctx.expr())
        bloque = self.visit(ctx.bloque())
        return NodoBucle(condicion, bloque)

    def visitFuncion(self, ctx: aprendaParser.FuncionContext):
        nombre = ctx.ID().getText()
        if ctx.ID().__len__() > 0:
            parametros = [param.getText() for param in ctx.ID()[1:]]
        else:
            parametros = []
        bloque = self.visit(ctx.bloque())
        return NodoFuncion(nombre, parametros, bloque)

    def visitLlamada_funcion(self, ctx: aprendaParser.Llamada_funcionContext):
        nombre = ctx.ID().getText()
        argumentos = [self.visit(arg) for arg in ctx.expr()]
        return NodoLlamadaFuncion(nombre, argumentos)

    def visitBloque(self, ctx: aprendaParser.BloqueContext):
        instrucciones = [self.visit(instr) for instr in ctx.instruccion()]
        return instrucciones

    def visitExpresionComparacion(self, ctx: aprendaParser.ExpresionComparacionContext):
        izquierdo = self.visit(ctx.expr(0))
        derecho = self.visit(ctx.expr(1))
        operador = ctx.op.text
        return NodoExpresion(operador, izquierdo, derecho)

    def visitExpresionSumaResta(self, ctx: aprendaParser.ExpresionSumaRestaContext):
        izquierdo = self.visit(ctx.expr(0))
        derecho = self.visit(ctx.expr(1))
        operador = ctx.op.text
        return NodoExpresion(operador, izquierdo, derecho)

    def visitExpresionMultiplicacionDivision(self, ctx: aprendaParser.ExpresionMultiplicacionDivisionContext):
        izquierdo = self.visit(ctx.expr(0))
        derecho = self.visit(ctx.expr(1))
        operador = ctx.op.text
        return NodoExpresion(operador, izquierdo, derecho)

    def visitExpresionUnaria(self, ctx: aprendaParser.ExpresionUnariaContext):
        operador = ctx.MINUS().getText()
        expr = self.visit(ctx.expr())
        return NodoExpresion(operador, expr)

    def visitExpresionParentesis(self, ctx: aprendaParser.ExpresionParentesisContext):
        return self.visit(ctx.expr())

    def visitExpresionLlamadaFuncion(self, ctx: aprendaParser.ExpresionLlamadaFuncionContext):
        return self.visit(ctx.llamada_funcion())

    def visitExpresionIdentificador(self, ctx: aprendaParser.ExpresionIdentificadorContext):
        nombre = ctx.ID().getText()
        return NodoIdentificador(nombre)

    def visitExpresionNumero(self, ctx: aprendaParser.ExpresionNumeroContext):
        valor = int(ctx.NUMBER().getText())
        return NodoNumero(valor)

    def visitExpresionCadena(self, ctx: aprendaParser.ExpresionCadenaContext):
        cadena = ctx.STRING_LITERAL().getText()[1:-1]
        return NodoCadena(cadena)
