#!/usr/bin/python3
# 2024.01.22
# Execute: cd modules
# python3 -i tests.live_session

'''
	dir()		Returns the list of names in the current local scope when you call it with no argument.
				Attempts to return a list of valid attributes for the object passed as an argument.
	vars()		Returns the .__dict__ attribute for a module, class, instance, or any other object with this attribute.
				The .__dict__ attribute holds a list of names pertaining to the underlying object.
	locals()	Returns a dictionary representing the names in the current local scope.
	globals()	Returns the dictionary representing the current module namespace.
	type()		Returns the type of an object when you call it with one argument.

	from importlib import reload

	import importlib
	importlib.reload(greeting)
    <module 'greeting' from '.../greeting.py'>
'''

# EXAMPLE


