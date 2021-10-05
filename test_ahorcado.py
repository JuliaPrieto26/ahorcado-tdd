import unittest
from ahorcado import Ahorcado

class TestLoginMethods(unittest.TestCase):

    def test_login_vacio(self):
        ahorcado = Ahorcado()
        with self.assertRaises(Exception) as context:
            ahorcado.login('')
        self.assertTrue('El nombre no debe ser vacío' in str(context.exception))


    def test_login_mas_30(self):
        ahorcado = Ahorcado()
        with self.assertRaises(Exception) as context:
            ahorcado.login('aoeuuuuuuuuuuoooooooooooooooouuuuuuuuuuuuuoeuoeu')
        self.assertTrue('El nombre no debe debe tener mas de 30 caracteres' in str(context.exception))

    def test_login_caracteres_invalidos(self):
        ahorcado = Ahorcado()
        with self.assertRaises(Exception) as context:
            ahorcado.login('P3dr0')
        self.assertTrue('El nombre no debe tener caracteres invalidos' in str(context.exception))

    def test_login_valido(self):
        ahorcado = Ahorcado()
        ahorcado.login('Juan')
        nombre = ahorcado.get_nombre()
        self.assertEquals(nombre, 'Juan')


class TestArriesgarPalabra(unittest.TestCase):

    def test_arriesgar_palabra_invalida(self):
        ahorcado = Ahorcado()
        ahorcado.login('Juan')
        ahorcado.set_palabra('Agiles')
        self.assertFalse(ahorcado.arriesgar_una_palabra('NoAgil'))

    def test_arriesgar_palabra_valida(self):
        ahorcado = Ahorcado()
        ahorcado.login('Juan')
        ahorcado.set_palabra('Agiles')
        self.assertTrue(ahorcado.arriesgar_una_palabra('Agiles'))

if __name__ == '__main__':
    unittest.main()
