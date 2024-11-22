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


    # Enter a parse tree produced by aprendaParser#declaracion.
    def enterDeclaracion(self, ctx:aprendaParser.DeclaracionContext):
        pass

    # Exit a parse tree produced by aprendaParser#declaracion.
    def exitDeclaracion(self, ctx:aprendaParser.DeclaracionContext):
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


    # Enter a parse tree produced by aprendaParser#tipo.
    def enterTipo(self, ctx:aprendaParser.TipoContext):
        pass

    # Exit a parse tree produced by aprendaParser#tipo.
    def exitTipo(self, ctx:aprendaParser.TipoContext):
        pass


    # Enter a parse tree produced by aprendaParser#ExpresionLlamadaFuncion.
    def enterExpresionLlamadaFuncion(self, ctx:aprendaParser.ExpresionLlamadaFuncionContext):
        pass

    # Exit a parse tree produced by aprendaParser#ExpresionLlamadaFuncion.
    def exitExpresionLlamadaFuncion(self, ctx:aprendaParser.ExpresionLlamadaFuncionContext):
        pass


    # Enter a parse tree produced by aprendaParser#ExpresionNumero.
    def enterExpresionNumero(self, ctx:aprendaParser.ExpresionNumeroContext):
        pass

    # Exit a parse tree produced by aprendaParser#ExpresionNumero.
    def exitExpresionNumero(self, ctx:aprendaParser.ExpresionNumeroContext):
        pass


    # Enter a parse tree produced by aprendaParser#ExpresionSumaResta.
    def enterExpresionSumaResta(self, ctx:aprendaParser.ExpresionSumaRestaContext):
        pass

    # Exit a parse tree produced by aprendaParser#ExpresionSumaResta.
    def exitExpresionSumaResta(self, ctx:aprendaParser.ExpresionSumaRestaContext):
        pass


    # Enter a parse tree produced by aprendaParser#ExpresionParentesis.
    def enterExpresionParentesis(self, ctx:aprendaParser.ExpresionParentesisContext):
        pass

    # Exit a parse tree produced by aprendaParser#ExpresionParentesis.
    def exitExpresionParentesis(self, ctx:aprendaParser.ExpresionParentesisContext):
        pass


    # Enter a parse tree produced by aprendaParser#ExpresionComparacion.
    def enterExpresionComparacion(self, ctx:aprendaParser.ExpresionComparacionContext):
        pass

    # Exit a parse tree produced by aprendaParser#ExpresionComparacion.
    def exitExpresionComparacion(self, ctx:aprendaParser.ExpresionComparacionContext):
        pass


    # Enter a parse tree produced by aprendaParser#ExpresionMultiplicacionDivision.
    def enterExpresionMultiplicacionDivision(self, ctx:aprendaParser.ExpresionMultiplicacionDivisionContext):
        pass

    # Exit a parse tree produced by aprendaParser#ExpresionMultiplicacionDivision.
    def exitExpresionMultiplicacionDivision(self, ctx:aprendaParser.ExpresionMultiplicacionDivisionContext):
        pass


    # Enter a parse tree produced by aprendaParser#ExpresionIdentificador.
    def enterExpresionIdentificador(self, ctx:aprendaParser.ExpresionIdentificadorContext):
        pass

    # Exit a parse tree produced by aprendaParser#ExpresionIdentificador.
    def exitExpresionIdentificador(self, ctx:aprendaParser.ExpresionIdentificadorContext):
        pass


    # Enter a parse tree produced by aprendaParser#ExpresionCadena.
    def enterExpresionCadena(self, ctx:aprendaParser.ExpresionCadenaContext):
        pass

    # Exit a parse tree produced by aprendaParser#ExpresionCadena.
    def exitExpresionCadena(self, ctx:aprendaParser.ExpresionCadenaContext):
        pass


    # Enter a parse tree produced by aprendaParser#ExpresionUnaria.
    def enterExpresionUnaria(self, ctx:aprendaParser.ExpresionUnariaContext):
        pass

    # Exit a parse tree produced by aprendaParser#ExpresionUnaria.
    def exitExpresionUnaria(self, ctx:aprendaParser.ExpresionUnariaContext):
        pass



del aprendaParser