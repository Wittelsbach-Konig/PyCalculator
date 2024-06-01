grammar Calculator;

program : lexpr (SEMI lexpr)* EOF
    ;

lexpr : expr                            # LargeExpr
    ;

expr
    : a=atom                            # TrivialAtom
    | a=func_                           # Function
    | a=(PLUS | MINUS) expr             # SignedExpr
    | <assoc=right> a=expr POW b=expr   # Pow
    | a=expr (TIMES | DIV) b=expr       # MulDiv
    | a=expr (PLUS | MINUS) b=expr      # PlusMinus
    | LPAREN a=expr RPAREN              # Paren
    ;

atom
    : NUMBER
    ;

func_
    : functionname LPAREN (expr (COMMA expr)*)? RPAREN
    ;

functionname
    : ID
    ;

PLUS: '+';
MINUS: '-';
TIMES: '*';
DIV: '/';
POW: '**';
COMMA : ',' ;
SEMI : ';' ;
LPAREN : '(' ;
RPAREN : ')' ;
NUMBER: [0-9]+('.'[0-9]*)?;
ID: [a-zA-Z_][a-zA-Z_0-9]* ;
WS: [ \t\n\r\f]+ -> skip ;