class Estudiantes: 
    def __init__(self, nombre, edad, nota1, nota2,nota3):
        self.nombre = nombre 
        self.edad = edad 
        self.nota1 = nota1
        self.nota2 = nota2 
        self.nota3 = nota3
    
    def mostrar_datos(self):
        print("nombre: ", self.nombre)
        print("edad: ", self.edad)
        print("nota1: ", self.nota1)
        print("nota2: ", self.nota2)
        print("nota3: ", self.nota3)
    
    def calcular_promedio(self):
        promedio = (self.nota1 + self.nota2 + self.nota3)/3
        return promedio

print("ingrese el nombre del estudiante")
nombre = input()
print("ingrese la edad del estudiante")
edad = int(input())
print("ingrese la primera nota")
nota1 = float(input())
print("ingrese la segunda nota")
nota2 = float(input())
print("ingrese la tercera nota")
nota3 = float(input())
promedio_estudiante = Estudiantes(nombre, edad, nota1, nota2, nota3)



print("bienvenido al sistema de gestion de estudiantes")
lista_estudiantes = []
while True:
    print("seleccionar la opcion deseada")
    print("1. Agregar estudiante")
    print("2. Mostrar informacion de estudiantes")
    print("3. Mostrar promedio de estudiantes")
    print("0. Salir")
    opcion = int(input())
    if opcion == 1:
        print("Ingrese el nombre del estudiante")
        nombre = input()
        print("ingrese la edad del estudiante")
        edad = int(input())
        print("ingrese la primera nota")
        nota1 = float(input())
        print("ingrese la segunda nota")
        nota2 = float(input())
        print("ingrese la tercera nota")
        nota3 = float(input())
    elif opcion == 2:
        numero_estudiantes = len(lista_estudiantes)
        print("El numero de estudiantes es: ", numero_estudiantes)
        for estudiantes in lista_estudiantes: 
            print("El nombre del estudiante es ", estudiantes.nombre)
            print("El promedio del estudiante es ", estudiantes.calcular_promedio)
    elif opcion == 0:
        print("Salio exitosamente")
        break
    else:
        print("Opcion no valida")
        