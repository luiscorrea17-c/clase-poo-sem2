class Estudiante:
    def __init__(self, nombre, promedio):
        self.nombre = nombre 
        self.promedio = promedio

    def aprobo(self):
        return self.promedio >= 3.0

class Curso:
    def __init__(self, nombre_arcivo):
        self.nombre_archivo = nombre_arcivo
        self.estudiantes = []
    
    def agregar_estudiante(self, estudiante):
        self.estudiantes.append(estudiante)
        print("Estudiante agregado exitosamente")
        with open(self.nombre_archivo, "a") as f:
            f.write(f"{estudiante.nombre}, {estudiante.promedio}")
    
    def guardar_es_archivo(self):
        try:
            with open(self.nombre_archivo, "w") as f:
                for e in self.estudiantes:
                    f.write(f"{e.nombre}, {e.promedio}\n")
            print("Estudiante guardado exitosamente")

        except:
            print("Hubo un error al guardar los estudiantes")


    def mostrar_estudiante(self):
        for e in self.estudiantes:
            print(f"{e.nombre} tiene un promedio de {e.promedio}")
    
    def cargar_desde_archivo(self):
        self.estudiantes = []
        try:
            with open(self.nombre_archivo, "r") as f:
                for linea in f:
                    nombre, promedio = linea.strip().split(",")
                    estudiante = Estudiante(nombre, promedio)
                    self.estudiantes.append(estudiante)
        
        except:
            print("hubo un error cargando los estudiantes")



poo = Curso("esudiantes.txt")
estudiante3 = Estudiante("Pablo", 2.6)
poo.agregar_estudiante(estudiante3)
poo.mostrar_estudiante()
poo.cargar_desde_archivo()
