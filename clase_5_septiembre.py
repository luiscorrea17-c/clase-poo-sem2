class Personas:
    def __init__(self, nombre, cedula, ti):
        self.nombre = nombre
        self.__cedula = cedula
        self.__ti = ti

    def obtener_cedula(self):
        if self.__cedula is not None:
            return self.__cedula
        else:
            return self.__ti

persona1 = Personas("juan", 1111, None)
persona2 = Personas("maria", 2222, None)



print("El nombre de la primera persona es: ", persona1.nombre)

print("La cedula de la primera persona es: ", persona1.obtener_cedula())

print("El nombre de la segunda persona es: ", persona2.nombre)

print("La cedula de la segunda persona es: ", persona2.obtener_cedula())


