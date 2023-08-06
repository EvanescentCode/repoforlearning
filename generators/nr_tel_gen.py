import random


class NumerTelefonu():
	"""
	Funkcja numer telefonu zwraca randomowy numer pomiędzy 500000000,a 800000000.
	"""
	def numer_telefonu(self):
		random_number = random.randint(500000000, 800000000)
		return str(random_number)
