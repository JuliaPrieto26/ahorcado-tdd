"""
Contiene toda la funcionalidad del clásico juego del ahorcado.
Se permiten un máximo de 6 errores.
El jugador puede arriesgar tanto letras como palabras.
"""
# pylint: disable=too-many-instance-attributes
# pylint: disable=missing-class-docstring

class Ahorcado:

    cantidad_errores_permitidos = 6

    def __init__(self):
        """Inicializa una nueva partida de ahorcado."""
        self.palabra = ''
        self.letras_adivinadas = []
        self.cantidad_aciertos = 0
        self.cantidad_errores = 0
        self.codigo_estado = 0
        self.estado = []
        self.letras_erroneas = []
        self.nombre = None

    def inicializar_partida(self):
        """Inicializa la partida."""
        self.palabra = ''
        self.letras_adivinadas = []
        self.cantidad_aciertos = 0
        self.cantidad_errores = 0
        self.codigo_estado = 0
        self.estado = []
        self.letras_erroneas = []

    def get_nombre(self):
        """Retorna el nombre de usuario."""
        return self.nombre

    def set_palabra(self, palabra):
        """Establece la palabra a adivinar convirtiendola a minúsculas."""
        if len(palabra) < 3:
            raise Exception('La palabra debe tener al menos 3 caracteres.')
        elif len(palabra) > 20:
            raise Exception('La palabra no debe tener más de 20 caracteres.')
        if not palabra.isalpha():
            raise Exception('La palabra no debe contener símbolos.')

        self.palabra = palabra.lower()
        self.estado = ['_' for _ in range(len(self.palabra))]

    def get_palabra(self):
        """Retorna la palabra a adivinar de la partida."""
        return self.palabra

    def login(self, nombre):
        """
        Valida y registra el nombre de usuario ingresado.
        Lanza excepciones si ingresó vacío, si ingresó un nombre de más de 30 letras
        o si contiene caracteres inválidos.
        """

        if len(nombre) == 0:
            raise Exception('El nombre no debe ser vacío')
        if len(nombre) > 30:
            raise Exception('El nombre no debe debe tener mas de 30 caracteres')
        if not nombre.isalpha():
            raise Exception('El nombre no debe tener caracteres invalidos')

        self.nombre = nombre

    def get_aciertos_errores(self):
        """Retorna la cantidad actual de aciertos y errores en formato (aciertos, errores)."""

        return self.cantidad_aciertos, self.cantidad_errores

    def get_codigo_estado(self):
        """
        Retorna el codigo de estado actual de la partida.
            -1 --> la partida está perdida
            1 --> la partida está ganada
            0 --> la partida está en progreso
        """

        if self.cantidad_errores == self.cantidad_errores_permitidos:
            self.codigo_estado = -1
        elif self.cantidad_aciertos == len(self.palabra):
            self.codigo_estado = 1
        return self.codigo_estado

    def get_estado(self):
        """Retorna el estado actual de la partida."""

        return ' '.join(self.estado)

    def get_letras_erroneas(self):
        """Retorna todas las letras erroneas ingresadas hasta el momento, separadas por espacios."""

        return ' '.join(self.letras_erroneas)

    def arriesgar_una_palabra(self, palabra):
        """Evalúa la palabra arriesgada. Retorna verdadero si es la correcta y falso si no lo es."""
        if palabra.lower() == self.palabra:
            self.estado = self.palabra
            self.codigo_estado = 1
            return True
        self.codigo_estado = -1
        return False

    def arriesgar_una_letra(self, letra):
        """
        Evalúa la letra arriesgada y actualiza el estado de la partida.
        Retorna verdadero si la letra es correcta y falso si no lo es.
        """
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
