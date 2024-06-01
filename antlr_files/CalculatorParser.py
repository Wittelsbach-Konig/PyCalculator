# Generated from grammar/Calculator.g4 by ANTLR 4.13.1
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
        4,1,12,68,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,1,0,1,
        0,1,0,5,0,16,8,0,10,0,12,0,19,9,0,1,0,1,0,1,1,1,1,1,2,1,2,1,2,1,
        2,1,2,1,2,1,2,1,2,1,2,3,2,34,8,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,
        1,2,5,2,45,8,2,10,2,12,2,48,9,2,1,3,1,3,1,4,1,4,1,4,1,4,1,4,5,4,
        57,8,4,10,4,12,4,60,9,4,3,4,62,8,4,1,4,1,4,1,5,1,5,1,5,0,1,4,6,0,
        2,4,6,8,10,0,2,1,0,1,2,1,0,3,4,70,0,12,1,0,0,0,2,22,1,0,0,0,4,33,
        1,0,0,0,6,49,1,0,0,0,8,51,1,0,0,0,10,65,1,0,0,0,12,17,3,2,1,0,13,
        14,5,7,0,0,14,16,3,2,1,0,15,13,1,0,0,0,16,19,1,0,0,0,17,15,1,0,0,
        0,17,18,1,0,0,0,18,20,1,0,0,0,19,17,1,0,0,0,20,21,5,0,0,1,21,1,1,
        0,0,0,22,23,3,4,2,0,23,3,1,0,0,0,24,25,6,2,-1,0,25,34,3,6,3,0,26,
        34,3,8,4,0,27,28,7,0,0,0,28,34,3,4,2,5,29,30,5,8,0,0,30,31,3,4,2,
        0,31,32,5,9,0,0,32,34,1,0,0,0,33,24,1,0,0,0,33,26,1,0,0,0,33,27,
        1,0,0,0,33,29,1,0,0,0,34,46,1,0,0,0,35,36,10,4,0,0,36,37,5,5,0,0,
        37,45,3,4,2,4,38,39,10,3,0,0,39,40,7,1,0,0,40,45,3,4,2,4,41,42,10,
        2,0,0,42,43,7,0,0,0,43,45,3,4,2,3,44,35,1,0,0,0,44,38,1,0,0,0,44,
        41,1,0,0,0,45,48,1,0,0,0,46,44,1,0,0,0,46,47,1,0,0,0,47,5,1,0,0,
        0,48,46,1,0,0,0,49,50,5,10,0,0,50,7,1,0,0,0,51,52,3,10,5,0,52,61,
        5,8,0,0,53,58,3,4,2,0,54,55,5,6,0,0,55,57,3,4,2,0,56,54,1,0,0,0,
        57,60,1,0,0,0,58,56,1,0,0,0,58,59,1,0,0,0,59,62,1,0,0,0,60,58,1,
        0,0,0,61,53,1,0,0,0,61,62,1,0,0,0,62,63,1,0,0,0,63,64,5,9,0,0,64,
        9,1,0,0,0,65,66,5,11,0,0,66,11,1,0,0,0,6,17,33,44,46,58,61
    ]

class CalculatorParser ( Parser ):

    grammarFileName = "Calculator.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'+'", "'-'", "'*'", "'/'", "'**'", "','", 
                     "';'", "'('", "')'" ]

    symbolicNames = [ "<INVALID>", "PLUS", "MINUS", "TIMES", "DIV", "POW", 
                      "COMMA", "SEMI", "LPAREN", "RPAREN", "NUMBER", "ID", 
                      "WS" ]

    RULE_program = 0
    RULE_lexpr = 1
    RULE_expr = 2
    RULE_atom = 3
    RULE_func_ = 4
    RULE_functionname = 5

    ruleNames =  [ "program", "lexpr", "expr", "atom", "func_", "functionname" ]

    EOF = Token.EOF
    PLUS=1
    MINUS=2
    TIMES=3
    DIV=4
    POW=5
    COMMA=6
    SEMI=7
    LPAREN=8
    RPAREN=9
    NUMBER=10
    ID=11
    WS=12

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def lexpr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CalculatorParser.LexprContext)
            else:
                return self.getTypedRuleContext(CalculatorParser.LexprContext,i)


        def EOF(self):
            return self.getToken(CalculatorParser.EOF, 0)

        def SEMI(self, i:int=None):
            if i is None:
                return self.getTokens(CalculatorParser.SEMI)
            else:
                return self.getToken(CalculatorParser.SEMI, i)

        def getRuleIndex(self):
            return CalculatorParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)




    def program(self):

        localctx = CalculatorParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 12
            self.lexpr()
            self.state = 17
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==7:
                self.state = 13
                self.match(CalculatorParser.SEMI)
                self.state = 14
                self.lexpr()
                self.state = 19
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 20
            self.match(CalculatorParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LexprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return CalculatorParser.RULE_lexpr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class LargeExprContext(LexprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CalculatorParser.LexprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(CalculatorParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLargeExpr" ):
                listener.enterLargeExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLargeExpr" ):
                listener.exitLargeExpr(self)



    def lexpr(self):

        localctx = CalculatorParser.LexprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_lexpr)
        try:
            localctx = CalculatorParser.LargeExprContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 22
            self.expr(0)
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


        def getRuleIndex(self):
            return CalculatorParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class PlusMinusContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CalculatorParser.ExprContext
            super().__init__(parser)
            self.a = None # ExprContext
            self.b = None # ExprContext
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CalculatorParser.ExprContext)
            else:
                return self.getTypedRuleContext(CalculatorParser.ExprContext,i)

        def PLUS(self):
            return self.getToken(CalculatorParser.PLUS, 0)
        def MINUS(self):
            return self.getToken(CalculatorParser.MINUS, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPlusMinus" ):
                listener.enterPlusMinus(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPlusMinus" ):
                listener.exitPlusMinus(self)


    class FunctionContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CalculatorParser.ExprContext
            super().__init__(parser)
            self.a = None # Func_Context
            self.copyFrom(ctx)

        def func_(self):
            return self.getTypedRuleContext(CalculatorParser.Func_Context,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunction" ):
                listener.enterFunction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunction" ):
                listener.exitFunction(self)


    class SignedExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CalculatorParser.ExprContext
            super().__init__(parser)
            self.a = None # Token
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(CalculatorParser.ExprContext,0)

        def PLUS(self):
            return self.getToken(CalculatorParser.PLUS, 0)
        def MINUS(self):
            return self.getToken(CalculatorParser.MINUS, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSignedExpr" ):
                listener.enterSignedExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSignedExpr" ):
                listener.exitSignedExpr(self)


    class MulDivContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CalculatorParser.ExprContext
            super().__init__(parser)
            self.a = None # ExprContext
            self.b = None # ExprContext
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CalculatorParser.ExprContext)
            else:
                return self.getTypedRuleContext(CalculatorParser.ExprContext,i)

        def TIMES(self):
            return self.getToken(CalculatorParser.TIMES, 0)
        def DIV(self):
            return self.getToken(CalculatorParser.DIV, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMulDiv" ):
                listener.enterMulDiv(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMulDiv" ):
                listener.exitMulDiv(self)


    class PowContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CalculatorParser.ExprContext
            super().__init__(parser)
            self.a = None # ExprContext
            self.b = None # ExprContext
            self.copyFrom(ctx)

        def POW(self):
            return self.getToken(CalculatorParser.POW, 0)
        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CalculatorParser.ExprContext)
            else:
                return self.getTypedRuleContext(CalculatorParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPow" ):
                listener.enterPow(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPow" ):
                listener.exitPow(self)


    class TrivialAtomContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CalculatorParser.ExprContext
            super().__init__(parser)
            self.a = None # AtomContext
            self.copyFrom(ctx)

        def atom(self):
            return self.getTypedRuleContext(CalculatorParser.AtomContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTrivialAtom" ):
                listener.enterTrivialAtom(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTrivialAtom" ):
                listener.exitTrivialAtom(self)


    class ParenContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CalculatorParser.ExprContext
            super().__init__(parser)
            self.a = None # ExprContext
            self.copyFrom(ctx)

        def LPAREN(self):
            return self.getToken(CalculatorParser.LPAREN, 0)
        def RPAREN(self):
            return self.getToken(CalculatorParser.RPAREN, 0)
        def expr(self):
            return self.getTypedRuleContext(CalculatorParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParen" ):
                listener.enterParen(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParen" ):
                listener.exitParen(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = CalculatorParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 4
        self.enterRecursionRule(localctx, 4, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 33
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [10]:
                localctx = CalculatorParser.TrivialAtomContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 25
                localctx.a = self.atom()
                pass
            elif token in [11]:
                localctx = CalculatorParser.FunctionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 26
                localctx.a = self.func_()
                pass
            elif token in [1, 2]:
                localctx = CalculatorParser.SignedExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 27
                localctx.a = self._input.LT(1)
                _la = self._input.LA(1)
                if not(_la==1 or _la==2):
                    localctx.a = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 28
                self.expr(5)
                pass
            elif token in [8]:
                localctx = CalculatorParser.ParenContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 29
                self.match(CalculatorParser.LPAREN)
                self.state = 30
                localctx.a = self.expr(0)
                self.state = 31
                self.match(CalculatorParser.RPAREN)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 46
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 44
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
                    if la_ == 1:
                        localctx = CalculatorParser.PowContext(self, CalculatorParser.ExprContext(self, _parentctx, _parentState))
                        localctx.a = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 35
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 36
                        self.match(CalculatorParser.POW)
                        self.state = 37
                        localctx.b = self.expr(4)
                        pass

                    elif la_ == 2:
                        localctx = CalculatorParser.MulDivContext(self, CalculatorParser.ExprContext(self, _parentctx, _parentState))
                        localctx.a = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 38
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 39
                        _la = self._input.LA(1)
                        if not(_la==3 or _la==4):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 40
                        localctx.b = self.expr(4)
                        pass

                    elif la_ == 3:
                        localctx = CalculatorParser.PlusMinusContext(self, CalculatorParser.ExprContext(self, _parentctx, _parentState))
                        localctx.a = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 41
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 42
                        _la = self._input.LA(1)
                        if not(_la==1 or _la==2):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 43
                        localctx.b = self.expr(3)
                        pass

             
                self.state = 48
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class AtomContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self):
            return self.getToken(CalculatorParser.NUMBER, 0)

        def getRuleIndex(self):
            return CalculatorParser.RULE_atom

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAtom" ):
                listener.enterAtom(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAtom" ):
                listener.exitAtom(self)




    def atom(self):

        localctx = CalculatorParser.AtomContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_atom)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 49
            self.match(CalculatorParser.NUMBER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Func_Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def functionname(self):
            return self.getTypedRuleContext(CalculatorParser.FunctionnameContext,0)


        def LPAREN(self):
            return self.getToken(CalculatorParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(CalculatorParser.RPAREN, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CalculatorParser.ExprContext)
            else:
                return self.getTypedRuleContext(CalculatorParser.ExprContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(CalculatorParser.COMMA)
            else:
                return self.getToken(CalculatorParser.COMMA, i)

        def getRuleIndex(self):
            return CalculatorParser.RULE_func_

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunc_" ):
                listener.enterFunc_(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunc_" ):
                listener.exitFunc_(self)




    def func_(self):

        localctx = CalculatorParser.Func_Context(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_func_)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 51
            self.functionname()
            self.state = 52
            self.match(CalculatorParser.LPAREN)
            self.state = 61
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 3334) != 0):
                self.state = 53
                self.expr(0)
                self.state = 58
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==6:
                    self.state = 54
                    self.match(CalculatorParser.COMMA)
                    self.state = 55
                    self.expr(0)
                    self.state = 60
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 63
            self.match(CalculatorParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionnameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(CalculatorParser.ID, 0)

        def getRuleIndex(self):
            return CalculatorParser.RULE_functionname

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionname" ):
                listener.enterFunctionname(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionname" ):
                listener.exitFunctionname(self)




    def functionname(self):

        localctx = CalculatorParser.FunctionnameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_functionname)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 65
            self.match(CalculatorParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[2] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         




