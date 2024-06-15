#!/usr/bin/python3
# 2024.01.20
# Execute: cd modules
# python3 -m unittest tests.unit.setting
# python3 -m unittest tests.unit.setting.TestCNT.test080_proxy

import unittest
import random, string
# Ejecutar text en el orden en el que se escriben
# unittest.TestLoader.sortTestMethodsUsing = lambda *args: -1

from modules.utils import lg_prt					# Mostrar y Colorear texto en consola
from modules.setting import Handler_setting			# Importar las configuraciones

VISITOR_INI_FILE = 'config/config.ini'
stt = Handler_setting(VISITOR_INI_FILE)


def randomword(length):
	letters = string.ascii_lowercase
	return ''.join(random.choice(letters) for i in range(length))


class TestScan(unittest.TestCase):

	def test000_create(self):
		pass

	def test001_load_and_show(self):
		# Cargar en objeto los attributos de INI
		stt.loadAllAttr()
		stt.showAttr()
		lg_prt('wy', 'Ejemplo insert', stt.URL_TARGET % 'insertado')
		lg_prt('ry', stt.parseObj.sections(), stt.__dict__.items())
		self.assertEqual(stt.URL_TARGET, 'https://www.mediavida.com/foro/feda/hilo-imagenes-increibles-432341/%s')
		self.assertEqual(stt.FOLDER_NAME, 'El hilo de las imágenes increíbles')
		self.assertEqual(stt.SOUP_CSS_CLASS, 'div.post-contents')
		self.assertEqual(stt.START_PAGE, 101)
		self.assertEqual(stt.END_PAGE, 101.2)
		self.assertFalse(stt.THIS_BOOL)
		self.assertTupleEqual(stt.NAMES, ('Aegnor', 'Aerandir'))
		self.assertIn('Aegnor', stt.NAMES)
		self.assertEqual(stt.ID_BLOCK, {12371441, 184432, 1405733})
		self.assertIn(1405733, stt.ID_BLOCK)
		self.assertEqual(stt.HEADERS['Host'], 'www.mediavida.com')
		self.assertIn('Connection', stt.HEADERS)

	def test001_save_and_show(self):
		# Salvar los atributos y comprobar que se ha guardado
		word = randomword(10)
		self.assertNotEqual(stt.PRUEBA, word)
		stt.PRUEBA = word
		stt.saveAllAttr()
		stt.loadAllAttr()
		self.assertEqual(stt.PRUEBA, word)


""" for section in stt.parseObj.sections():
	for key, value in stt.parseObj[section].items():
		print(key, value)
"""
