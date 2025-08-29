class Profesor:
    def __init__(self, nombre, edad, experiencia):
        self.nombre = nombre
        self.edad = edad
        self.experiencia = experiencia

class Estudiante:
    def __init__(self, nombre, nota, edad):
        self.nombre = nombre
        self.edad = edad
        self.nota = nota

class asignatura:
    def __init__(self, nombre, horario, codigo, profesor):
        self.nombre = nombre
        self.horario = horario
        self.profesor = profesor
        self.estudiantes = []
        self.codigo = codigo
    def Agregar_estdiante(self, estudiante):
        self.estudiantes.append(estudiante)
        print("Estudiante agregado correctamente")

    def Promedio(self):
        acumulador = 0
        for estudiante in self.estudiantes:
            acumulador = acumulador + estudiante.nota
        promedio = acumulador/len(self.estudiantes)
        return promedio
    def Mostrar_estudiantes(self):
        for estudiante in self.estudiantes:
            print(estudiante.nombre)



                





profesor = Profesor("Juan Esteban", 35, 5)
poo = asignatura("Programacion Orientada a Objetos", "M-V- 10- 12", 62, profesor)
estudiante_1 = Estudiante("Luis correa", 5, 17)
estudiante_2 = Estudiante("Alejandro correa", 2.5, 18)
estudiante_3 = Estudiante("Tomas correa", 4, 21)

poo.Agregar_estdiante(estudiante_1)

poo.Agregar_estdiante(estudiante_2)

poo.Agregar_estdiante(estudiante_3)

print(poo.Promedio())

poo.Mostrar_estudiantes()