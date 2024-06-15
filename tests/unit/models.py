#!/usr/bin/python3
# 2024.01.20
# Execute: cd modules
# python3 -m unittest tests.unit.models
# python3 -m unittest tests.unit.models.TestCNT.test080_proxy

import unittest
# Ejecutar text en el orden en el que se escriben
# unittest.TestLoader.sortTestMethodsUsing = lambda *args: -1

from modules.models import Film


oneFilm = Film(1, 'Start war', 45.3, False)


class TestModels(unittest.TestCase):

	def test000_create(self):
		# Crear de distintas formas
		self.assertEqual(1, oneFilm.film_id)
		self.assertEqual('Start war', oneFilm.name)
		self.assertEqual(45.3, oneFilm.fps)
		self.assertFalse(oneFilm.external)
		# Crear mediante setter
		oneFilm.film_id = 2
		oneFilm.name = 'Jonh Wich'
		oneFilm.fps = 66.66
		oneFilm.external = True
		self.assertEqual(2, oneFilm.film_id)
		self.assertEqual('Jonh Wich', oneFilm.name)
		self.assertEqual(66.66, oneFilm.fps)
		self.assertTrue(oneFilm.external)
		oneFilm.showAttr()

	def test010_validate(self):
		# Validar que los datos sean del tipo adecuado
		result = oneFilm.validate()
		self.assertTrue(result)
		# Datos no válidos
		oneFilm.film_id = '2'
		oneFilm.name = 66.7
		oneFilm.fps = True
		oneFilm.external = 45
		result = oneFilm.validate()
		self.assertFalse(result)

	def test020_clear(self):
		# Limpiar los atributos (SI SE PERMITEN VALORES NONE)
		oneFilm.clear()
		self.assertIsNone(oneFilm.film_id, 'Esto debe ser None')
		self.assertIsNone(oneFilm.name, 'Esto debe ser None')
		self.assertIsNone(oneFilm.fps, 'Esto debe ser None')
		self.assertIsNone(oneFilm.external, 'Esto debe ser None')
		# Comprobar que no es valido
		result = oneFilm.validate()
		self.assertTrue(result)		# SE PERMITEN ATRIBUTOS None
		result = oneFilm.json()
		self.assertEqual(result, {'film_id': None, 'name': None, 'fps': None, 'external': None})

	def test030_json(self):
		# Crear un diccionario con las propiedades de la clase
		oneFilm.film_id = 2
		oneFilm.name = 'Jonh Wich'
		oneFilm.fps = 66.66
		oneFilm.external = True
		result = oneFilm.json()
		self.assertEqual(result, {'film_id': 2, 'name': 'Jonh Wich', 'fps': 66.66, 'external': True})

	def test040_exchange(self):
		# Probar a cambiar el tipo de dato si no es el correcto
		oneFilm.film_id = 2.66
		oneFilm.name = 56745
		oneFilm.fps = 66
		oneFilm.external = 'Blancanieves'
		result = oneFilm.exchange()
		self.assertTrue(result)
		self.assertEqual(2, oneFilm.film_id)
		self.assertEqual('56745', oneFilm.name)
		self.assertEqual(66.0, oneFilm.fps)
		self.assertTrue(oneFilm.external)
		# Imposible de convertir
		oneFilm.film_id = 'algo'
		oneFilm.name = None
		oneFilm.fps = 'algo'
		oneFilm.external = self
		result = oneFilm.exchange()
		self.assertFalse(result)

	def test050_trim(self):
		# Prueba trim
		oneFilm.name = '   hola'
		oneFilm.trim()
		self.assertEqual('hola', oneFilm.name)
		# Con tabulador
		oneFilm.name = '	hola'
		oneFilm.trim()
		self.assertEqual('hola', oneFilm.name)
		# Prueba trim
		oneFilm.name = 'hola    '
		oneFilm.trim()
		self.assertEqual('hola', oneFilm.name)
		# Con tabulador
		oneFilm.name = 'hola   '
		oneFilm.trim()
		self.assertEqual('hola', oneFilm.name)
		# Espacio central
		oneFilm.name = 'ho la'
		oneFilm.trim()
		self.assertNotEqual('hola', oneFilm.name)

	def test060_prepare(self):
		# Preparar la información del dataclass para ser utiliza
		oneFilm._film_id = 2.0
		oneFilm.film_id = 2.0
		oneFilm.name = '    Jonh Wich  '
		oneFilm.fps = 66
		oneFilm.external = 45745
		result = oneFilm.validate()
		self.assertFalse(result)
		result = oneFilm.prepare()
		self.assertEqual(result, {'film_id': 2, 'name': 'Jonh Wich', 'fps': 66.0, 'external': True})
		# Probar la no positibilidad de preparar la información
		oneFilm.film_id = 'hola'
		oneFilm.name = (34)
		oneFilm.fps = (None)
		oneFilm.external = (45745)
		result = oneFilm.prepare()
		self.assertIsNone(result)


if __name__ == '__main__':
	unittest.main()
