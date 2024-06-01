#!/bin/bash
alias antlr4='java -jar /usr/local/lib/antlr-4.13.1-complete.jar'
antlr4 -Dlanguage=Python3 grammar/Expr.g4 -Xexact-output-dir -o ./python_LexParLis/