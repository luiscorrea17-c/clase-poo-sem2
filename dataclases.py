from dataclasses import dataclass, field, asdict
import operaciones

@dataclass(frozen=True)
class Personas:
    nombre: str
    edad: int = field(default=35)

    def retornar_edad_por_2(self) -> int:
        return self.edad * 2 
@dataclass
class Puesto:
    nombre = str
    persona: Personas


class Personas2:
    def __init__(self, nombre, edad=35):
        self.nombre = nombre
        self.edad = edad

persona1 = Personas("Juan", 36)
persona2 = Personas("Juan")

puesto1 = Puesto("Desarrolador", persona1)

print(puesto1)

operaciones.suma()

print(asdict(persona1))

if persona1 == persona2:
    print("Son iguales")
else:
    ("No son iguales")
