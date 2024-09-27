# Generated from aprenda.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,26,123,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,1,0,4,0,22,8,0,11,0,12,0,23,1,1,1,1,1,
        1,1,1,1,1,1,1,3,1,32,8,1,1,2,1,2,1,2,1,2,1,2,1,2,1,3,1,3,1,3,1,3,
        1,3,1,4,1,4,1,4,1,4,1,4,1,4,1,4,3,4,52,8,4,1,5,1,5,1,5,1,5,1,5,1,
        5,1,6,1,6,1,6,1,6,1,6,1,6,5,6,66,8,6,10,6,12,6,69,9,6,3,6,71,8,6,
        1,6,1,6,1,6,1,7,1,7,1,7,1,7,1,7,5,7,81,8,7,10,7,12,7,84,9,7,3,7,
        86,8,7,1,7,1,7,1,7,1,8,1,8,5,8,93,8,8,10,8,12,8,96,9,8,1,8,1,8,1,
        9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,3,9,110,8,9,1,9,1,9,1,9,1,
        9,1,9,1,9,5,9,118,8,9,10,9,12,9,121,9,9,1,9,0,1,18,10,0,2,4,6,8,
        10,12,14,16,18,0,2,1,0,5,8,1,0,9,12,130,0,21,1,0,0,0,2,31,1,0,0,
        0,4,33,1,0,0,0,6,39,1,0,0,0,8,44,1,0,0,0,10,53,1,0,0,0,12,59,1,0,
        0,0,14,75,1,0,0,0,16,90,1,0,0,0,18,109,1,0,0,0,20,22,3,2,1,0,21,
        20,1,0,0,0,22,23,1,0,0,0,23,21,1,0,0,0,23,24,1,0,0,0,24,1,1,0,0,
        0,25,32,3,4,2,0,26,32,3,6,3,0,27,32,3,8,4,0,28,32,3,10,5,0,29,32,
        3,12,6,0,30,32,3,14,7,0,31,25,1,0,0,0,31,26,1,0,0,0,31,27,1,0,0,
        0,31,28,1,0,0,0,31,29,1,0,0,0,31,30,1,0,0,0,32,3,1,0,0,0,33,34,5,
        19,0,0,34,35,5,1,0,0,35,36,5,23,0,0,36,37,5,2,0,0,37,38,5,3,0,0,
        38,5,1,0,0,0,39,40,5,21,0,0,40,41,5,4,0,0,41,42,3,18,9,0,42,43,5,
        3,0,0,43,7,1,0,0,0,44,45,5,16,0,0,45,46,5,1,0,0,46,47,3,18,9,0,47,
        48,5,2,0,0,48,51,3,16,8,0,49,50,5,17,0,0,50,52,3,16,8,0,51,49,1,
        0,0,0,51,52,1,0,0,0,52,9,1,0,0,0,53,54,5,18,0,0,54,55,5,1,0,0,55,
        56,3,18,9,0,56,57,5,2,0,0,57,58,3,16,8,0,58,11,1,0,0,0,59,60,5,20,
        0,0,60,61,5,21,0,0,61,70,5,1,0,0,62,67,5,21,0,0,63,64,5,15,0,0,64,
        66,5,21,0,0,65,63,1,0,0,0,66,69,1,0,0,0,67,65,1,0,0,0,67,68,1,0,
        0,0,68,71,1,0,0,0,69,67,1,0,0,0,70,62,1,0,0,0,70,71,1,0,0,0,71,72,
        1,0,0,0,72,73,5,2,0,0,73,74,3,16,8,0,74,13,1,0,0,0,75,76,5,21,0,
        0,76,85,5,1,0,0,77,82,3,18,9,0,78,79,5,15,0,0,79,81,3,18,9,0,80,
        78,1,0,0,0,81,84,1,0,0,0,82,80,1,0,0,0,82,83,1,0,0,0,83,86,1,0,0,
        0,84,82,1,0,0,0,85,77,1,0,0,0,85,86,1,0,0,0,86,87,1,0,0,0,87,88,
        5,2,0,0,88,89,5,3,0,0,89,15,1,0,0,0,90,94,5,13,0,0,91,93,3,2,1,0,
        92,91,1,0,0,0,93,96,1,0,0,0,94,92,1,0,0,0,94,95,1,0,0,0,95,97,1,
        0,0,0,96,94,1,0,0,0,97,98,5,14,0,0,98,17,1,0,0,0,99,100,6,9,-1,0,
        100,101,5,1,0,0,101,102,3,18,9,0,102,103,5,2,0,0,103,110,1,0,0,0,
        104,105,5,6,0,0,105,110,3,18,9,4,106,110,5,21,0,0,107,110,5,22,0,
        0,108,110,3,14,7,0,109,99,1,0,0,0,109,104,1,0,0,0,109,106,1,0,0,
        0,109,107,1,0,0,0,109,108,1,0,0,0,110,119,1,0,0,0,111,112,10,7,0,
        0,112,113,7,0,0,0,113,118,3,18,9,8,114,115,10,6,0,0,115,116,7,1,
        0,0,116,118,3,18,9,7,117,111,1,0,0,0,117,114,1,0,0,0,118,121,1,0,
        0,0,119,117,1,0,0,0,119,120,1,0,0,0,120,19,1,0,0,0,121,119,1,0,0,
        0,11,23,31,51,67,70,82,85,94,109,117,119
    ]

class aprendaParser ( Parser ):

    grammarFileName = "aprenda.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "')'", "';'", "'='", "'+'", "'-'", 
                     "'*'", "'/'", "'=='", "'!='", "'<'", "'>'", "'{'", 
                     "'}'", "','", "'si'", "'sino'", "'mientras'", "'imprimir'", 
                     "'funcion'" ]

    symbolicNames = [ "<INVALID>", "LPAREN", "RPAREN", "SEMICOLON", "EQUAL", 
                      "PLUS", "MINUS", "MUL", "DIV", "EQ", "NEQ", "LT", 
                      "GT", "LBRACE", "RBRACE", "COMMA", "IF", "ELSE", "WHILE", 
                      "PRINT", "FUNCION", "ID", "NUMBER", "STRING", "WS", 
                      "COMMENT", "LINE_COMMENT" ]

    RULE_programa = 0
    RULE_instruccion = 1
    RULE_imprimir = 2
    RULE_asignacion = 3
    RULE_condicional = 4
    RULE_bucle = 5
    RULE_funcion = 6
    RULE_llamada_funcion = 7
    RULE_bloque = 8
    RULE_expr = 9

    ruleNames =  [ "programa", "instruccion", "imprimir", "asignacion", 
                   "condicional", "bucle", "funcion", "llamada_funcion", 
                   "bloque", "expr" ]

    EOF = Token.EOF
    LPAREN=1
    RPAREN=2
    SEMICOLON=3
    EQUAL=4
    PLUS=5
    MINUS=6
    MUL=7
    DIV=8
    EQ=9
    NEQ=10
    LT=11
    GT=12
    LBRACE=13
    RBRACE=14
    COMMA=15
    IF=16
    ELSE=17
    WHILE=18
    PRINT=19
    FUNCION=20
    ID=21
    NUMBER=22
    STRING=23
    WS=24
    COMMENT=25
    LINE_COMMENT=26

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def instruccion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(aprendaParser.InstruccionContext)
            else:
                return self.getTypedRuleContext(aprendaParser.InstruccionContext,i)


        def getRuleIndex(self):
            return aprendaParser.RULE_programa

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrograma" ):
                listener.enterPrograma(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrograma" ):
                listener.exitPrograma(self)




    def programa(self):

        localctx = aprendaParser.ProgramaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_programa)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 21 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 20
                self.instruccion()
                self.state = 23 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 3997696) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InstruccionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def imprimir(self):
            return self.getTypedRuleContext(aprendaParser.ImprimirContext,0)


        def asignacion(self):
            return self.getTypedRuleContext(aprendaParser.AsignacionContext,0)


        def condicional(self):
            return self.getTypedRuleContext(aprendaParser.CondicionalContext,0)


        def bucle(self):
            return self.getTypedRuleContext(aprendaParser.BucleContext,0)


        def funcion(self):
            return self.getTypedRuleContext(aprendaParser.FuncionContext,0)


        def llamada_funcion(self):
            return self.getTypedRuleContext(aprendaParser.Llamada_funcionContext,0)


        def getRuleIndex(self):
            return aprendaParser.RULE_instruccion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInstruccion" ):
                listener.enterInstruccion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInstruccion" ):
                listener.exitInstruccion(self)




    def instruccion(self):

        localctx = aprendaParser.InstruccionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_instruccion)
        try:
            self.state = 31
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 25
                self.imprimir()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 26
                self.asignacion()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 27
                self.condicional()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 28
                self.bucle()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 29
                self.funcion()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 30
                self.llamada_funcion()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ImprimirContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PRINT(self):
            return self.getToken(aprendaParser.PRINT, 0)

        def LPAREN(self):
            return self.getToken(aprendaParser.LPAREN, 0)

        def STRING(self):
            return self.getToken(aprendaParser.STRING, 0)

        def RPAREN(self):
            return self.getToken(aprendaParser.RPAREN, 0)

        def SEMICOLON(self):
            return self.getToken(aprendaParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return aprendaParser.RULE_imprimir

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterImprimir" ):
                listener.enterImprimir(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitImprimir" ):
                listener.exitImprimir(self)




    def imprimir(self):

        localctx = aprendaParser.ImprimirContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_imprimir)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 33
            self.match(aprendaParser.PRINT)
            self.state = 34
            self.match(aprendaParser.LPAREN)
            self.state = 35
            self.match(aprendaParser.STRING)
            self.state = 36
            self.match(aprendaParser.RPAREN)
            self.state = 37
            self.match(aprendaParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AsignacionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(aprendaParser.ID, 0)

        def EQUAL(self):
            return self.getToken(aprendaParser.EQUAL, 0)

        def expr(self):
            return self.getTypedRuleContext(aprendaParser.ExprContext,0)


        def SEMICOLON(self):
            return self.getToken(aprendaParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return aprendaParser.RULE_asignacion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAsignacion" ):
                listener.enterAsignacion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAsignacion" ):
                listener.exitAsignacion(self)




    def asignacion(self):

        localctx = aprendaParser.AsignacionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_asignacion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 39
            self.match(aprendaParser.ID)
            self.state = 40
            self.match(aprendaParser.EQUAL)
            self.state = 41
            self.expr(0)
            self.state = 42
            self.match(aprendaParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CondicionalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(aprendaParser.IF, 0)

        def LPAREN(self):
            return self.getToken(aprendaParser.LPAREN, 0)

        def expr(self):
            return self.getTypedRuleContext(aprendaParser.ExprContext,0)


        def RPAREN(self):
            return self.getToken(aprendaParser.RPAREN, 0)

        def bloque(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(aprendaParser.BloqueContext)
            else:
                return self.getTypedRuleContext(aprendaParser.BloqueContext,i)


        def ELSE(self):
            return self.getToken(aprendaParser.ELSE, 0)

        def getRuleIndex(self):
            return aprendaParser.RULE_condicional

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCondicional" ):
                listener.enterCondicional(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCondicional" ):
                listener.exitCondicional(self)




    def condicional(self):

        localctx = aprendaParser.CondicionalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_condicional)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 44
            self.match(aprendaParser.IF)
            self.state = 45
            self.match(aprendaParser.LPAREN)
            self.state = 46
            self.expr(0)
            self.state = 47
            self.match(aprendaParser.RPAREN)
            self.state = 48
            self.bloque()
            self.state = 51
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==17:
                self.state = 49
                self.match(aprendaParser.ELSE)
                self.state = 50
                self.bloque()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BucleContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHILE(self):
            return self.getToken(aprendaParser.WHILE, 0)

        def LPAREN(self):
            return self.getToken(aprendaParser.LPAREN, 0)

        def expr(self):
            return self.getTypedRuleContext(aprendaParser.ExprContext,0)


        def RPAREN(self):
            return self.getToken(aprendaParser.RPAREN, 0)

        def bloque(self):
            return self.getTypedRuleContext(aprendaParser.BloqueContext,0)


        def getRuleIndex(self):
            return aprendaParser.RULE_bucle

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBucle" ):
                listener.enterBucle(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBucle" ):
                listener.exitBucle(self)




    def bucle(self):

        localctx = aprendaParser.BucleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_bucle)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 53
            self.match(aprendaParser.WHILE)
            self.state = 54
            self.match(aprendaParser.LPAREN)
            self.state = 55
            self.expr(0)
            self.state = 56
            self.match(aprendaParser.RPAREN)
            self.state = 57
            self.bloque()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNCION(self):
            return self.getToken(aprendaParser.FUNCION, 0)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(aprendaParser.ID)
            else:
                return self.getToken(aprendaParser.ID, i)

        def LPAREN(self):
            return self.getToken(aprendaParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(aprendaParser.RPAREN, 0)

        def bloque(self):
            return self.getTypedRuleContext(aprendaParser.BloqueContext,0)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(aprendaParser.COMMA)
            else:
                return self.getToken(aprendaParser.COMMA, i)

        def getRuleIndex(self):
            return aprendaParser.RULE_funcion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFuncion" ):
                listener.enterFuncion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFuncion" ):
                listener.exitFuncion(self)




    def funcion(self):

        localctx = aprendaParser.FuncionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_funcion)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 59
            self.match(aprendaParser.FUNCION)
            self.state = 60
            self.match(aprendaParser.ID)
            self.state = 61
            self.match(aprendaParser.LPAREN)
            self.state = 70
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==21:
                self.state = 62
                self.match(aprendaParser.ID)
                self.state = 67
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==15:
                    self.state = 63
                    self.match(aprendaParser.COMMA)
                    self.state = 64
                    self.match(aprendaParser.ID)
                    self.state = 69
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 72
            self.match(aprendaParser.RPAREN)
            self.state = 73
            self.bloque()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Llamada_funcionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(aprendaParser.ID, 0)

        def LPAREN(self):
            return self.getToken(aprendaParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(aprendaParser.RPAREN, 0)

        def SEMICOLON(self):
            return self.getToken(aprendaParser.SEMICOLON, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(aprendaParser.ExprContext)
            else:
                return self.getTypedRuleContext(aprendaParser.ExprContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(aprendaParser.COMMA)
            else:
                return self.getToken(aprendaParser.COMMA, i)

        def getRuleIndex(self):
            return aprendaParser.RULE_llamada_funcion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLlamada_funcion" ):
                listener.enterLlamada_funcion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLlamada_funcion" ):
                listener.exitLlamada_funcion(self)




    def llamada_funcion(self):

        localctx = aprendaParser.Llamada_funcionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_llamada_funcion)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 75
            self.match(aprendaParser.ID)
            self.state = 76
            self.match(aprendaParser.LPAREN)
            self.state = 85
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 6291522) != 0):
                self.state = 77
                self.expr(0)
                self.state = 82
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==15:
                    self.state = 78
                    self.match(aprendaParser.COMMA)
                    self.state = 79
                    self.expr(0)
                    self.state = 84
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 87
            self.match(aprendaParser.RPAREN)
            self.state = 88
            self.match(aprendaParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BloqueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACE(self):
            return self.getToken(aprendaParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(aprendaParser.RBRACE, 0)

        def instruccion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(aprendaParser.InstruccionContext)
            else:
                return self.getTypedRuleContext(aprendaParser.InstruccionContext,i)


        def getRuleIndex(self):
            return aprendaParser.RULE_bloque

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBloque" ):
                listener.enterBloque(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBloque" ):
                listener.exitBloque(self)




    def bloque(self):

        localctx = aprendaParser.BloqueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_bloque)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 90
            self.match(aprendaParser.LBRACE)
            self.state = 94
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 3997696) != 0):
                self.state = 91
                self.instruccion()
                self.state = 96
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 97
            self.match(aprendaParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LPAREN(self):
            return self.getToken(aprendaParser.LPAREN, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(aprendaParser.ExprContext)
            else:
                return self.getTypedRuleContext(aprendaParser.ExprContext,i)


        def RPAREN(self):
            return self.getToken(aprendaParser.RPAREN, 0)

        def MINUS(self):
            return self.getToken(aprendaParser.MINUS, 0)

        def ID(self):
            return self.getToken(aprendaParser.ID, 0)

        def NUMBER(self):
            return self.getToken(aprendaParser.NUMBER, 0)

        def llamada_funcion(self):
            return self.getTypedRuleContext(aprendaParser.Llamada_funcionContext,0)


        def PLUS(self):
            return self.getToken(aprendaParser.PLUS, 0)

        def MUL(self):
            return self.getToken(aprendaParser.MUL, 0)

        def DIV(self):
            return self.getToken(aprendaParser.DIV, 0)

        def EQ(self):
            return self.getToken(aprendaParser.EQ, 0)

        def NEQ(self):
            return self.getToken(aprendaParser.NEQ, 0)

        def LT(self):
            return self.getToken(aprendaParser.LT, 0)

        def GT(self):
            return self.getToken(aprendaParser.GT, 0)

        def getRuleIndex(self):
            return aprendaParser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = aprendaParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 18
        self.enterRecursionRule(localctx, 18, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 109
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.state = 100
                self.match(aprendaParser.LPAREN)
                self.state = 101
                self.expr(0)
                self.state = 102
                self.match(aprendaParser.RPAREN)
                pass

            elif la_ == 2:
                self.state = 104
                self.match(aprendaParser.MINUS)
                self.state = 105
                self.expr(4)
                pass

            elif la_ == 3:
                self.state = 106
                self.match(aprendaParser.ID)
                pass

            elif la_ == 4:
                self.state = 107
                self.match(aprendaParser.NUMBER)
                pass

            elif la_ == 5:
                self.state = 108
                self.llamada_funcion()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 119
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,10,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 117
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
                    if la_ == 1:
                        localctx = aprendaParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 111
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 112
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 480) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 113
                        self.expr(8)
                        pass

                    elif la_ == 2:
                        localctx = aprendaParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 114
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 115
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 7680) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 116
                        self.expr(7)
                        pass

             
                self.state = 121
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,10,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[9] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 6)
         




