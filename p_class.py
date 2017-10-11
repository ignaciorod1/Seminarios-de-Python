
 # PYTHON CLASS 10/10/2017
 #---------------------------------------------------------------------	 IMPORT -------------------------------------------------------------------
 

import time
from time import *
from math import pi
import RPi.GPIO as esparrago


 
 #---------------------------------------------------------------------		ENTRADA POR TECLADO ------------------------------------------
'''
print ("Cual es la respuesta a la vida, el universo y todo lo demas?")

anworte = input()

print(type(anworte))
print ("La respuesta es ", anworte)
'''
# OTRA FORMA MAS OPTIMA ES INTRODUCIR EL PRINT COMO ARGUMENTO DEL INPUT
'''
javiesunpesao = input("Cual es la respuesta a la vida, el universo y todo lo demas?\n")

print(javiesunpesao)
'''
# STRINGS
'''
name = input("Como se llama el perro de Hora de Aventuras?")

print ("El perro de Hora de Aventuras se llama", name)
'''
# CONVERSION DE TIPOS EN EL INPUT()
'''
cantidad_int = int(input("Insterte un numero no entero de lechuzas: "))	#	INT

print ("Han sido ejecutadas ", cantidad_int, 'lechuzas')

'''

#cantidad_float = int(input("Insterte un numero decimal de llaves allen "))	#	FLOAT MAL

#print ("Han sido perdidas ", cantidad_float, 'llaves allen')



#cantidad_float = float(input("Insterte un numero decimal de llaves allen "))	#	FLOAT BIEN

#print ("Han sido perdidas ", cantidad_float, 'llaves allen')


#----------------------------------------------------------------------	CLASES		-------------------------------------------------------------------------------
'''

class MyClass:
	"""Info"""

class Complex:
	"""Complex class"""
	def __init__(self, a,b):		# CONSTRUCTOR
		self.r = a						# VARIABLES DE LA CLASE 
		self.imag = b
		print("Clase construida")
		
	def show(self):
		print(self.r, '+ j', self.imag)
	
n = Complex(2, 5)			# HEMOS CREADO UN OBJETO INSTANCIA LLAMADO 'n'
p = Complex(2, 5)	
n.show()
print(n.__doc__)
'''
#	----*****---- SE PUEDEN CREAR VARIABLES PARA UN OBJETO INSTANCIA FUERA DE LA CLASE
'''
class Buch:

	def __init__(self, name):
		self.name = name
		
	def __init__(self, name, b):
		self.name = name
		self.pages = b
		
	def show(self):
		print('Mein buch ist ', self.name, 'und er hat', self.pages)

got = Buch('Game of Thrones', 54)		
got.show()

Buch.pages = 998			#  UTIL PARA HACER CONTADORES QUE RECORRAN LA CLASE . 
print(got.pages)

asdf = Buch('Emm', 9)		
asdf.show()
asdf.pages = 321
asdf.show()
'''
# Se definen en las clases los mEtodos con los atributos que se van a manejar y los atributos se declaran fuera de la clase
'''
class Buch:
	
	def __init__(self, name):
		self.name = name
		
	def __init__ (self): 			# SOBRECARGA DEL CONSTRUCTOR
		pass
		
	def show(self):
		print('Mein buch ist ', self.name, 'und er hat', self.pages, 'seiten')



hitchhickers = Buch()
hitchhickers.name = input('"Cual es el nombre del libro?"')
hitchhickers.pages = input("Wie viele seiten dein buch hat?")
hitchhickers.show()



hacklab_diaries = Buch()
hacklab_diaries.personajes = ['Javi Red' ,'Monty', 'Juako', 'Paula', 'Luispoiler', 'Ignatius', 'Elena', 'Bafian', 'Leo']
print (hacklab_diaries.personajes[2])


'''
#-----------------

#COSAS TOPE EXTREMAS

class Base:
	def __init__(self, name):
		self.name = name
		print("clase base construida")
		
class Derivada(Base):
	def __init__(self, name, n):
		self.num = n		
		print("clase derivada construida")
	def print(self):
		print(self.num)

x = Derivada("Jon Snow", 42)
print(x)

#Base.atr_nuevo = 23

#print(x.atr_nuevo)










