class Persona:
    def __init__(self, nombre, correo):
        self.__nombre = nombre
        self.__correo = correo

    def presentarse(self):
        return "Hola, soy " + self.__nombre + ", correo: " + self.__correo

    def get_nombre(self):
        return self.__nombre

    def get_correo(self):
        return self.__correo

class Empleado(Persona):
    def __init__(self, nombre, correo, salario):
        super().__init__(nombre, correo)
        self.__salario = float(salario)
        self._proyectos_asignados = []

    def get_salario(self):
        return self.__salario

    def calcular_bono(self):
        return 0.0

    def asignar_proyecto(self, proyecto):
        encontrado = False
        for p in self._proyectos_asignados:
            if p is proyecto:
                encontrado = True
                break
        if not encontrado:
            self._proyectos_asignados.append(proyecto)

    def listar_proyectos(self):
        lista = []
        for p in self._proyectos_asignados:
            lista.append(p)
        return lista

    def presentarse(self):
        base = super().presentarse()
        return base + " Soy empleado con salario " + format(self.__salario, ".2f")

class Desarrollador(Empleado):
    def __init__(self, nombre, correo, salario, lenguaje_principal):
        super().__init__(nombre, correo, salario)
        self.__lenguaje_principal = lenguaje_principal

    def presentarse(self):
        return super().presentarse() + " Desarrollador en " + self.__lenguaje_principal

    def calcular_bono(self):
        salario_base = self.get_salario()
        porcentaje_base = 0.10
        porcentaje_extra = 0.0
        for proyecto in self.listar_proyectos():
            if proyecto.cantidad_tareas() > 5:
                porcentaje_extra = porcentaje_extra + 0.01
        bono_calculado = salario_base * (porcentaje_base + porcentaje_extra)
        return bono_calculado

class Analista(Empleado):
    def __init__(self, nombre, correo, salario, nivel_experiencia):
        super().__init__(nombre, correo, salario)
        self.__nivel_experiencia = nivel_experiencia.lower()

    def presentarse(self):
        return super().presentarse() + " Analista nivel " + self.__nivel_experiencia

    def calcular_bono(self):
        salario_base = self.get_salario()
        porcentaje = 0.08
        if self.__nivel_experiencia == "senior":
            porcentaje = porcentaje + 0.03
        bono_calculado = salario_base * porcentaje
        return bono_calculado

class Gerente(Empleado):
    def __init__(self, nombre, correo, salario, departamento):
        super().__init__(nombre, correo, salario)
        self.__departamento = departamento
        self.__equipo_a_cargo = []

    def presentarse(self):
        return super().presentarse() + " Gerente del departamento " + self.__departamento

    def calcular_bono(self):
        bono_calculado = self.get_salario() * 0.12
        return bono_calculado

    def asignar_empleado_al_equipo(self, empleado):
        if empleado is self:
            print("Error: no puedes asignarte a ti mismo.")
            return
        ya = False
        for e in self.__equipo_a_cargo:
            if e is empleado:
                ya = True
                break
        if ya:
            print("Error: ese empleado ya está en tu equipo.")
            return
        self.__equipo_a_cargo.append(empleado)
        print("Empleado " + empleado.get_nombre() + " agregado al equipo.")

    def remover_empleado_del_equipo(self, empleado):
        encontrado = False
        for e in self.__equipo_a_cargo:
            if e is empleado:
                encontrado = True
                break
        if encontrado:
            self.__equipo_a_cargo.remove(empleado)
            print("Empleado " + empleado.get_nombre() + " removido del equipo.")
        else:
            print("Error: empleado no pertenece al equipo.")

    def listar_equipo(self):
        lista = []
        for e in self.__equipo_a_cargo:
            lista.append(e)
        return lista

class Tarea:
    _siguiente_id = 1

    def __init__(self, descripcion, horas_estimadas):
        if horas_estimadas < 0:
            print("Advertencia: horas negativas ajustadas a 0.")
            horas_estimadas = 0.0
        self._id_tarea = Tarea._siguiente_id
        Tarea._siguiente_id = Tarea._siguiente_id + 1
        self._descripcion = descripcion
        self._horas_estimadas = float(horas_estimadas)
        self._empleado_asignado = None
        self._estado = "pendiente"

    def asignar_empleado(self, empleado):
        self._empleado_asignado = empleado

    def diferir(self):
        self._estado = "diferida"

    def reactivar(self):
        self._estado = "pendiente"

    def get_id(self):
        return self._id_tarea

    def get_estado(self):
        return self._estado

    def get_asignado(self):
        return self._empleado_asignado

    def mostrar_tarea(self):
        asignado = "Sin asignar"
        if self._empleado_asignado != None:
            asignado = self._empleado_asignado.get_nombre()
        horas_str = format(self._horas_estimadas, ".2f")
        return ("Tarea id=" + format(self._id_tarea, "") + ", desc=" + self._descripcion +
                ", horas=" + horas_str + ", estado=" + self._estado +
                ", asignado=" + asignado)

class Proyecto:
    def __init__(self, nombre, presupuesto):
        self.__nombre = nombre
        self.__presupuesto = float(presupuesto)
        self.__lista_tareas = []

    def get_nombre(self):
        return self.__nombre
    
    def get_presupuesto(self):
        return self.__presupuesto
    def agregar_tarea(self, descripcion, horas_estimadas):
        tarea_nueva = Tarea(descripcion, horas_estimadas)
        self.__lista_tareas.append(tarea_nueva)
        print("Tarea " + format(tarea_nueva.obtener_id(), "") + " creada.")

    def asignar_tarea(self, id_tarea, empleado):
        tarea_obj = None
        for tarea in self.__lista_tareas:
            if tarea.obtener_id() == id_tarea:
                tarea_obj = tarea
                break
        if tarea_obj is None:
            print("Error: tarea no encontrada.")
        else:
            tarea_obj.asignar_empleado(empleado)
            empleado.asignar_proyecto(self)
            print("Tarea " + format(id_tarea, "") + " asignada a " + empleado.get_nombre() + ".")

    def diferir_tarea(self, id_tarea):
        for tarea in self.__lista_tareas:
            if tarea.obtener_id() == id_tarea:
                tarea.diferir()
                print("Tarea " + format(id_tarea, "") + " diferida.")
                return
        print("Error: tarea no encontrada para diferir.")

    def listar_tareas(self):
        lista = []
        for t in self.__lista_tareas:
            lista.append(t)
        return lista

    def cantidad_tareas(self):
        return len(self.__lista_tareas)

    def mostrar_proyecto(self):
        return ("Proyecto '" + self.__nombre + "', tareas = " +
                format(len(self.__lista_tareas), ""))

class Empresa:
    def __init__(self, nombre_empresa):
        self.__nombre_empresa = nombre_empresa
        self.__lista_empleados = []
        self.__lista_proyectos = []

    def agregar_empleado(self, empleado):
        ya = False
        for e in self.__lista_empleados:
            if e is empleado:
                ya = True
                break
        if not ya:
            self.__lista_empleados.append(empleado)
            print("Empleado " + empleado.get_nombre() + " agregado.")
        else:
            print("Ya existe ese empleado.")

    def crear_proyecto(self, nombre_proyecto, presupuesto):
        proyecto_nuevo = Proyecto(nombre_proyecto, presupuesto)
        self.__lista_proyectos.append(proyecto_nuevo)
        print("Proyecto '" + nombre_proyecto + "' creado.")
        return proyecto_nuevo

    def asignar_empleado_a_proyecto(self, proyecto, id_tarea, empleado):
        existe_proy = False
        for p in self.__lista_proyectos:
            if p is proyecto:
                existe_proy = True
                break
        existe_emp = False
        for e in self.__lista_empleados:
            if e is empleado:
                existe_emp = True
                break
        if not existe_proy:
            print("Error: proyecto no registrado en la empresa.")
        elif not existe_emp:
            print("Error: empleado no pertenece a la empresa.")
        else:
            proyecto.asignar_tarea(id_tarea, empleado)

    def listar_empleados(self):
        lista = []
        for e in self.__lista_empleados:
            lista.append(e)
        return lista

    def listar_proyectos(self):
        lista = []
        for p in self.__lista_proyectos:
            lista.append(p)
        return lista

    def mostrar_empresa(self):
        return ("Empresa " + self.__nombre_empresa + ", empleados = " +
                format(len(self.__lista_empleados), "") + ", proyectos = " +
                format(len(self.__lista_proyectos), ""))

def menu_interactivo():
    empresa = Empresa("MiEmpresa")
    while True:
        print("\n--- MENÚ PRINCIPAL ---")
        print("1. Crear empleado")
        print("2. Crear gerente")
        print("3. Crear proyecto")
        print("4. Crear tarea")
        print("5. Asignar tarea al empleado")
        print("6. Diferir tarea")
        print("7. Mostrar empleados y bonos")
        print("8. Mostrar proyectos y tareas")
        print("0. Salir")
        opcion = input(int("Opción: "))

        if opcion == 1:
            nombre = input("Nombre: ")
            correo = input("Correo: ")
            salario = float(input("Salario: "))
            tipo = input("Tipo (desarrollador / analista): ").strip().lower()
            if tipo == "desarrollador":
                lenguaje = input("Lenguaje principal: ")
                empleado = Desarrollador(nombre, correo, salario, lenguaje)
            else:
                nivel = input("Nivel experiencia: ")
                empleado = Analista(nombre, correo, salario, nivel)
            empresa.agregar_empleado(empleado)

        elif opcion == 2:
            nombre = input("Nombre gerente: ")
            correo = input("Correo: ")
            salario = float(input("Salario: "))
            departamento = input("Departamento: ")
            gerente = Gerente(nombre, correo, salario, departamento)
            empresa.agregar_empleado(gerente)

        elif opcion == 3:
            nombre_proj = input("Nombre proyecto: ")
            presupuesto = float(input("Presupuesto: "))
            empresa.crear_proyecto(nombre_proj, presupuesto)

        elif opcion == 4:
            proyectos = empresa.listar_proyectos()
            if len(proyectos) == 0:
                print("No hay proyectos.")
                continue
            for i in range(len(proyectos)):
                print(format(i+1, "") + ". " + proyectos[i].obtener_nombre())
            sel = int(input("Proyecto (número): ")) - 1
            if sel < 0 or sel >= len(proyectos):
                print("Selección inválida.")
                continue
            proyecto_seleccionado = proyectos[sel]
            descripcion = input("Descripción tarea: ")
            horas = float(input("Horas estimadas: "))
            proyecto_seleccionado.agregar_tarea(descripcion, horas)

        elif opcion == 5:
            proyectos = empresa.listar_proyectos()
            if len(proyectos) == 0:
                print("No hay proyectos.")
                continue
            for i in range(len(proyectos)):
                print(format(i+1, "") + ". " + proyectos[i].obtener_nombre())
            sel = int(input("Proyecto (número): ")) - 1
            if sel < 0 or sel >= len(proyectos):
                print("Selección inválida.")
                continue
            proyecto_sel = proyectos[sel]
            for tarea in proyecto_sel.listar_tareas():
                print(tarea.mostrar_tarea())
            id_tarea = int(input("Ingrese ID de la tarea: "))
            empleados = empresa.listar_empleados()
            for j in range(len(empleados)):
                print(format(j+1, "") + ". " + empleados[j].get_nombre())
            sel_emp = int(input("Empleado (número): ")) - 1
            if sel_emp < 0 or sel_emp >= len(empleados):
                print("Empleado inválido.")
                continue
            empleado_sel = empleados[sel_emp]
            empresa.asignar_empleado_a_proyecto(proyecto_sel, id_tarea, empleado_sel)

        elif opcion == 6:
            proyectos = empresa.listar_proyectos()
            if len(proyectos) == 0:
                print("No hay proyectos.")
                continue
            for i in range(len(proyectos)):
                print(format(i+1, "") + ". " + proyectos[i].obtener_nombre())
            sel = int(input("Proyecto (número): ")) - 1
            if sel < 0 or sel >= len(proyectos):
                print("Selección inválida.")
                continue
            proyecto_sel = proyectos[sel]
            for tarea in proyecto_sel.listar_tareas():
                print(tarea.mostrar_tarea())
            id_tarea = int(input("ID tarea a diferir: "))
            proyecto_sel.diferir_tarea(id_tarea)

        elif opcion == 7:
            empleados = empresa.listar_empleados()
            for emp in empleados:
                bono = emp.calcular_bono()
                print(emp.presentarse() + " — Bono: " + format(bono, ".2f"))
        elif opcion == 8:
            proyectos = empresa.listar_proyectos()
            for pr in proyectos:
                print(pr.mostrar_proyecto())
                for tarea in pr.listar_tareas():
                    print("   ", tarea.mostrar_tarea())
        elif opcion == 0:
            print("Saliendo.")
            break
        else:
            print("Opción inválida. Intenta otra vez.")