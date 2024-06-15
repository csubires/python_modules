'''
	Version: 2024.01.15
	Autor: CJSM

	Script para configurar y usar un conjunto de proxies
	EN CASO DE QUEDARSE COLGADO PRESIONAR Ctrl+Shift+C PARA PASAR AL SIGUIENTE PROXY
'''

from .utils import Logging
from config.connection import URL_PROXY_CHECK


class Handler_proxy:
	'''
		Probar un listado de proxies y quedarte con el primero válido, de forma secuencial
		Para hacerlo de forma concurrecte ver Handler_proxy_thread
		Args:
			connection (obj):	Objeto manejador de timpo Handler_connection
			proxy_list (list): 	Listado de proxies
			url_base (str): 	URL base (Opcional)
			check_str (str): 	Cadena a buscar el el código fuente (Opcional)

		Use:
			oCNT = Handler_proxy(CONNECTION, PROXIES, URL_PROOF, CHECK_STR)
			oCNT.check_proxy()		# Solo si se requiere conectar mediante proxy
	'''

	def __init__(self, connection, proxy_list, url_base=None, check_str=None):
		self.logger = Logging('logs/connection.log')
		self.inetObj = connection
		self.proxy_list = proxy_list
		self.url_base = url_base
		self.check_str = check_str

		self.STOP = False
		self.proxyDict = {
			'http': 'http://127.0.0.1:80',
			'https': 'https://127.0.0.1:80',
			'ftp': 'ftp://127.0.0.1:80'
		}

	def stop(self):
		self.STOP = True
		self.logger.warning('Stop by Interrupt')

	def __str__(self):
		# Información de la conexión
		return f"Current connection: {type(self.inetObj)}, Proxy actual is: {self.proxyDict['https']}"

	def set_proxy(self):
		# Comprobar y extablecer un proxy válido
		self.logger.info('Searching valid proxy', f'URL: {self.url_base} within {self.check_str}', f'\nProxies: {self.proxy_list}')

		for proxy in self.proxy_list:
			if self.STOP:
				break

			chk_proxy = False
			self.logger.info('Setting proxy:', proxy)
			self.proxyDict['http'] = 'http://' + proxy
			self.proxyDict['https'] = 'https://' + proxy
			self.proxyDict['ftp'] = 'ftp://' + proxy
			self.inetObj.proxies = self.proxyDict

			try:
				self.logger.info('[1] Checking access to proxy', self.proxyDict['https'])
				page, status = self.send('GET', URL_PROXY_CHECK)		# Obtener la IP pública
				chk_proxy = (status == 200) and (page.text.strip() in self.proxyDict['https'])
				if chk_proxy: 	# Si coincide la IP del proxy establecido con lo devuelto por el server web check
					self.logger.success('Access proxy', f'Status: {status}, Return: {page.text.strip()}')
					if self.url_base is not None:
						self.logger.info('[2] Searching string', f'"{self.check_str}" in URL')
						page, status = self.send('GET', self.url_base)
						chk_proxy = self.check_str in page.text
						if chk_proxy:
							self.logger.success('String in Page', f'Status: {status}')
						else:
							self.logger.error('String not found.', f'In {self.url_base}, Status: {status}')

				else:
					self.logger.error('Access proxy', 'Status: {status}, Return: {page.text}')
				if chk_proxy:
					return True		# Yield Salir si ha encontrado un proxy válido
			except Exception as e:
				self.logger.error('Connection refused', f"Proxy: {self.proxyDict['https']}, State: {chk_proxy} \n", e)

		self.logger.warning('No proxy is valid')
		return False
