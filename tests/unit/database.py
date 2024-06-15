#!/usr/bin/python3
# 2024.01.20
# Execute: cd modules
# python3 -m unittest tests.unit.database
# python3 -m unittest tests.unit.database.TestCNT.test080_proxy

import unittest
# Ejecutar text en el orden en el que se escriben
# unittest.TestLoader.sortTestMethodsUsing = lambda *args: -1

from modules.database import Handler_SQL

TAG_QUERY = {
	'create_table': 'CREATE TABLE perro (id INTEGER PRIMARY KEY, nombre TEXT NOT NULL, edad INTEGER, alias TEXT UNIQUE)',
	'select_perro': 'SELECT id, nombre, edad, alias FROM perro',
	'insert_perro': 'INSERT INTO perro (nombre, edad, alias) VALUES (:nombre, :edad, :alias)',
	'update_perro': 'UPDATE perro SET nombre = :nombre, edad = :edad, alias = :alias WHERE id = :id',
	'select_unperro': 'SELECT id, nombre, edad, alias FROM perro WHERE id = :id',
	'delete_perro': 'DELETE FROM perro WHERE id = :id',
	'delete_maxive': 'DELETE FROM perro WHERE id = :id',
	'insert_maxive': 'INSERT OR REPLACE INTO perro (nombre, edad, alias) VALUES (:nombre, :edad, :alias)',
}

# Crear objeto
oDTBF = None
oDTB = Handler_SQL(':memory:', TAG_QUERY)
oDTB.execute('create_table')


class TestDTB(unittest.TestCase):

	def test000_create(self):
		# Comprobar error al crear la base de datos
		# oDTBF = Handler_SQL('algo/algo/as.db', TAG_QUERY)
		# self.assertIsNone(oDTBF.db, 'Debería ser None')
		# del oDTBF
		#  Crear base de datos
		# oDTB = Handler_SQL(':memory:', TAG_QUERY)
		self.assertIsNotNone(oDTB.db)
		# Crear la tabla
		# oDTB.execute('create_table')

	def test010_pre_select(self):
		# Probar tabla vacía
		rows = oDTB.execute('select_perro')
		self.assertIsNone(rows, 'Debería ser None')

	def test020_insert(self):
		# Prueba insertar
		params = {'nombre': 'toby', 'edad': 34, 'alias': 'tob'}
		rows = oDTB.execute('insert_perro', params)
		self.assertIsNone(rows, 'Debería ser None')
		self.assertEqual(oDTB.lastid(), 1)
		# Prueba select
		rows = oDTB.execute('select_perro')
		self.assertIsNotNone(rows, 'No debería ser None')
		self.assertEqual(len(rows), 1)
		self.assertEqual(rows[0][1], 'toby')

	def test030_update(self):
		# Prueba update
		params = {'id': '1', 'nombre': 'toby', 'edad': '999', 'alias': 'tobb'}
		rows = oDTB.execute('update_perro', params)
		self.assertIsNone(rows, 'Debería ser None')
		# Prueba select
		rows = oDTB.execute('select_perro')
		self.assertIsNotNone(rows, 'No debería ser None')
		self.assertEqual(len(rows), 1)
		self.assertEqual(rows[0][2], 999)
		self.assertEqual(rows[0][3], 'tobb')

	def test040_select_one(self):
		# Prueba select con params
		rows = oDTB.execute('select_unperro', {'id': '1'})
		self.assertIsNotNone(rows, 'No debería ser None')
		self.assertEqual(len(rows), 1)
		self.assertEqual(rows[0][2], 999)
		self.assertEqual(rows[0][3], 'tobb')
		# Selecionar un perro que no existe
		rows = oDTB.execute('select_unperro', {'id': 30})
		self.assertIsNone(rows, 'Debería ser None')

	def test050_delete_one(self):
		# Prueba borrar el único perro
		rows = oDTB.execute('delete_perro', {'id': 1})
		self.assertIsNone(rows, 'Debería ser None')
		self.assertEqual(oDTB.affected(), 1)
		# Prueba select
		rows = oDTB.execute('select_perro')
		self.assertIsNone(rows, 'Debería ser None')

	def test060_execute_many(self):
		# Prueba insertar maxivamente
		params = [
			('Minelva', 34, 'mine'),
			('Chucho', 67, 'chuk'),
			('Rex', 89, 'rek'),
		]
		rows = oDTB.execute_many('insert_maxive', params)
		self.assertIsNone(rows, 'Debería ser None')

		# Prueba select
		rows = oDTB.execute('select_perro')
		self.assertIsNotNone(rows, 'No debería ser None')
		self.assertEqual(len(rows), 3)
		self.assertEqual(rows[0][2], 34)
		self.assertEqual(rows[1][3], 'chuk')

	def test080_delete_maxive(self):
		# Borrar todas las filas de la tabla
		rows = oDTB.execute('select_perro')
		ids = [(i[0],) for i in rows]
		rows = oDTB.execute_many('delete_maxive', ids)
		self.assertIsNone(rows, 'Debería ser None')

		# Prueba select
		rows = oDTB.execute('select_perro')
		self.assertIsNone(rows, 'Debería ser None')


if __name__ == '__main__':
	unittest.main()
