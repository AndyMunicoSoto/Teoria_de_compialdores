grammar aprenda;

// Reglas léxicas
IF      : 'si';
ELSE    : 'sino';
WHILE   : 'mientras';
PRINT   : 'imprimir';
FUNCION : 'funcion';
ID      : [a-zA-Z_]+;
NUMBER  : [0-9]+;
STRING  : '"' .*? '"';
WS      : [ \t\r\n]+ -> skip;  // Ignorar espacios en blanco

// Reglas sintácticas
programa    : (instruccion)* ;
instruccion : imprimir | asignacion | condicional | bucle | funcion | llamada_funcion ;

imprimir    : PRINT '(' STRING ')' ';' ;
asignacion  : ID '=' expr ';' ;
condicional : IF '(' expr ')' '{' (instruccion)* '}' (ELSE '{' (instruccion)* '}')? ;
bucle       : WHILE '(' expr ')' '{' (instruccion)* '}' ;
funcion     : FUNCION ID '(' (ID (',' ID)*)? ')' '{' (instruccion)* '}' ;
llamada_funcion : ID '(' (expr (',' expr)*)? ')' ';' ;

// Expresiones
expr : expr ('+' | '-' | '*' | '/') expr   // Operaciones aritméticas
     | expr ('==' | '!=' | '<' | '>') expr // Operaciones lógicas
     | NUMBER                              // Números
     | ID                                  // Variables
     | '(' expr ')'                        // Expresiones agrupadas
     ;