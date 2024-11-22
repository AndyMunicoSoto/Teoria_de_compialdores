def imprimir_ast(nodo, indent=0):
    prefix = '  ' * indent
    if isinstance(nodo, list):
        for elem in nodo:
            imprimir_ast(elem, indent)
    elif hasattr(nodo, '__str__'):
        print(f"{prefix}{str(nodo)}")
    else:
        print(f"{prefix}{nodo}")
if __name__ == "__main__":
    codigo = '''
    funcion saludar(nombre) {
        imprimir("Hola, " + nombre);
    }

    saludar("Mundo");
    '''
    ast = construir_ast(codigo)
    imprimir_ast(ast)
