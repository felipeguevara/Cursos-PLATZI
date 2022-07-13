def decorator_upper(func):                  # Función decoradora
	def wrapper(text):                      # Función anidada
		return func(text).upper()           # Operación que realiza el decorado a la función (func), inserta el texto a la función original. Convierte todo a mayúsculas.
	return wrapper                          # Devuelve wapper como indica la regla de los Clousures

@decorator_upper                            # Decora la función message
def message(name):
	return f'{name}, recibiste un mensaje'  # Esto es lo que realiza la función message, previo a ser decorada.

@decorator_upper                            # Decora la función warning
def warning(name):
	return f'Usa solo mayúsculas {name}'  # Esto es lo que realiza la función warning, previo a ser decorada.


if __name__ == "__main__":
    print(message("Cesar")) # Output: CESAR, RECIBISTE UN MENSAJE
    print(warning("Cesar")) # Output: USA SOLO MAYÚSCULAS CESAR

