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
COMMA   : ',';

// Reglas para palabras clave
IF      : 'si';
ELSE    : 'sino';
WHILE   : 'mientras';
PRINT   : 'imprimir';
FUNCION : 'funcion';
INT     : 'int';
STRING  : 'string';

// Identificadores y literales
ID          : [a-zA-Z_][a-zA-Z0-9_]*;
NUMBER      : [0-9]+;
STRING_LITERAL  : '"' .*? '"'; // Renombrado para evitar conflictos

// Ignorar espacios en blanco y comentarios
WS          : [ \t\r\n]+ -> skip;
COMMENT     : '/*' .*? '*/' -> skip;
LINE_COMMENT : '//' ~[\r\n]* -> skip;

// Reglas sintácticas principales
programa : (instruccion)+ ;

// Tipos de instrucciones
instruccion
    : declaracion
    | imprimir
    | asignacion
    | condicional
    | bucle
    | funcion
    | llamada_funcion
    ;

// Regla para declaración de variables
declaracion : tipo ID SEMICOLON ;

// Regla para imprimir
imprimir : PRINT LPAREN expr RPAREN SEMICOLON ;

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

// Definición de tipos
tipo
    : INT
    | STRING
    ;

// Expresiones aritméticas y lógicas con precedencia
expr
    : expr op=EQ expr         # ExpresionComparacion
    | expr op=NEQ expr        # ExpresionComparacion
    | expr op=LT expr         # ExpresionComparacion
    | expr op=GT expr         # ExpresionComparacion
    | expr op=PLUS expr       # ExpresionSumaResta
    | expr op=MINUS expr      # ExpresionSumaResta
    | expr op=MUL expr        # ExpresionMultiplicacionDivision
    | expr op=DIV expr        # ExpresionMultiplicacionDivision
    | MINUS expr              # ExpresionUnaria
    | LPAREN expr RPAREN      # ExpresionParentesis
    | llamada_funcion         # ExpresionLlamadaFuncion
    | ID                      # ExpresionIdentificador
    | NUMBER                  # ExpresionNumero
    | STRING_LITERAL          # ExpresionCadena
    ;
