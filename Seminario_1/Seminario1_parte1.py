# -*- coding: cp1252 -*-
#SEMINARIO 1 DE PYTHON (versión 3.6)
#Parte 1: Variables
#Contexto: Hacklab_UPM
#Fecha: jueves, 5 de octubre de 2017
#Impartido por: Javier Rojo Muñoz




#COMENTARIOS y miscelánea
#El intérprete de Python ignora todo lo que encuentre después del '#'
#al definir listas/tuplas/diccionarios las comas ',' permiten seguir en otra línea física.
#Se pueden concatenar varias líneas lógicas en una línea física:
x=2;print(x)


#############################################################################

#VARIABLES SIMILARES A OTROS LENGUAJES
x= True        #Un booleano
x= 1           #un número entero
x= 2.3         #un número decimal (float)
x= "casa"      #una cadena de caracteres (String)
x= 5+2j        #un número imaginario
x= complex(5,2)#otra manera de crear un número imaginario

#Python permite algunas sintaxis de asignación especiales:
x=y=4          #ahora x=4 e y=4
x,y=1,5        #ahora x=1 e y=5


#############################################################################

#ELIMINAR VARIABLES
#para eliminar una variable al completo usamos 'del'
del y          #ahora cualquier operación con y daría error.


#############################################################################

#LA FUNCIÓN PRINT() Y LAS CADENAS DE CARACTERES

#La función print() imprime (normalmente en la consola) el parámetro que pasemos.
#En Python 3 se vuelve obligatorio el uso de paréntesis.
print("hola mundo")
print(x)
print("Esta línea se imprimirá\
en una sola línea de consola.")
print("Detrás de esta línea no imprimirá un salto de línea",end="")
print("""Esto representa un párrafo
donde se respetarán los saltos,
espacios y "comillas" literales.""")

#Podemos concatenar cadenas con '+', y podemos unir distintos objetos con ','
print("Nueva "+"Zelanda")               #Nueva Zelanda
print("Tengo", 20, "años.")             #Tengo 20 años. Por defecto sustituye la coma por espacios
print("Soy", "un", "Robot", sep="-")    #Soy-un-robot

#Si intentamos concatenar una cadena y un número tendremos que
#transformar el número en un literal (cadena). Cuidado:
#No hay espacios en la concatenación. Es una unión literal.
print("Tengo "+str(20)+" años")


#ACCEDER A LOS ELEMENTOS DE UNA CADENA
#Estos métodos serán muy útiles ya que se repetirán en otras estructuras como las listas
mi_cadena = "Python es genial."
print(mi_cadena[0])   #P
print(mi_cadena[1])   #y

print(mi_cadena[:2])  #Py
#Significa "empieza a coger elementos hasta que llegues al segundo (índice 1).

print(mi_cadena[2:])  #thon es genial.
#Significa "ponte en el elemento de índice 2 (t) y recorre hasta el final.

print(mi_cadena[0:])  #Python es genial. Véase el ejemplo anterior.
#0 significa el inicio de la cadena

#NO se pueden asignar valores a elementos concretos de la cadena.
#mi_cadena[0]='a'

#Como ya hemos visto, se pueden concatenar cadenas.



#############################################################################

#TIPOS ESPECIALES DE VARIABLES
#Una vez hemos visto los tipos de variables más básicos podemos
#centrarnos en los más "especiales", curiosos o simplemente diferentes
#Es importante señalar que en todos estos tipos podemos incluir otros objetos
#de ese mismo tipo (por ejemplo, una lista de listas, una tupla con un diccionario, etc.)


#############################################################################

#LISTAS
#Una lista es un conjunto ORDENADO y MUTABLE de objetos.
#Es parecido en cierto sentido a un vector en C.
#Se indican con [] y tienen índices

mi_lista = [1, "hola", 3.14, 4-2j, [2,3,4], "último"]
print(mi_lista)        #imprime toda la lista
print(mi_lista[2])     #imprime 3.14
print(mi_lista[:3])    #imprime [1,"hola",3.14]
print(len(mi_lista))   #imprime 6 (el número de elementos)
#Los índices negativos se pueden usar para indicar valores empezando por el final
print(mi_lista[-2])    #imprime [2,3,4]
print(mi_lista[-3:])   #imprime [4-2j, [2,3,4], "último"]

#Para modificar valores:
mi_lista[0]= "primero"             #sustituye el elemento [0] por "primero"
mi_lista.append("nuevo elemento")  #añade un elemento al final.
print(mi_lista)


#############################################################################

#TUPLAS
#Las tuplas son conjuntos ORDENADOS, pero INMUTABLES
#Si intentamos dar un nuevo valor a una tupla ya creada obtenemos un error.
#Se representan con (), pero al llamar por el índice se hace exactamente igual que las listas
tupla_semanal = ("Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo")
print(tupla_semanal[2])  #imprime "Miércoles"


#############################################################################

#DICCIONARIOS
#Son conjuntos NO ORDENADOS y MUTABLES.
#Esto quiere decir que sólo nos importa "si el elemento existe en el diccionario".
#Al imprimir el conjunto entero no podemos saber en qué orden lo hará.
#Están formados por parejas de claves (keys) y valores (values)
#Sintaxis: {key1:value1, key2:value2, ...}
#Veremos en profundidad cómo iterar en diccionarios cuando veamos bucles

nivel_genialidad = {"C":9000,"Python":9001, "java":"¿Y ese quién es?", "otros":mi_lista}
otro_ejemplo ={"Pedro":"Picapiedra",
               "Homer":"Simpson",
               "Seilmour":"Skinner",
               "Armin":"Tanzanian"}

print(nivel_genialidad)          #imprime todo el diccionario con sus parejas
print(nivel_genialidad["Python"])#imprime 9001
print(nivel_genialidad.keys())   #imprime:  C, Python, java, otros
print(nivel_genialidad.values()) #imprime:  9000,9001,"¿Y ese quién es?", mi_lista(imprime toda la lista)

#Para modificar valores (si existen) o añadirlos automáticamente:
otro_ejemplo["Pedro"]="Almodóvar"
otro_ejemplo["Sentido de la vida"]=42
print(otro_ejemplo)

#un adelanto sobre booleanos:
#Si escribimos 'in' dicccionario buscará ese elemento entre las claves.

print("Homer" in otro_ejemplo)             #True. Por defecto busca entre las clavesprint("Homer" in otro_ejemplo.keys())      #True. Busca entre las claves
print("Simpson" in otro_ejemplo)           #False. Busca entre las claves por defecto
print("Simpson" in otro_ejemplo.values())  #True. Busca entre los valores de otro_ejemplo



