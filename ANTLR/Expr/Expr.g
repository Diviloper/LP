grammar Expr;
root : expr EOF ;
expr : < assoc = right > expr POT expr 
    | expr MUL expr
    | expr DIV expr
    | expr SUM expr
    | expr DIF expr
    | NUM
    ;
POT : '^' ;
MUL : '*' ;
DIV : '/' ;
SUM : '+' ;
DIF : '-' ;
NUM : [0-9]+ ;
WS : [ \n]+ -> skip ;