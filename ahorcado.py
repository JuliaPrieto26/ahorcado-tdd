class Ahorcado:

    def __init__(self):
        self.nombre = None
        self.palabra = None

    def get_nombre(self):
        return self.nombre

    def set_palabra(self, palabra):
        self.palabra = palabra

    def login(self, nombre):
        if len(nombre) == 0:
            raise Exception('El nombre no debe ser vacío')
        elif len(nombre) > 30:
            raise Exception('El nombre no debe debe tener mas de 30 caracteres')
        elif not nombre.isalpha():
            raise Exception('El nombre no debe tener caracteres invalidos')
        else:
            self.nombre = nombre

    def arriesgar_una_palabra(self, palabra):
        if palabra == self.palabra:
            return True
        else:
            return False
