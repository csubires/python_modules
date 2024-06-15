#!/usr/bin/python3
# 2024.01.20
# Execute: cd modules
# python3 -m unittest tests.unit.extras
# python3 -m unittest tests.unit.extras.TestCNT.test080_proxy

import unittest
# Ejecutar text en el orden en el que se escriben
# unittest.TestLoader.sortTestMethodsUsing = lambda *args: -1

from modules.extras import *


class TestScan(unittest.TestCase):

	def test000_create(self):
		pass

	def test010_timestamp_to_datetime(self):
		pass

	def test011_timestamp_to_date(self):
		result = timestamp_to_date(1651855905)
		self.assertEqual(result, '2022-05-06')

	def test012_date_to_human(self):
		result = date_to_human('2020-10-23 21:34:23')
		self.assertEqual(result, '23 de October de 2020')

	def test013_time_to_seconds(self):
		result = time_to_seconds('02:05:12')
		self.assertEqual(result, 7512)

	def test014_seconds_to_time(self):
		result = seconds_to_time(7512)
		self.assertEqual(result, '2hr, 5min, 12seg')
		result = seconds_to_time(696)
		self.assertEqual(result, '11min, 36seg')

	def test015_bytes_to_human(self):
		result = bytes_to_human(14272717)
		self.assertEqual(result, '13.61 MB')

	def test070_listToDict(self):
		# Prueba respuesta de select a diccionario
		headers = ['id', 'nombre', 'edad', 'alias']
		response = (
			[23, 'Pepe', 45, 'pepito'],
			[253, 'Marie', 34, 'mari'],
			[55, 'Giyer', 23, 'gie']
		)
		response = list_to_dict(headers, response)
		self.assertEqual(len(response), 3)

		# Prueba respuesta de select a diccionario (MAL)
		headers = ['id', 'nombre', 'edad', 'alias', 'NOO']
		response = ((),)
		response = list_to_dict(headers, response)
		self.assertIsNone(response)

		# Prueba respuesta de select a diccionario (Sólo una fila)
		headers = ['id', 'nombre', 'edad', 'alias']
		response = (
			[23, 'Pepe', 45, 'pepito'],
		)
		response = list_to_dict(headers, response)
		self.assertEqual(len(response), 1)

	# ---- Pruebas


if __name__ == '__main__':
	unittest.main()
