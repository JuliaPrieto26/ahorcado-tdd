import unittest
from ahorcado.ahorcado import Ahorcado

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
        ahorcado.login('juan')
        nombre = ahorcado.get_nombre()
        self.assertEqual(nombre, 'juan')


class TestArriesgarPalabra(unittest.TestCase):

    def test_arriesgar_palabra_invalida(self):
        ahorcado = Ahorcado()
        ahorcado.login('juan')
        ahorcado.set_palabra('agiles')
        self.assertFalse(ahorcado.arriesgar_una_palabra('noagil'))

    def test_arriesgar_palabra_valida(self):
        ahorcado = Ahorcado()
        ahorcado.login('juan')
        ahorcado.set_palabra('agiles')
        self.assertTrue(ahorcado.arriesgar_una_palabra('agiles'))

class TestArriesgarLetra(unittest.TestCase):

    def test_arriesgar_letra_valida(self):
        ahorcado = Ahorcado()
        ahorcado.login('juan')
        ahorcado.set_palabra('agiles')
        ahorcado.arriesgar_una_letra('i')
        self.assertEqual(ahorcado.get_aciertos_errores(), (1, 0))

    def test_arriesgar_letra_valida_repetida(self):
        ahorcado = Ahorcado()
        ahorcado.login('juan')
        ahorcado.set_palabra('casa')
        ahorcado.arriesgar_una_letra('a')
        self.assertEqual(ahorcado.get_aciertos_errores(), (2, 0))

    def test_arriesgar_letra_invalida(self):
        ahorcado = Ahorcado()
        ahorcado.login('juan')
        ahorcado.set_palabra('agiles')
        ahorcado.arriesgar_una_letra('n')
        self.assertEqual(ahorcado.get_aciertos_errores(), (0, 1))

    def test_partida_perdida(self):
        ahorcado = Ahorcado()
        ahorcado.login('juan')
        ahorcado.set_palabra('agiles')
        ahorcado.arriesgar_una_letra('n')
        ahorcado.arriesgar_una_letra('n')
        ahorcado.arriesgar_una_letra('n')
        ahorcado.arriesgar_una_letra('n')
        ahorcado.arriesgar_una_letra('n')
        ahorcado.arriesgar_una_letra('n')
        self.assertEqual(ahorcado.check_codigo_estado(), -1)

    def test_partida_ganada(self):
        ahorcado = Ahorcado()
        ahorcado.login('juan')
        ahorcado.set_palabra('agiles')
        ahorcado.arriesgar_una_letra('a')
        ahorcado.arriesgar_una_letra('g')
        ahorcado.arriesgar_una_letra('i')
        ahorcado.arriesgar_una_letra('l')
        ahorcado.arriesgar_una_letra('e')
        ahorcado.arriesgar_una_letra('s')
        self.assertEqual(ahorcado.check_codigo_estado(), 1)

    def test_estado_a_mitad_de_partida(self):
        ahorcado = Ahorcado()
        ahorcado.login('juan')
        ahorcado.set_palabra('maraton')
        ahorcado.arriesgar_una_letra('a')
        ahorcado.arriesgar_una_letra('g')
        self.assertEqual(ahorcado.get_estado(), '_ a _ a _ _ _')
        self.assertEqual(ahorcado.check_codigo_estado(), 0)

    def test_estado_a_final_de_partida(self):
        ahorcado = Ahorcado()
        ahorcado.login('juan')
        ahorcado.set_palabra('agiles')
        ahorcado.arriesgar_una_letra('a')
        ahorcado.arriesgar_una_letra('g')
        ahorcado.arriesgar_una_letra('i')
        ahorcado.arriesgar_una_letra('l')
        ahorcado.arriesgar_una_letra('e')
        ahorcado.arriesgar_una_letra('s')
        self.assertEqual(ahorcado.get_estado(), 'a g i l e s')
        self.assertEqual(ahorcado.check_codigo_estado(), 1)

    def test_registrar_letras_erroneas(self):
        ahorcado = Ahorcado()
        ahorcado.login('juan')
        ahorcado.set_palabra('agiles')
        ahorcado.arriesgar_una_letra('a')
        ahorcado.arriesgar_una_letra('n')
        ahorcado.arriesgar_una_letra('r')
        ahorcado.arriesgar_una_letra('p')
        self.assertEqual(ahorcado.get_letras_erroneas(), 'n r p')
        self.assertEqual(ahorcado.check_codigo_estado(), 0)

if __name__ == '__main__':
    unittest.main()
