class Usuario:
    def __init__(self, nombre, rol):
        self.nombre = nombre
        self.rol = rol
    def mostrar_info(self):
        print(f"usuario: {self.nombre} | rol: {self.rol}")
class Reporte:
    def __init__(self, titulo, contenido):
        self.titulo = titulo
        self.contenido = contenido
    def mostrar_reporte(self):
        print(f" {self.titulo}:\n{self.contenido}\n")
class Configuracion:
    def __init__(self):
        self.ajustes = {}
    def actualizar_ajuste(self, clave, valor):
        self.ajustes[clave] = valor
        print(f"ajuste '{clave}' actualizado a '{valor}'.\n")
    def mostrar_ajustes(self):
        if not self.ajustes:
            print("no hay ajustes configurados.\n")
        else:
            print("ajustes actuales:")
            for clave, valor in self.ajustes.items():
                print(f"- {clave}: {valor}")
            print()
def menu():
    usuarios = []
    reportes = []
    configuracion = Configuracion()
    while True:
        print("panel de control administrativo")
        print("1. registrar usuario")
        print("2. crear reporte")
        print("3. ver reportes")
        print("4. ajustes del sistema")
        print("5. salir")
        opcion = input("seleccione una opcion: ")
        if opcion == "1":
            nombre = input("nombre del usuario: ")
            rol = input("rol del usuario: ")
            usuario = Usuario(nombre, rol)
            usuarios.append(usuario)
            print(f"usuario {nombre} con rol {rol} registrado.\n")
        elif opcion == "2":
            titulo = input("titulo del reporte: ")
            contenido = input("contenido del reporte: ")
            reporte = Reporte(titulo, contenido)
            reportes.append(reporte)
            print(f"reporte '{titulo}' creado.\n")
        elif opcion == "3":
            if not reportes:
                print("no hay reportes disponibles.\n")
            else:
                for r in reportes:
                    r.mostrar_reporte()
        elif opcion == "4":
            print("ajustes del sistema")
            print("a. ver ajustes")
            print("b. actualizar ajuste")
            sub_opcion = input("seleccione una opcion: ")
            if sub_opcion.lower() == "a":
                configuracion.mostrar_ajustes()
            elif sub_opcion.lower() == "b":
                clave = input("nombre del ajuste: ")
                valor = input("valor del ajuste: ")
                configuracion.actualizar_ajuste(clave, valor)
            else:
                print("opcion invalida.\n")
        elif opcion == "5":
            print("saliendo del sistema...")
            break
        else:
            print("opcion invalida.\n")
menu()