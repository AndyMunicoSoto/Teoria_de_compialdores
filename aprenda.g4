grammar aprenda;

// Reglas léxicas (Tokens simbólicos primero)
LPAREN  : '(';
RPAREN  : ')';
SEMICOLON : ';';
EQUAL   : '=';
PLUS    : '+';
MINUS   : '-';
MUL     : '*';
DIV     : '/';
EQ      : '==';
NEQ     : '!=';
LT      : '<';
GT      : '>';
LBRACE  : '{';
RBRACE  : '}';
COMMA   : ',';    // Agregado

// Reglas para palabras clave
IF      : 'si';
ELSE    : 'sino';
WHILE   : 'mientras';
PRINT   : 'imprimir';
FUNCION : 'funcion';

// Identificadores y literales
ID      : [a-zA-Z_][a-zA-Z0-9_]*;
NUMBER  : [0-9]+;
STRING  : '"' .*? '"';

// Ignorar espacios en blanco y comentarios
WS      : [ \t\r\n]+ -> skip;
COMMENT : '/*' .*? '*/' -> skip;
LINE_COMMENT : '//' ~[\r\n]* -> skip;

// Reglas sintácticas principales
programa : (instruccion)+ ;

// Tipos de instrucciones
instruccion : imprimir
            | asignacion
            | condicional
            | bucle
            | funcion
            | llamada_funcion
            ;

// Regla para imprimir
imprimir : PRINT LPAREN STRING RPAREN SEMICOLON ;

// Regla para asignación de variables
asignacion : ID EQUAL expr SEMICOLON ;

// Regla para condicionales (si/sino)
condicional : IF LPAREN expr RPAREN bloque (ELSE bloque)? ;

// Regla para bucles (mientras)
bucle : WHILE LPAREN expr RPAREN bloque ;

// Definición de una función
funcion : FUNCION ID LPAREN (ID (COMMA ID)*)? RPAREN bloque ;

// Llamada de funciones
llamada_funcion : ID LPAREN (expr (COMMA expr)*)? RPAREN SEMICOLON ;

// Bloques de código (una o más instrucciones dentro de llaves)
bloque : LBRACE (instruccion)* RBRACE ;

// Expresiones aritméticas y lógicas
expr : expr (PLUS | MINUS | MUL | DIV) expr
     | expr (EQ | NEQ | LT | GT) expr
     | LPAREN expr RPAREN
     | MINUS expr
     | ID
     | NUMBER
     | llamada_funcion
     ;
