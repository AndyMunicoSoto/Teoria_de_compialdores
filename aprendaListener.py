# Generated from aprenda.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .aprendaParser import aprendaParser
else:
    from aprendaParser import aprendaParser

# This class defines a complete listener for a parse tree produced by aprendaParser.
class aprendaListener(ParseTreeListener):

    # Enter a parse tree produced by aprendaParser#programa.
    def enterPrograma(self, ctx:aprendaParser.ProgramaContext):
        pass

    # Exit a parse tree produced by aprendaParser#programa.
    def exitPrograma(self, ctx:aprendaParser.ProgramaContext):
        pass


    # Enter a parse tree produced by aprendaParser#instruccion.
    def enterInstruccion(self, ctx:aprendaParser.InstruccionContext):
        pass

    # Exit a parse tree produced by aprendaParser#instruccion.
    def exitInstruccion(self, ctx:aprendaParser.InstruccionContext):
        pass


    # Enter a parse tree produced by aprendaParser#imprimir.
    def enterImprimir(self, ctx:aprendaParser.ImprimirContext):
        pass

    # Exit a parse tree produced by aprendaParser#imprimir.
    def exitImprimir(self, ctx:aprendaParser.ImprimirContext):
        pass


    # Enter a parse tree produced by aprendaParser#asignacion.
    def enterAsignacion(self, ctx:aprendaParser.AsignacionContext):
        pass

    # Exit a parse tree produced by aprendaParser#asignacion.
    def exitAsignacion(self, ctx:aprendaParser.AsignacionContext):
        pass


    # Enter a parse tree produced by aprendaParser#condicional.
    def enterCondicional(self, ctx:aprendaParser.CondicionalContext):
        pass

    # Exit a parse tree produced by aprendaParser#condicional.
    def exitCondicional(self, ctx:aprendaParser.CondicionalContext):
        pass


    # Enter a parse tree produced by aprendaParser#bucle.
    def enterBucle(self, ctx:aprendaParser.BucleContext):
        pass

    # Exit a parse tree produced by aprendaParser#bucle.
    def exitBucle(self, ctx:aprendaParser.BucleContext):
        pass


    # Enter a parse tree produced by aprendaParser#funcion.
    def enterFuncion(self, ctx:aprendaParser.FuncionContext):
        pass

    # Exit a parse tree produced by aprendaParser#funcion.
    def exitFuncion(self, ctx:aprendaParser.FuncionContext):
        pass


    # Enter a parse tree produced by aprendaParser#llamada_funcion.
    def enterLlamada_funcion(self, ctx:aprendaParser.Llamada_funcionContext):
        pass

    # Exit a parse tree produced by aprendaParser#llamada_funcion.
    def exitLlamada_funcion(self, ctx:aprendaParser.Llamada_funcionContext):
        pass


    # Enter a parse tree produced by aprendaParser#bloque.
    def enterBloque(self, ctx:aprendaParser.BloqueContext):
        pass

    # Exit a parse tree produced by aprendaParser#bloque.
    def exitBloque(self, ctx:aprendaParser.BloqueContext):
        pass


    # Enter a parse tree produced by aprendaParser#expr.
    def enterExpr(self, ctx:aprendaParser.ExprContext):
        pass

    # Exit a parse tree produced by aprendaParser#expr.
    def exitExpr(self, ctx:aprendaParser.ExprContext):
        pass



del aprendaParser