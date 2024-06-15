'''
	Version: 2024.01.20
	Autor: CJSM

	Este script contiene una clase para manejar archivos de configuración INI
'''

import configparser 				# Para extraer la configuración de los archivos INI

from .utils import Logging, singleton


@singleton
class Handler_setting:
	"""	Carga los valores de parametros de registro en una estructura
		Args:
			ini_file (str): 	Ruta del archivo "*.ini" Ex: 'config/%s/prueba.ini'
		Use:
			stt = Handler_setting(ini_file)
			stt.loadAllAttr()
			stt.saveAllAttr()
			stt.showAttr()
	"""

	def __init__(self, ini_file):
		self.ini_file = ini_file
		self.parseObj = configparser.ConfigParser()
		self.parseObj.read(self.ini_file)
		self.logger = Logging('logs/setting.log')
		self.logger.object('File loaded', self.ini_file)

	def __str__(self):
		return self.parseObj.items()

	def load_attr(self):
		# Convertir el diccionario parse en atributos de clase
		for section in self.parseObj.sections():
			for key, value in self.parseObj[section].items():
				# print(key, value)
				try:
					# Todos los elementos son cargados como atributos de clase
					setattr(self, key.upper(), eval(value))
				except Exception:
					setattr(self, key.upper(), value)
		self.logger.object('All attr of "*.ini" loaded')

	def save_attr(self):
		# Salvar los atributos de clase en un archivo ini
		for section in self.parseObj.sections():
			for key, value in self.__dict__.items():
				if key in self.parseObj[section]:
					value = str(value)
					value = value.replace('%', '%%')
					self.parseObj[section][key.lower()] = value

		with open(self.ini_file, 'w') as f:
			self.parseObj.write(f)
		self.logger.object('All attr saved in', self.ini_file)

	def show_attr(self):
		# Mostrar los atributos de la clase
		self.logger.debug('Attr of *.ini', self.__dict__.keys(), self.__dict__.values())
