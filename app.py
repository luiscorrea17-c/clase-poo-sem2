class perro:
    def __init__(self,nombre,raza):

        self.nombre=nombre
        self.raza=raza
def ladrar(self):
    print("el perro que esta ladrando es",self.nombre)

class moto:
    def __init__(self,cilindraje,marca):
        self.cilindraje=cilindraje
        self.marca=marca

class celular:
    def __init__(self,tamaño,procesador):
        self.tamaño=tamaño
        self.procesador=procesador
hola= input("ingrese el nombre del perro")
hola2= input("ingrese la raza del perro")

miperrito= perro(hola,hola2)
print(f'el nombre del perro es {miperrito.nombre} y su raza es {miperrito.raza}')

h= input("ingrese el cilindraje")
h2= input("ingrese la marca")

h2
mimoto= moto(h,h2)
print(f'el cilindeje es {mimoto.cilindraje} de marca {mimoto.marca}')

print("ahora los perros van a ladrar")
perro.ladrar()