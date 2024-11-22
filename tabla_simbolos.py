
class Simbolo:
    def __init__(self, nombre, tipo, params=None):
        self.nombre = nombre
        self.tipo = tipo
        self.params = params or []

class TablaSimbolos:
    def __init__(self, padre=None):
        self.padre = padre
        self.simbolos = {}

    def definir(self, simbolo):
        if simbolo.nombre in self.simbolos:
            raise Exception(f"Símbolo '{simbolo.nombre}' ya está definido en este ámbito.")
        self.simbolos[simbolo.nombre] = simbolo
        print(f"Definiendo símbolo: {simbolo.nombre} de tipo '{simbolo.tipo}'")
    def obtener(self, nombre):
        simbolo = self.simbolos.get(nombre)
        if simbolo:
            return simbolo
        elif self.padre:
            return self.padre.obtener(nombre)
        else:
            return None

    def existe_en_ambito_actual(self, nombre):
        return nombre in self.simbolos
