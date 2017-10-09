
 # PYTHON CLASS 10/10/2017
 
 #---------------------------------------------------------------------		ENTRADA POR TECLADO ------------------------------------------

#print ("Cual es la respuesta a la vida, el universo y todo lo demas?")

#anworte = input()

#print ("La respuesta es ", anworte)

# OTRA FORMA MÁS ÓPTIMA ES INTRODUCIR EL PRINT COMO ARGUMENTO DEL INPUT

#input("Cual es la respuesta a la vida, el universo y todo lo demas?")


# STRINGS

#name = input("Como se llama el perro de Hora de Aventuras?")

#print ("El perro de Hora de Aventuras se llama", name)

# CONVERSION DE TIPOS EN EL INPUT()

#cantidad_int = int(input("Insterte un numero entero de lechuzas: "))	#	INT

#print ("Han sido ejecutadas ", cantidad_int, 'lechuzas')



#cantidad_float = int(input("Insterte un numero decimal de llaves allen "))	#	FLOAT MAL

#print ("Han sido perdidas ", cantidad_float, 'llaves allen')



#cantidad_float = float(input("Insterte un numero decimal de llaves allen "))	#	FLOAT BIEN

#print ("Han sido perdidas ", cantidad_float, 'llaves allen')


#----------------------------------------------------------------------	CLASES		-------------------------------------------------------------------------------


#class MyClass:
#		"""Info""""
#		<declaración>
"""
class Complex:
	def __init__(self, a,b):		# CONSTRUCTOR
		self.r = a						# VARIABLES DE LA CLASE 
		self.imag = b
		
	def show(self):
		print(self.r, '+ j', self.imag)
	
n = Complex(2, 5)			# HEMOS CREADO UN OBJETO INSTANCIA LLAMADO 'n'
n.show()
"""
#	----*****---- SE PUEDEN CREAR VARIABLES PARA UN OBJETO INSTANCIA FUERA DE LA CLASE
'''
class Buch:

	def __init__(self, name):
		self.name = name
		
	def show(self):
		print('Mein buch ist ', self.name, 'und er hat', pages, 'pages')

got = Buch('Game of Thrones')		
got.show()

got.pages = 998			#  ÚTIL PARA HACER CONTADORES QUE RECORRAN LA CLASE . 
print(got.pages)
'''

# Se definen en las clases los métodos con los atributos que se van a manejar y los atributos se declaran fuera de la clase
'''
class Buch:
	
	def __init__(self, name):
		self.name = name
		
	def __init__ (self): 			# SOBRECARGA DEL CONSTRUCTOR
		pass
		
	def show(self):
		print('Mein buch ist ', self.name, 'und er hat', self.pages, 'seiten')



hitchhickers = Buch()
hitchhickers.name = input()
hitchhickers.pages = input('Wie viele seiten dein buch hat?')
hitchhickers.show()



hacklab_diaries = Buch()
hacklab_diaries.personajes = ['Javi Red' ,'Monty', 'Juako', 'Paula', 'Luispoiler', 'Ignatius', 'Elena', 'Bafian', 'Leo']
print (hacklab_diaries.personajes[2])


'''











