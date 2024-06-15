#!/usr/bin/python3
# 2024.01.13
# Execute: cd modules
# python3 -m unittest tests.unit.utils
# python3 -m unittest tests.unit.utils.TestScan.test010_validate

import unittest
# Ejecutar text en el orden en el que se escriben
# unittest.TestLoader.sortTestMethodsUsing = lambda *args: -1

from modules.utils import *


# Mostrar todos los colores y formato de letra
def show_all_color():
	for index, color in enumerate(PALETTE.keys()):
		lg_prt(color, f'Mensaje {index}, Color: {color}')


# Mostrar todos los formatos de fecha y tiempo
def show_all_dt():
	for index, format in enumerate(DATETIME_FORMAT.keys()):
		print(index, type(dt_format(format)), format, '\t\t\t\t', dt_format(format))


class TestScan(unittest.TestCase):

	# @unittest.skip('comments_for_skipping_unit_tests')
	def test000_showColors(self):
		lg_prt('v', '------------------------------------------')
		show_all_color()
		pass

	# @unittest.skip('comments_for_skipping_unit_tests')
	def test001_showColors(self):
		lg_prt('v', '------------------------------------------')
		lg_prt('ryc', 'rojo', 'amarillo', 'cian')
		lg_prt('nryc', 'rojo', 'amarillo', 'cian')
		lg_prt('uryc', 'rojo', 'amarillo', 'cian')
		lg_prt('b', 'solo un mensaje')
		lg_prt('ob', 'un mensaje', 'dos mensajes')
		lg_prt('orb', 'un mensaje', 'dos mensajes', 'tres mensajes')
		lg_prt('bor', 'más colores que mensajes')
		lg_prt('rnw', 'rojo', 'negrita', 'blanco')
		lg_prt('ruw', 'rojo', 'delineado', 'blanco')
		lg_prt('riw', 'rojo', 'cursiva', 'blanco')
		lg_prt('rkw', 'rojo', 'parpadeo', 'blanco')
		lg_prt('rtw', 'rojo', 'titulo', 'blanco')
		pass

	# @unittest.skip('comments_for_skipping_unit_tests')
	def test002_showColors(self):
		lg_prt('v', '------------------------------------------')
		lg_prt('yr', 'menos', ' colores', ' que mensajes', ' que mensajes', ' que mensajes')
		lg_prt('u', 'HEADER 1', 'HEADER 2', 'HEADER 3')
		lg_prt('z', 'Escribeme el color z')
		pass

	# @unittest.skip('comments_for_skipping_unit_tests')
	def test010_showDateTime(self):
		lg_prt('v', '------------------------------------------')
		show_all_dt()
		pass

	def test021_loggin(self):
		# Probar la creación de mensajes
		logger = Logging()
		print()
		logger.title('Esto es un título sin más')
		logger.title('Esto es un título', 'data', '+data')
		logger.info('Esto es un info', 'data', '+data')
		logger.object('Esto es la creación o borrado de un objeto', 'data', '+data')
		logger.warning('Esto es un warning', 'data', '+data')
		logger.error('Esto es un error', 'data', '+data')
		logger.success('Esto es una acción correcta', 'data', '+data')
		logger.critical('Esto es un error catastrofico', 'data', '+data')
		logger.hr()
		logger.debug('Debuguea esto', '{a:s, s:v}', '+data')
		logger.debug('Debuguea esto', {'a': 's', 's': 'v'}, None)
		pass

	# @unittest.skip('comments_for_skipping_unit_tests')
	def test021_log_file(self):
		# Probar la creación de archivos logs
		logger = Logging('logs/this_log.txt')
		logger.file('Algo paso')
		logger.file('ERROR', 'Era un error', 'oyokese')
		logger.file('WARNING', 'Era un error')
		pass

	# @unittest.skip('comments_for_skipping_unit_tests')
	def test030_cronos(self):
		# Probar las funciones de contar tiempo de ejecución
		with Chronos('showAllColor1'):
			show_all_color()

		@chronos
		def showAllColor2():
			for index, color in enumerate(PALETTE.keys()):
				lg_prt(color, f'Mensaje {index}, Color: {color}')

		showAllColor2()
		pass

	def test032_disable(self):
		# Deshabilitar el loggin
		logger = Logging()
		print()
		logger.title('Esto es un título sin más')
		logger.disable()
		logger.title('esto NO debe salir')
		logger.enable()
		logger.title('esto SI debe salir')


if __name__ == '__main__':
	unittest.main()
