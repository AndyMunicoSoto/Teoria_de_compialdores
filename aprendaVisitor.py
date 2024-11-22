# Generated from aprenda.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .aprendaParser import aprendaParser
else:
    from aprendaParser import aprendaParser

# This class defines a complete generic visitor for a parse tree produced by aprendaParser.

class aprendaVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by aprendaParser#programa.
    def visitPrograma(self, ctx:aprendaParser.ProgramaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by aprendaParser#instruccion.
    def visitInstruccion(self, ctx:aprendaParser.InstruccionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by aprendaParser#declaracion.
    def visitDeclaracion(self, ctx:aprendaParser.DeclaracionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by aprendaParser#imprimir.
    def visitImprimir(self, ctx:aprendaParser.ImprimirContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by aprendaParser#asignacion.
    def visitAsignacion(self, ctx:aprendaParser.AsignacionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by aprendaParser#condicional.
    def visitCondicional(self, ctx:aprendaParser.CondicionalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by aprendaParser#bucle.
    def visitBucle(self, ctx:aprendaParser.BucleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by aprendaParser#funcion.
    def visitFuncion(self, ctx:aprendaParser.FuncionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by aprendaParser#llamada_funcion.
    def visitLlamada_funcion(self, ctx:aprendaParser.Llamada_funcionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by aprendaParser#bloque.
    def visitBloque(self, ctx:aprendaParser.BloqueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by aprendaParser#tipo.
    def visitTipo(self, ctx:aprendaParser.TipoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by aprendaParser#ExpresionLlamadaFuncion.
    def visitExpresionLlamadaFuncion(self, ctx:aprendaParser.ExpresionLlamadaFuncionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by aprendaParser#ExpresionNumero.
    def visitExpresionNumero(self, ctx:aprendaParser.ExpresionNumeroContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by aprendaParser#ExpresionSumaResta.
    def visitExpresionSumaResta(self, ctx:aprendaParser.ExpresionSumaRestaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by aprendaParser#ExpresionParentesis.
    def visitExpresionParentesis(self, ctx:aprendaParser.ExpresionParentesisContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by aprendaParser#ExpresionComparacion.
    def visitExpresionComparacion(self, ctx:aprendaParser.ExpresionComparacionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by aprendaParser#ExpresionMultiplicacionDivision.
    def visitExpresionMultiplicacionDivision(self, ctx:aprendaParser.ExpresionMultiplicacionDivisionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by aprendaParser#ExpresionIdentificador.
    def visitExpresionIdentificador(self, ctx:aprendaParser.ExpresionIdentificadorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by aprendaParser#ExpresionCadena.
    def visitExpresionCadena(self, ctx:aprendaParser.ExpresionCadenaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by aprendaParser#ExpresionUnaria.
    def visitExpresionUnaria(self, ctx:aprendaParser.ExpresionUnariaContext):
        return self.visitChildren(ctx)



del aprendaParser