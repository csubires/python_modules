#!/usr/bin/python3
# 2024.01.15
# Execute: cd modules
# python3 -m unittest tests.unit.proxy
# python3 -m unittest tests.unit.proxy.TestCNT.test080_proxy

import unittest
# Ejecutar text en el orden en el que se escriben
# unittest.TestLoader.sortTestMethodsUsing = lambda *args: -1

from modules.connection import Handler_connection
from modules.proxy import Handler_proxy

URL_PROOF = 'https://api.ipify.org'
PROXIES = ['152.67.203.22:443', '191.7.8.199:80']

oCNT = Handler_connection()
oPRX = Handler_proxy(oCNT, PROXIES, 'https://www.filmaffinity.com', 'Filmaffinity')


class TestCNT(unittest.TestCase):

	def test000_create(self):
		pass

	# @unittest.skip("Si no hay Internet o proxies válidos no funcionará")
	def test080_proxy(self):
		#  Comprobar proxies
		result = oCNT.is_online()
		# self.assertFalse(result, 'Si no hay Internet')
		self.assertTrue(result, 'Si hay Internet')
		#  Como ya está creado el objeto para evitar @singleton
		result = oCNT.set_proxy()
		# print(oCNT.proxy_list)
		# print(oCNT.STOP)
		# print(oCNT)
		# print(oCNT.inetObj.proxies)
		print(oPRX)
		self.assertTrue(result, 'Proxy establecido')
		proxy = oCNT.inetObj.proxies['https']
		page, status = oCNT.send('GET', URL_PROOF)
		self.assertEqual(status, 200)
		self.assertIn(page.text, proxy, 'Encontrado el cambio de IP')


if __name__ == '__main__':
	unittest.main()
