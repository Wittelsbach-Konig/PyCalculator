import argparse

from antlr4 import FileStream, CommonTokenStream

from antlr_files.CalculatorLexer import CalculatorLexer
from antlr_files.CalculatorParser import CalculatorParser
from MyListener import MyListener


def main(input, debug):
    input_stream = FileStream(input)
    lexer = CalculatorLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = CalculatorParser(stream)
    tree = parser.program()
    if parser.getNumberOfSyntaxErrors() > 0:
        print("syntax error: " + str(parser.getNumberOfSyntaxErrors()))
    else:
        listener = MyListener(debug)
        result = listener.run(tree)
        for key, value in result.items():
            print(f"{key} = {value}")


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--input',
        dest='input',
        type=str,
        required=True,
        help='path to input file with math expression',
    )
    parser.add_argument(
        '--debug',
        action='store_true',
        required=False,
        help='enable debug mode',
    )
    args = parser.parse_args()
    main(args.input, args.debug)
