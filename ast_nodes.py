class Nodo:
    pass

class Programa(Nodo):
    def __init__(self, instrucciones):
        self.instrucciones = instrucciones

    def __str__(self):
        instrucciones_str = ', '.join(str(instr) for instr in self.instrucciones)
        return f"Programa([{instrucciones_str}])"

class NodoDeclaracion(Nodo):
    def __init__(self, tipo, nombre):
        self.tipo = tipo
        self.nombre = nombre

    def __str__(self):
        return f"Declaracion({self.tipo} {self.nombre})"

class NodoAsignacion(Nodo):
    def __init__(self, identificador, expresion):
        self.identificador = identificador
        self.expresion = expresion

    def __str__(self):
        return f"Asig({self.identificador} = {self.expresion})"

class NodoImprimir(Nodo):
    def __init__(self, mensaje):
        self.mensaje = mensaje

    def __str__(self):
        return f"Imprimir({self.mensaje})"

class NodoLlamadaFuncion(Nodo):
    def __init__(self, nombre, argumentos):
        self.nombre = nombre
        self.argumentos = argumentos

    def __str__(self):
        argumentos_str = ', '.join(str(arg) for arg in self.argumentos)
        return f"Llamada({self.nombre}({argumentos_str}))"

class NodoFuncion(Nodo):
    def __init__(self, nombre, parametros, bloque):
        self.nombre = nombre
        self.parametros = parametros
        self.bloque = bloque

    def __str__(self):
        parametros_str = ', '.join(self.parametros)
        bloque_str = ', '.join(str(instr) for instr in self.bloque)
        return f"Funcion({self.nombre}({parametros_str}) {{ {bloque_str} }})"

class NodoCondicional(Nodo):
    def __init__(self, condicion, bloque_true, bloque_false=None):
        self.condicion = condicion
        self.bloque_true = bloque_true
        self.bloque_false = bloque_false

    def __str__(self):
        if self.bloque_false:
            bloque_false_str = ', '.join(str(instr) for instr in self.bloque_false)
            return f"Si({self.condicion}) {{ {', '.join(str(instr) for instr in self.bloque_true)} }} Sino {{ {bloque_false_str} }}"
        else:
            return f"Si({self.condicion}) {{ {', '.join(str(instr) for instr in self.bloque_true)} }}"

class NodoBucle(Nodo):
    def __init__(self, condicion, bloque):
        self.condicion = condicion
        self.bloque = bloque

    def __str__(self):
        return f"Mientras({self.condicion}) {{ {', '.join(str(instr) for instr in self.bloque)} }}"

class NodoExpresion(Nodo):
    def __init__(self, operador, izquierdo, derecho=None):
        self.operador = operador
        self.izquierdo = izquierdo
        self.derecho = derecho

    def __str__(self):
        if self.derecho:
            return f"({self.izquierdo} {self.operador} {self.derecho})"
        else:
            return f"({self.operador}{self.izquierdo})"

class NodoIdentificador(Nodo):
    def __init__(self, nombre):
        self.nombre = nombre

    def __str__(self):
        return self.nombre

class NodoNumero(Nodo):
    def __init__(self, valor):
        self.valor = valor

    def __str__(self):
        return str(self.valor)

class NodoCadena(Nodo):
    def __init__(self, valor):
        self.valor = valor

    def __str__(self):
        return f'"{self.valor}"'
