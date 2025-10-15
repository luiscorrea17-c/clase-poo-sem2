from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self) -> float:
        """Calcula el área de la figura."""
        pass

    @abstractmethod
    def perimeter(self) -> float:
        """Calcula el perímetro de la figura."""
        pass

class Rectangle(Shape):
    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height

    def area(self) -> float:
        return self.width * self.height

    def perimeter(self) -> float:
        return 2 * (self.width + self.height)

class Circle(Shape):
    def __init__(self, radius: float):
        self.radius = radius

    def area(self) -> float:
        import math
        return math.pi * self.radius ** 2

    def perimeter(self) -> float:
        import math
        return 2 * math.pi * self.radius

# No puedes hacer esto:
# s = Shape()  # TypeError: can't instantiate abstract class

r = Rectangle(3, 4)
print("Área rectángulo:", r.area())       # 12
print("Perímetro rectángulo:", r.perimeter())  # 14

c = Circle(5)
print("Área círculo:", c.area())
print("Perímetro círculo:", c.perimeter())

#POLIMORFISMO

class Animal:
    def hablar(self):
        pass

class Perro(Animal):
    def hablar(self):
        print("Guau!")

class Gato(Animal):
    def hablar(self):
        print("Miau!")

def haz_hablar(animal: Animal):
    # no importa si es Perro o Gato, llamamos al método hablar
    animal.hablar()

animales = [Perro(), Gato()]
for a in animales:
    haz_hablar(a)
    # imprimirá:
    # Guau!
    # Miau!