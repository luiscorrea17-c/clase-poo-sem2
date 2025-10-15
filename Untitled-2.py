from dataclasses import dataclass, field
from typing import List, Optional

@dataclass
class Person:
    name: str
    age: int
    interests: List[str] = field(default_factory=list)

# Con dataclass se genera automáticamente:
# - __init__(self, name: str, age: int, interests: List[str] = [])
# - __repr__
# - __eq__

p1 = Person("Ana", 30, ["leer", "pintar"])
p2 = Person("Carlos", 25)

print(p1)  # Person(name='Ana', age=30, interests=['leer', 'pintar'])
print(p2)  # Person(name='Carlos', age=25, interests=[])

# Comparar por valores de los campos
p3 = Person("Ana", 30, ["leer", "pintar"])
print(p1 == p3)  # True

# HERENCIAS

class Animal:
    def __init__(self, especie: str, edad: int):
        self.especie = especie
        self.edad = edad

    def describeme(self):
        print("Soy un", type(self).__name__, "de especie", self.especie, "y edad", self.edad)

    def hablar(self):
        print("No sé qué decir...")

class Perro(Animal):
    def __init__(self, especie: str, edad: int, nombre: str):
        super().__init__(especie, edad)
        self.nombre = nombre

    def hablar(self):
        print("Guau! Me llamo", self.nombre)

class Gato(Animal):
    def hablar(self):
        print("Miau!")

# Uso
perro = Perro("canino", 5, "Rocky")
gato = Gato("felino", 3)

perro.describeme()  # Soy un Perro de especie canino y edad 5
perro.hablar()       # Guau! Me llamo Rocky

gato.describeme()    # Soy un Gato de especie felino y edad 3
gato.hablar()         # Miau!