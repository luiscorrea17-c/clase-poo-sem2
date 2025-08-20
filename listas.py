#Crear Lista 

"""mi_lista = ["Primer Elemento", "Segundo elemento", "Tecer elemento"]
print(mi_lista[-1])""" #Para obtener el ultimo elemento de una lista

"""mi_lista = ["Primer Elemento", "Segundo elemento", "Tecer elemento"]
print(mi_lista[:])""" 

#Crear listas con ceros 

import random

lista_ceros = []

for i in range(0,10):
    lista_ceros.append(random.randint(1,100))
print(lista_ceros)
#Agregar numeros aleatorios del 1 al 100, randint es entre un rango de x numeros 
lista_random2 = [random.randint(1,100) for _ in range(10)]
print(lista_random2)

lista_ramdon3 = []
for n in range(0,10):
    lista_ramdon3.append(n)

print(lista_ramdon3)
#Cambiar el valor de un elemento por su indice
lista_ramdon3[2] = 1
lista_ramdon3[5] = 6

print(lista_ramdon3)
"""#Eliminar un elemento
lista_ramdon3.remove(1)

print(lista_ramdon3)

#Elimnar por su indice
del lista_ramdon3[2]
print(lista_ramdon3)"""

lista_ramdon3 = [elemento for elemento in lista_ramdon3 if elemento != 1]
print(lista_ramdon3)

lista_ramdon3.sort(reverse=True) # .sort ordena la lista de menor a mayor y con reverse=True lo ordena al contrario, osea de maor a menor
print(lista_ramdon3)

lista_ramdon3.reverse()
print(lista_ramdon3)

#Ejercicio de practica


class Personas:
    def __init__(self, nombre, ):
        self.nombre = nombre
        self.numero = [random.randint(100,999) for _ in range(5)]

lista_personas = []
while True:
    print("\nSeleccione una opción:")
    print("1. Inscribirte ")
    print("2. Conocer los numeros")    
    print("3. Salir")  

    opcion = int(input())

    if opcion == 1:
        print("Ingrese su nombre:")
        nombre = input()
    elif opcion == 2:
        print("Los numeros de",Personas.nombre)
        print("Son: ", Personas.numero)
    elif opcion == 3:
        print("gracias")
        break

