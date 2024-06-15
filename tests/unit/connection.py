#!/usr/bin/python3
# 2024.01.15
# Execute: cd modules
# python3 -m unittest tests.unit.connection
# python3 -m unittest tests.unit.connection.TestCNT.test080_proxy

import unittest
# Ejecutar text en el orden en el que se escriben
# unittest.TestLoader.sortTestMethodsUsing = lambda *args: -1

from modules.connection import Handler_connection


oCNT = Handler_connection()
print('Init Cookies:', oCNT.get_cookies())


class TestCNT(unittest.TestCase):

	def test000_create(self):
		pass

	def test010_get(self):
		# Prueba GET
		# Error 500
		page, status = oCNT.send('GET', 'http://127.0.0.1:5000/')
		self.assertEqual(status, 404)
		# Obtener respuesta OK
		page, status = oCNT.send('GET', 'http://127.0.0.1:5000/simple_get')
		self.assertEqual(status, 200)
		self.assertEqual(page.text, 'Hello, World!')

	def test011_get_params(self):
		# Prueba GET con parametros
		page, status = oCNT.send('GET', 'http://127.0.0.1:5000/params_get?hola=mundo')
		self.assertEqual(status, 200)
		self.assertEqual(page.text, '{\n  "hola": "mundo"\n}\n')

	def test020_post(self):
		# Prueba POST
		# Error 405
		page, status = oCNT.send('GET', 'http://127.0.0.1:5000/simple_post')
		self.assertEqual(status, 405)
		self.assertIn('405 Method Not Allowed', page.text)
		# Obtener respuesta OK
		params = {'hola': 'mundo'}
		page, status = oCNT.send('POST', 'http://127.0.0.1:5000/simple_post', params)
		self.assertEqual(status, 200)
		self.assertIn('mundo', page.text)

	def test021_post_file(self):
		# Prueba send files POST
		# cwd = os.getcwd()  # Get the current working directory (cwd)
		# files = os.listdir(cwd)  # Get all the files in that directory
		# print("Files in %r: %s" % (cwd, files))
		f = open('tests/unit/extras/1.jpg', 'rb')
		files = {
			'add_picture': (None, '0', None),
			'qqfile': ('1.jpg', f.read(), 'image/jpeg')
		}
		f.close()

		page, status = oCNT.send('POST', 'http://127.0.0.1:5000/file_post', None, files=files)
		self.assertEqual(status, 200)
		self.assertIn('add_picture', page.text)
		# self.assertIn('405 Method Not Allowed', page.text)

	# @unittest.skip("Deshabilitar temporalmente para no mostrar prints")
	def test030_errors(self):
		# Probar los errores de send
		# Error metodo desconocido
		page, status = oCNT.send('GETAS', 'http://127.0.0.1:5000/simple_get')
		self.assertEqual(status, 999)
		self.assertIsNone(page, 'Esto debe ser None')
		# Web inaccesible
		page, status = oCNT.send('GETAS', 'http://127.0.0.1:5001/simple_get')
		self.assertEqual(status, 999)
		self.assertIsNone(page, 'Esto debe ser None')
		# Otros
		page, status = oCNT.send('GETAS', 'http://127.0.0.1:5000/simple_gets')
		self.assertEqual(status, 999)
		self.assertIsNone(page, 'Esto debe ser None')

	def test040_redirect(self):
		# Probar obtener url de una redirección
		url, status = oCNT.get_url_redirect('http://127.0.0.1:5000/simple_redirect')
		self.assertEqual(status, 302)
		self.assertEqual(url, '/simple_get')
		# Probar obtener url de una doble redirección
		url, status = oCNT.get_url_redirect('http://127.0.0.1:5000/double_get')
		self.assertEqual(status, 302)
		self.assertEqual(url, '/simple_get')
		# Probar un url sin redirección
		url, status = oCNT.get_url_redirect('http://127.0.0.1:5000/simple_get')
		self.assertIsNone(url, 'Esto debe ser None')
		self.assertIsNone(status, 'Esto debe ser None')

	def test040_encode(self):
		# Probar códificar una url
		url = oCNT.encode_url('http://127.0.0.1:5000/params_get?hola=mundo qué tal?')
		self.assertEqual(url, 'http://127.0.0.1:5000/params_get?hola=mundo%20qu%C3%A9%20tal?')

	def test050_headers(self):
		# Probar cabeceras de peticioón
		headers = oCNT.get_headers()
		self.assertIn('Mozilla', headers['User-Agent'])
		# Probar cambiar cabecera
		params = {'User-Agent': 'nuevo user-agent'}
		oCNT.set_headers(params)
		headers = oCNT.get_headers()
		self.assertEqual(headers['User-Agent'], 'nuevo user-agent')
		# Probar que se estan mandando la cabecera al servidor
		page, _ = oCNT.send('GET', 'http://127.0.0.1:5000/headers')
		self.assertIn('nuevo user-agent', page.text)

	def test060_cookies(self):
		# Probar las cookies
		cookies = oCNT.get_cookies()
		self.assertIsNotNone(cookies)
		self.assertIn('session', cookies)
		# Probar establecer cookie
		oCNT.set_cookies({'nombre': 'manolo'})
		cookies = oCNT.get_cookies()
		self.assertEqual(cookies['nombre'], 'manolo')
		# Probar que se mandandan las cookie al servidor
		page, status = oCNT.send('GET', 'http://127.0.0.1:5000/showcookie')
		self.assertEqual(status, 200)
		self.assertIn('manolo', page.text)

	def test061_save_cookies(self):
		# Comprobar número de cookies
		num = oCNT.num_cookies()
		self.assertEqual(num, 2)
		# Obtener el valor de una cookie
		value = oCNT.get_name_cookies('nombre')
		self.assertEqual(value, 'manolo')
		# Comprobar salvar cookies
		result = oCNT.save_cookies('tests/unit/')
		self.assertTrue(result)
		# Comprobar borrado de cookies
		oCNT.clear_cookies()
		num = oCNT.num_cookies()
		self.assertEqual(num, 0)
		# Comprobar cargar cookie
		result = oCNT.load_cookies('tests/unit/')
		value = oCNT.get_name_cookies('nombre')
		self.assertEqual(value, 'manolo')
		# Comprobar que se mandan al servidor despues de cargar
		page, status = oCNT.send('GET', 'http://127.0.0.1:5000/showcookie')
		self.assertEqual(status, 200)
		self.assertIn('manolo', page.text)

	# @unittest.skip('comments_for_skipping_unit_tests')
	def test070_is_online(self):
		result = oCNT.is_online()
		# self.assertFalse(result, 'Si no hay Internet')
		self.assertTrue(result, 'Si hay Internet')

	def test080_persistence(self):
		# Comprobar la persistencia de la sesión
		# Probar establecer cookie
		print(oCNT.get_cookies())
		cookies = oCNT.get_cookies()
		self.assertEqual(cookies['nombre'], 'manolo')


if __name__ == '__main__':
	unittest.main()
