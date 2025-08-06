#Ejercicio 2


class Producto:
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    def mostrar_datos(self):
        print("Nombre del producto:", self.nombre)
        print("Precio:", self.precio)
        print("Cantidad disponible:", self.cantidad)

    def vender(self, cantidad_vendida):
        if cantidad_vendida <= self.cantidad:
            self.cantidad -= cantidad_vendida
            print(f"Se vendieron {cantidad_vendida} unidades de {self.nombre}.")
        else:
            print(f"No hay suficientes unidades de {self.nombre}. Solo hay {self.cantidad} disponibles.")
lista_productos = []

print("Bienvenido al sistema de gestión de productos")
while True:
    print("\nSeleccione una opción:")
    print("1. Agregar producto")
    print("2. Mostrar información de productos")
    print("3. Vender producto")
    print("0. Salir")

    opcion = int(input())

    if opcion == 1:
        print("Ingrese el nombre del producto:")
        nombre = input()
        print("Ingrese el precio del producto:")
        precio = float(input())
        print("Ingrese la cantidad disponible:")
        cantidad = int(input())
        producto = Producto(nombre, precio, cantidad)
        lista_productos.append(producto)

    elif opcion == 2:
        if len(lista_productos) == 0:
            print("No hay productos registrados.")
        else:
            for producto in lista_productos:
                producto.mostrar_datos()

    elif opcion == 3:
        if len(lista_productos) == 0:
            print("No hay productos para vender.")
        else:
            print("Ingrese el nombre del producto a vender:")
            nombre_producto = input()
            encontrado = False
            for producto in lista_productos:
                if producto.nombre == nombre_producto:
                    encontrado = True
                    print("Ingrese la cantidad a vender:")
                    cantidad_vender = int(input())
                    producto.vender(cantidad_vender)
                    break
        if encontrado == False:
            print("Producto no encontrado.")
    elif opcion == 0:
        print("Gracias por usar el sistema.")
        break

    else:
        print("Opción no válida.")

#Ejercicio 3