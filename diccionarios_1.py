# Diccionario: clave-valor 
# EJEMPLO calve = valor "juan esteban"

# Creamos la agenda con 3 contactos

"""agenda = {
    "Ana": "31222222",
    "Bruno": "315443242",
    "Carla":"393290329",
}


nombre = input("Ingrese el nombre de la persona: ")
# Mostrar el numero de un contacto especifico

if nombre in agenda:
    print("EL numero de telefono es: ", agenda[nombre])
else:
    print("No esta")
    contra = input("Ingrese la contraseña de esa persona" )
    agenda[nombre] = contra
print(agenda)"""

# Agregar nuevos contactos(valores)

"""agenda["luis"] = "1891256551"
"""

# Eliminar valores

"""del agenda["Ana"]"""

estudiantes = {
    "lucia": [4.5, 3.8, 4.2],
    "Mateo": [3.0, 3.5, 4.0, 4.2],
    "Sofia": [5.0, 4.,4.9],
}

promedio = {}
for nombre, notas in estudiantes.items():
    prom = sum(notas) / len(notas)
    print(f'Promedio de {nombre}: {prom: 2f}')
    promedio[nombre] = prom

print(promedio)

mejor_estudiante = max(promedio, key=promedio.get)
print(mejor_estudiante, promedio[mejor_estudiante])


# Ejercicio clase


while True:
    inventario = {
    "cuaderno": 15,
    "lapiz": 40,
    "borrador": 0,
    "marcador": 10,
    "regla": 5,
    }

    print("Bievenido a la tienda de utilies")
    print("Ingrese 1 para agregar un producto y cantidad")
    print("Ingrese 2 para comprar")
    print("ingrese 3 para ver el invetario actualizado")
    print("Ingrese 0 para salir")
    opcion = int(input())
    if opcion == 1:
        producto= input("Ingrese el nombre del producto: ")
        cantidad = input(int("ingrese la cantidad: "))
        if producto in inventario:
            inventario[producto]+=cantidad
        else:
            print("No esta")
            inventario[producto] = cantidad
    elif opcion  == 2:
        productos = input("Ingrese el nombre del producto: ")
        if productos in inventario:
            cantidades = input(int("ingrese la cantidad: "))
            if inventario[productos] >= cantidades:
                inventario[productos] -= cantidades
                print("Inventario actualizado")
            else:
                print("Cantidad insuficiente")
        else:
            print("No existe")
    elif opcion == 3:
        print(inventario)
    elif opcion == 0:
        print("Hasta pronto")
        break
    else:
        print("opcion incorrecta")

            
        