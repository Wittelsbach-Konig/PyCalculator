from math import log, log10, log2, exp, expm1, sin, cos, tan, degrees, radians

from antlr4 import ParseTreeWalker

from antlr_files.CalculatorParser import CalculatorParser
from antlr_files.CalculatorListener import CalculatorListener
from stack.stack import Stack


OPERATIONS = {
    '+': lambda a, b: a + b,
    '-': lambda a, b: a - b,
    '*': lambda a, b: a * b,
    '/': lambda a, b: a / b,
    '**': lambda a, b: pow(a, b),
}

FUNCTIONS = {
    'abs': lambda a: abs(a),
    'round': lambda a: round(a),
    'log': lambda a: log(a),
    'log10': lambda a: log10(a),
    'log2': lambda a: log2(a),
    'exp': lambda a: exp(a),
    'expm1': lambda a: expm1(a),
    'sin': lambda a: sin(a),
    'cos': lambda a: cos(a),
    'tan': lambda a: tan(a),
    'degrees': lambda a: degrees(a),
    'radians': lambda a: radians(a),
    'pow': lambda a, b: pow(a, b),
}


class MyListener(CalculatorListener):
    """Listener class."""

    def __init__(self, debug=False):
        self.stack = Stack()
        self.result = {}
        self.debug_mode = debug

    def operation(self, ctx):
        b = self.stack.pop()
        a = self.stack.pop()
        self.stack.push(OPERATIONS[ctx.getChild(1).getText()](a, b))

    def run(self, tree: CalculatorParser.ProgramContext) -> dict:
        """Метод для прохождения по дереву."""
        ParseTreeWalker().walk(self, tree)
        return self.result

    def exitLargeExpr(self, ctx: CalculatorParser.LargeExprContext):
        """
        Автоматически вызывается,
        когда парсер встречает большое выражение.
        """
        self.result[ctx.getChild(0).getText()] = self.stack.pop()
        if self.debug_mode:
            print("Exiting largeExpr rule")
            print("LargeExpr rule", ctx.getText())

    def exitPlusMinus(self, ctx: CalculatorParser.PlusMinusContext):
        """Автоматически вызывается, когда парсер встречает оператор + или -"""
        self.operation(ctx)
        if self.debug_mode:
            print("Exiting plusMinus rule")
            print("PlusMinus rule", ctx.getText())

    def exitMulDiv(self, ctx: CalculatorParser.MulDivContext):
        """Автоматически вызывается, когда парсер встречает оператор * или /"""
        self.operation(ctx)
        if self.debug_mode:
            print("Exiting mulDiv rule")
            print("MulDiv rule", ctx.getText())

    def exitPow(self, ctx: CalculatorParser.PowContext):
        """Автоматически вызывается, когда парсер встречает оператор ^"""
        self.operation(ctx)
        if self.debug_mode:
            print("Exiting pow rule")
            print("Pow rule", ctx.getText())

    def exitSignedExpr(self, ctx: CalculatorParser.SignedExprContext):
        """Автоматически вызывается, когда парсер встречает унарный оператор"""
        if ctx.getChild(0).getText() == '-':
            self.stack.push(-1 * self.stack.pop())
        if self.debug_mode:
            print("Exiting signedExpr rule")
            print("SignedExpr rule", ctx.getText())

    def exitAtom(self, ctx: CalculatorParser.AtomContext):
        """Автоматически вызывается, когда парсер встречает число"""
        value = ctx.getText()
        self.stack.push(float(value))
        if self.debug_mode:
            print("Exiting atom rule")
            print("Atom rule", ctx.getText())
            print(self.stack)

    def exitFunc_(self, ctx: CalculatorParser.Func_Context):
        """Автоматически вызывается, когда парсер встречает функцию"""
        args = []
        for i in range(ctx.getChildCount()//2 - 1):
            args.append(self.stack.pop())
        args.reverse()
        func = self.stack.pop()
        self.stack.push(func(*tuple(args)))
        if self.debug_mode:
            print("Exiting func_ rule")
            print("Func_ rule", ctx.getText())
            for i in range(ctx.getChildCount()):
                print(ctx.getChild(i).getText())
            print(self.stack)

    def exitFunctionname(self, ctx: CalculatorParser.FunctionnameContext):
        """Автоматически вызывается, когда парсер встречает имя функции"""
        self.stack.push(FUNCTIONS[ctx.getText()])
        if self.debug_mode:
            print("Exiting functionname rule")
            print("Functionname rule", ctx.getText())
