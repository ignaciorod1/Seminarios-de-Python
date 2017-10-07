# -*- coding: cp1252 -*-
#SEMINARIO 1 DE PYTHON (versión 3.6)
#Parte 2: Bucles y funciones
#Contexto: Hacklab_UPM
#Fecha: jueves, 5 de octubre de 2017
#Impartido por: Javier Rojo Muñoz

#############################################################################

Bool_ej=True
Bool_ej2=False
lista_ej = ["elem1", "elem2", "elem3", "elem4"]


#############################################################################

#BOOLEANOS Y OPERACIONES LÓGICAS
#En Python3 usamos las palabras not, and, or para describir las operaciones booleanas
#las comparaciones son iguales a otros lenguajes de programación (<,>,<=,>=,==)
#Recordemos que == significa comparación y que = significa asignación
print(1<2 and 3==3)           #True. Ambas son verdaderas
print(1<2 and 4==3)           #False. No se cumple la condición 'and'
print(1<2 or 4==3)            #True. Una de las dos condiciones se cumple
print("elem1" not in lista_ej)#False. 'in lista_ej' devuelve True y NOT lo niega



#############################################################################

#La sintaxis de Python marca que aquello que pertenece a una categoría inferior
#(líneas dentro de un if, de un bucle, el contenido de una función) debe señalarse
#mediante indentación (recomendada 4 espacios). El inicio se marca con dos puntos
#y lo importante es ser coherente. Es decir, que aquello que esté indentado con
#8 espacios sea porque esté dos niveles por debajo del código principal. Ejemplo:


#VÁLIDO Y  RECOMENDADO
#if x==5:
#    print("x era igual a 5")
#else:
#    print("Vuelva a intentarlo")


#VÁLIDO PERO NO RECOMENDADO
#if x==5:
#  print("x era igual a 5")
#else:
#  print("Vuelva a intentarlo")


#NO VÁLIDO
#if x==5:
#    print("x era igual a 5")
#else:
#  print("Vuelva a intentarlo")


#############################################################################

#IF,ELIF,ELSE
#Si se cumple la condición del if python ejecutará las líneas que se encuentren dentro.
#Una vez acabado el if saltaría al final del else para continuar con el código.
#Si no se cumple la condición del if, Python evaluará la condición del primer elif.
#Python procederá de manera análoga al if con todos los 'elif' (diminutivo de
#'else if'. Finalmente, si no se ha cumplido ninguna condición ejecuta el interior
#de 'else'. No es necesario incluir elif ni else, pero suele ser conveniente
#para controlar qué sucede en caso de "error"


print("antes del if-elif-else")
if Bool_ej:
    print("El booleano de ejemplo era cierto")
elif Bool_ej2:
    print("El booleano 1 era falso, pero al menos el 2 es cierto")
else:
    print("Ninguno de los dos booleanos era cierto.")
print("después del if-elif-else")

#Puedes jugar con el valor de estos booleanos (al inicio del código) para ver
#qué resultado sale.
#Los 'else' tienen otros posibles usos que veremos con los bucles

#############################################################################

#RANGE()
#La función range() es muy útil para generar sucesiones de números.
#si solo incluimos un parámetro hará una sucesión desde cero hasta ese número.
#si incluimos dos números hará una sucesión del primero al segundo.
#un tercer parámetro indicaría el "salto". Es decir, que coja los valores de
#dos en dos o de tres en tres:
print(list(range(5)))          #0,1,2,3,4
print(list(range(3,10)))       #3,4,5,6,7,8,9
print(list(range(10,3)))       #inválido. No imprime nada. Habría que añadir como
                               #tercer factor un (-1)
print(list(range(2,20,2)))     #2,4,6,8,10,12,14,16,18
print(list(range(100,50,-10))) #100,90,80,70,60


#############################################################################

#BUCLES FOR Y RECORRER LISTAS

#Los bucles for los podemos usar de dos formas:
#O bien iteramos a lo largo de una lista/tupla/diccionario
#o bien iteramos a lo largo de un rango de números range() cuando sabemos el número de iteraciones.
#'continue' hace que pasemos a la siguiente iteración
#'break' hace que se acabe el bucle

for x in lista_ej:
    if x=="elem2":  #si topamos con elem2 "abortamos" la ITERACIÓN. Break saldría del BUCLE
        continue
    print(x,end="-")

#En el for, la variable x se crea al iniciar el bucle (o podría estar ya creada de antes)
#Podriamos haberla llamado como quisieramos (p.ej.:for elem in lista_ej:)
#Para cada iteración del bucle, adquiere el valor del siguiente elemento de la lista.
#Dentro del bucle se puede usar ahora esta variable para hacer operaciones (como imprimirlo por pantalla)

print("")
for x in range(10):
    print(x,end=".")


#si incluimos un else después entra sólo si ha salido del bucle normalmente (no por un break)
#Prueba a cambiar la condición del if para que sea True o False y mira el resultado
print("")
for x in range(5):
    if x==6:
        break
    print(x,end="_")
else:
    print("dentro del else. Todo ha ido bien")
print("detrás del for")



#############################################################################

#BUCLES WHILE
#usamos while cuando no sabemos el número de iteraciones, sino que queremos
#realizar la acción hasta que se cumpla una condición.
#por ejemplo, hasta que el número de dni introducido sea mayor que 0
#Un else se ejecuta si se sale normalmente al comprobar que la condición es falsa
#Un else no se ejecutará si se sale con un break
#Pueden surgir fácilmente bucles infinitos si, por ejemplo, el booleano siempre es True
while Bool_ej2:
    print("dentro del while")
else:
    print("La condición era falsa. Todo controlado")



#############################################################################

#FUNCIONES SIMPLES
#Las funciones las definimos con 'def nombre(posibles_parámetros):'
#Como el intérprete salta de línea en línea necesitamos definir la función
#antes de utilizarla. Las funciones pueden devolver objetos mediante return.
#Todo lo que quede detrás del return se ignorará, ya que volveremos al código principal.
def saludar():
    print("hola")

saludar()  #llamará a la función y se empezarán a ejecutar las líneas dentro de ésta

def imprimir(mensaje):
    print(mensaje)

imprimir("llamada a función con parámetro")

#Podemos dar valores por defecto a los parámetros con ciertas condiciones:
#1:Los valores por defecto deben ir al final
#2:En la llamada a la función todo parámetro sin valor por defecto debe ser explícito
#3:Podemos redefinir parámetros o bien por el orden o bien por el nombre:

def sumayresta(A,B=0,C=0):
    #por defecto b y c valen cero, pero siempre hay que pasar un valor de a
    return A+B-C

print(sumayresta(1))         #1+0-0=1. Es obligatorio dar valor a A, ya que no tiene valor default
print(sumayresta(1,3))       #1+3-0=4. Se lo asignamos al primer parámetro sin valor default
print(sumayresta(1,3,2))     #1+3-2=2. Sustituimos todos los valores por defecto
print(sumayresta(1,C=2,B=3)) #1+3-2=2. Si lo indicamos con el nombre no necesitamos el orden



#############################################################################

#PASS
#La palabra clave 'pass' no hace nada. Se utiliza mientras se programa cuando
#sintácticamente necesitas rellenar un hueco, pero no quieres que haga nada:

def megafuncion():
    #ya escribiré después el código
    pass


