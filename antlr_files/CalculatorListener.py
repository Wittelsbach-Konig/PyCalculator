# Generated from grammar/Calculator.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .CalculatorParser import CalculatorParser
else:
    from CalculatorParser import CalculatorParser

# This class defines a complete listener for a parse tree produced by CalculatorParser.
class CalculatorListener(ParseTreeListener):

    # Enter a parse tree produced by CalculatorParser#program.
    def enterProgram(self, ctx:CalculatorParser.ProgramContext):
        pass

    # Exit a parse tree produced by CalculatorParser#program.
    def exitProgram(self, ctx:CalculatorParser.ProgramContext):
        pass


    # Enter a parse tree produced by CalculatorParser#LargeExpr.
    def enterLargeExpr(self, ctx:CalculatorParser.LargeExprContext):
        pass

    # Exit a parse tree produced by CalculatorParser#LargeExpr.
    def exitLargeExpr(self, ctx:CalculatorParser.LargeExprContext):
        pass


    # Enter a parse tree produced by CalculatorParser#PlusMinus.
    def enterPlusMinus(self, ctx:CalculatorParser.PlusMinusContext):
        pass

    # Exit a parse tree produced by CalculatorParser#PlusMinus.
    def exitPlusMinus(self, ctx:CalculatorParser.PlusMinusContext):
        pass


    # Enter a parse tree produced by CalculatorParser#Function.
    def enterFunction(self, ctx:CalculatorParser.FunctionContext):
        pass

    # Exit a parse tree produced by CalculatorParser#Function.
    def exitFunction(self, ctx:CalculatorParser.FunctionContext):
        pass


    # Enter a parse tree produced by CalculatorParser#SignedExpr.
    def enterSignedExpr(self, ctx:CalculatorParser.SignedExprContext):
        pass

    # Exit a parse tree produced by CalculatorParser#SignedExpr.
    def exitSignedExpr(self, ctx:CalculatorParser.SignedExprContext):
        pass


    # Enter a parse tree produced by CalculatorParser#MulDiv.
    def enterMulDiv(self, ctx:CalculatorParser.MulDivContext):
        pass

    # Exit a parse tree produced by CalculatorParser#MulDiv.
    def exitMulDiv(self, ctx:CalculatorParser.MulDivContext):
        pass


    # Enter a parse tree produced by CalculatorParser#Pow.
    def enterPow(self, ctx:CalculatorParser.PowContext):
        pass

    # Exit a parse tree produced by CalculatorParser#Pow.
    def exitPow(self, ctx:CalculatorParser.PowContext):
        pass


    # Enter a parse tree produced by CalculatorParser#TrivialAtom.
    def enterTrivialAtom(self, ctx:CalculatorParser.TrivialAtomContext):
        pass

    # Exit a parse tree produced by CalculatorParser#TrivialAtom.
    def exitTrivialAtom(self, ctx:CalculatorParser.TrivialAtomContext):
        pass


    # Enter a parse tree produced by CalculatorParser#Paren.
    def enterParen(self, ctx:CalculatorParser.ParenContext):
        pass

    # Exit a parse tree produced by CalculatorParser#Paren.
    def exitParen(self, ctx:CalculatorParser.ParenContext):
        pass


    # Enter a parse tree produced by CalculatorParser#atom.
    def enterAtom(self, ctx:CalculatorParser.AtomContext):
        pass

    # Exit a parse tree produced by CalculatorParser#atom.
    def exitAtom(self, ctx:CalculatorParser.AtomContext):
        pass


    # Enter a parse tree produced by CalculatorParser#func_.
    def enterFunc_(self, ctx:CalculatorParser.Func_Context):
        pass

    # Exit a parse tree produced by CalculatorParser#func_.
    def exitFunc_(self, ctx:CalculatorParser.Func_Context):
        pass


    # Enter a parse tree produced by CalculatorParser#functionname.
    def enterFunctionname(self, ctx:CalculatorParser.FunctionnameContext):
        pass

    # Exit a parse tree produced by CalculatorParser#functionname.
    def exitFunctionname(self, ctx:CalculatorParser.FunctionnameContext):
        pass



del CalculatorParser