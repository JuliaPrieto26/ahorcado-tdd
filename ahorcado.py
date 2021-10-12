class Ahorcado:

    def __init__(self):
        self.nombre = None
        self.palabra = ''
        self.letras_adivinadas = ['']
        self.cantidad_aciertos = 0
        self.cantidad_errores = 0
        self.cantidad_errores_permitidos = 6
        self.estado = 0 # 0: sigue jugando, 1: ganó, -1: perdió.

    def get_nombre(self):
        return self.nombre

    def set_palabra(self, palabra):
        self.palabra = palabra.lower()

    def login(self, nombre):
        if len(nombre) == 0:
            raise Exception('El nombre no debe ser vacío')
        elif len(nombre) > 30:
            raise Exception('El nombre no debe debe tener mas de 30 caracteres')
        elif not nombre.isalpha():
            raise Exception('El nombre no debe tener caracteres invalidos')
        else:
            self.nombre = nombre

    def get_aciertos_errores(self):
        return self.cantidad_aciertos, self.cantidad_errores

    def check_estado(self):
        if self.cantidad_errores == self.cantidad_errores_permitidos:
            self.estado = -1
        if self.cantidad_aciertos == len(self.palabra):
            self.estado = 1
        return self.estado

    def arriesgar_una_palabra(self, palabra):
        if palabra == self.palabra:
            return True
        else:
            return False

    def arriesgar_una_letra(self, letra):
        letra = letra.lower()
        if letra in self.palabra:
            if letra not in self.letras_adivinadas:
                self.letras_adivinadas.append(letra)
                self.cantidad_aciertos += self.palabra.count(letra)
            return True
        self.cantidad_errores += 1
        return False
