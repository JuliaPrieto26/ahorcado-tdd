class Ahorcado:

    def __init__(self):
        self.nombre = None
        self.palabra = ''
        self.letras_adivinadas = ['']
        self.cantidad_aciertos = 0
        self.cantidad_errores = 0
        self.cantidad_errores_permitidos = 6
        self.codigo_estado = 0 # 0: sigue jugando, 1: ganó, -1: perdió.
        self.estado = []
        self.letras_erroneas = []

    def get_nombre(self):
        return self.nombre

    def set_palabra(self, palabra):
        self.palabra = palabra.lower()
        self.estado = ['_' for _ in range(len(self.palabra))]

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

    def check_codigo_estado(self):
        if self.cantidad_errores == self.cantidad_errores_permitidos:
            self.codigo_estado = -1
        if self.cantidad_aciertos == len(self.palabra):
            self.codigo_estado = 1
        return self.codigo_estado

    def get_estado(self):
        return ' '.join(self.estado)

    def get_letras_erroneas(self):
        return ' '.join(self.letras_erroneas)

    def arriesgar_una_palabra(self, palabra):
        if palabra == self.palabra:
            self.estado = self.palabra
            return True
        else:
            return False

    def arriesgar_una_letra(self, letra):
        letra = letra.lower()
        if letra in self.palabra:
            if letra not in self.letras_adivinadas:
                self.letras_adivinadas.append(letra)
                self.cantidad_aciertos += self.palabra.count(letra)

                for i, letra_valida in enumerate(self.palabra):
                    if letra == letra_valida:
                        self.estado[i] = letra

            return True
        self.cantidad_errores += 1
        self.letras_erroneas.append(letra)
        return False
