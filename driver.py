import sys
from antlr4 import *
from aprendaLexer import aprendaLexer
from aprendaParser import aprendaParser

def ejecutar_parser(entrada):
    input_stream = InputStream(entrada)

    lexer = aprendaLexer(input_stream)
    token_stream = CommonTokenStream(lexer)

    print("Tokens generados:")
    lexer.reset()
    for token in lexer.getAllTokens():
        token_type = token.type

        if token_type < len(lexer.symbolicNames) and lexer.symbolicNames[token_type]:
            token_name = lexer.symbolicNames[token_type]
        elif token_type < len(lexer.literalNames) and lexer.literalNames[token_type]:
            token_name = lexer.literalNames[token_type]
        else:
            token_name = f"Desconocido ({token_type})"

        if token_name.startswith("'") and token_name.endswith("'"):
            token_name = token_name[1:-1]

        print(f"Token: {token.text}, Tipo: {token_name}, Tipo_num: {token_type}")
    lexer.reset()

    parser = aprendaParser(token_stream)

    parser.removeErrorListeners()
    parser.addErrorListener(DiagnosticErrorListener())

    try:
        print("\nIniciando el parseo...")
        tree = parser.programa()
        print("Parseo exitoso.")
    except Exception as e:
        print(f"Error durante el parseo: {e}")

if __name__ == "__main__":
    entrada = """
    imprimir("Hola, mundo");
    si (5 > 3) {
        imprimir("5 es mayor que 3");
    } sino {
        imprimir("5 no es mayor que 3");
    }
    """
    ejecutar_parser(entrada)
