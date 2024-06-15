'''
	Version: 2024.01.20
	Autor: CJSM

	Este script contiene una clase para manejar modelos de un objeto
'''

from dataclasses import dataclass

from .utils import Logging, singleton						# Mostrar y Colorear texto en consola


@singleton
@dataclass
class Film:
	# Modelo para una película
	_film_id: int
	_name: str
	_fps: float
	_external: bool
	logger = Logging('logs/models.log')

	def __post_init__(self):
		# Que se inicie con una limpieza
		# self.clear()
		pass

	def validate(self):
		# Validar que cada propiedad sea del tipo adecuado o None
		result = True
		# lg_prt('r', self.__dict__)
		# lg_prt('g', self.__dict__.items())
		# lg_prt('g', self.__dict__.keys())
		# lg_prt('r', self.__annotations__)
		# lg_prt('g', self.__annotations__.items())
		for name, field_type in self.__annotations__.items():
			provided_key = self.__dict__.get(name, None)
			# Permitir atributos None, y (si no es None y no coinciden los tipos)
			if provided_key is not None and not isinstance(provided_key, field_type):
				self.logger.error(f'The field "{name}" is of type', type(provided_key), 'was expected', field_type)
				result = False
		return result

	def exchange(self):
		# Intentar convertir todas las propiedades a sus tipos adecuados
		result = True
		for name, field_type in self.__annotations__.items():
			provided_key = self.__dict__.get(name, None)
			# Permitir atributos None, y (si no es None y no coinciden los tipos)
			if provided_key is not None and not isinstance(provided_key, field_type):
				try:
					if 'str' in str(field_type):
						setattr(self, name, str(provided_key))

					elif 'int' in str(field_type):
						setattr(self, name, int(provided_key))

					elif 'float' in str(field_type):
						setattr(self, name, float(provided_key))

					elif 'bool' in str(field_type):
						setattr(self, name, bool(provided_key))
				except Exception as e:
					self.logger.error(f'Can not change the field "{name}" is of type', type(provided_key), 'to', field_type, e)
					result = False
		return result

	def trim(self):
		# Elimina espacios en blanco en los atributos de tipo string
		for key, value in self.__dict__.items():
			if isinstance(value, str):
				setattr(self, key, value.strip())

	def clear(self):
		# Resetear todas las propiedades
		for key in self.__annotations__.keys():
			setattr(self, key, None)

	def json(self):
		# Crear un diccionario con las propiedades de la clase
		result = {}
		for key, value in self.__dict__.items():
			result.update({f'{key[1:]}': value})
		return result

	def prepare(self):
		# Preparar la información del dataclass para ser utilizada
		self.exchange()				# Intentar forzar la validación
		if self.validate():			# Si es validado
			self.trim()				# Hacer trim
			return self.json()		# Devolver el diccionario de datos
		else:
			return None

	def show_attr(self):
		# Mostrar los atributos de la clase
		self.logger.debug('Attr of film', self.__dict__.keys(), self.__dict__.values())

	# -------------------- GETTERS & SETTERS ---------------------

	@property
	def film_id(self) -> int:
		return self._film_id

	@film_id.setter
	def film_id(self, value: int):
		self._film_id = value

	@property
	def name(self) -> str:
		return self._name

	@name.setter
	def name(self, value: str):
		self._name = value

	@property
	def fps(self) -> float:
		return self._fps

	@fps.setter
	def fps(self, value: float):
		self._fps = value

	@property
	def external(self) -> bool:
		return self._external

	@external.setter
	def external(self, value: bool):
		self._external = value
