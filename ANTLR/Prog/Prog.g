grammar Prog;
root: accio+ EOF;
accio: assig | write | conditional;

assig: VAR ':=' expr;
write: 'write' expr;
conditional: 'if' boolExp 'then' accio+ 'endif';

boolExp: expr EQ expr
    | expr NEQ expr
    | expr LT expr
    | expr LEQ expr
    | expr GT expr
    | expr GEQ expr;

expr:
	< assoc = right> expr POT expr
	| expr MUL expr
	| expr DIV expr
	| expr SUM expr
	| expr DIF expr
	| sym;

sym: VAR | NUM;

EQ: '=';
NEQ: '<>';
LT: '<';
LEQ: '<=';
GT: '>';
GEQ: '>=';
POT: '^';
MUL: '*';
DIV: '/';
SUM: '+';
DIF: '-';
VAR: [a-z]+;
NUM: [0-9]+;
WS: [ \n\r]+ -> skip;
