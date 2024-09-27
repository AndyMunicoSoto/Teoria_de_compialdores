import sys
from antlr4 import *
from aprendaLexer import aprendaLexer
from aprendaParser import aprendaParser

def ejecutar_parser(entrada):
    # Crear un input stream a partir del código fuente
    input_stream = InputStream(entrada)

    # Pasar el input al lexer
    lexer = aprendaLexer(input_stream)
    token_stream = CommonTokenStream(lexer)

    # Imprimir los tokens generados para verificar el análisis léxico
    print("Tokens generados:")
    lexer.reset()
    for token in lexer.getAllTokens():
        token_type = token.type

        # Intentar obtener el nombre del token de symbolicNames o literalNames
        if token_type < len(lexer.symbolicNames) and lexer.symbolicNames[token_type]:
            token_name = lexer.symbolicNames[token_type]
        elif token_type < len(lexer.literalNames) and lexer.literalNames[token_type]:
            token_name = lexer.literalNames[token_type]
        else:
            token_name = f"Desconocido ({token_type})"

        # Remover comillas simples de los literalNames
        if token_name.startswith("'") and token_name.endswith("'"):
            token_name = token_name[1:-1]

        print(f"Token: {token.text}, Tipo: {token_name}, Tipo_num: {token_type}")
    lexer.reset()

    # Pasar el flujo de tokens al parser
    parser = aprendaParser(token_stream)

    # Mostrar errores sintácticos
    parser.removeErrorListeners()
    parser.addErrorListener(DiagnosticErrorListener())

    # Iniciar el parseo desde la regla inicial
    try:
        print("\nIniciando el parseo...")
        tree = parser.programa()  # Parsear desde la regla principal 'programa'
        print("Parseo exitoso.")
    except Exception as e:
        print(f"Error durante el parseo: {e}")

if __name__ == "__main__":
    # Leer el código de entrada (entrada directa para simplicidad)
    entrada = """
    imprimir("Hola, mundo");
    si (5 + 2 > 6) {
        imprimir("Condición verdadera");
    } sino {
        imprimir("Condición falsa");
    }
    """
    ejecutar_parser(entrada)
