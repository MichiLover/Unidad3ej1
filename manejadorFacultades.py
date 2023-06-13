import csv
from claseCarrera import Carrera
from claseFacultad import Facultad

class Manejador:
    def __init__(self):
        self.__facultades = []

    def cargar_facultades(self):
        archivo = open('facultades.csv')
        reader = csv.reader(archivo, delimiter=',')

        facultad_actual = None

        for linea in reader:
            if len(linea) == 5:
                facultad_actual = Facultad(int(linea[0]), linea[1], linea[2], linea[3], linea[4])
                self.__facultades.append(facultad_actual)
            elif len(linea) == 4 and facultad_actual is not None:
                unaCarrera = Carrera(linea[0], linea[1], linea[2], linea[3])
                facultad_actual.agregar_carrera(unaCarrera)

        archivo.close()


    def obtener_facultades(self):
        return self.__facultades

    #Este metodo es para ver que se hayan cargado los datos del archivo
    def imprimir_facultades_carreras(self):
        facultades = self.obtener_facultades()

        for facultad in facultades:
            print("Facultad:")
            print(f"Código: {facultad.getCodigo()}")
            print(f"Nombre: {facultad.getNombre()}")
            print(f"Dirección: {facultad.getDireccion()}")
            print(f"Localidad: {facultad.getLocalidad()}")
            print(f"Teléfono: {facultad.getTelefono()}")
            print("-------------------------------")
            carreras = facultad.getCarreras()
            for carrera in carreras:
                print("\tCarrera:")
                print(f"\tCódigo: {carrera.getCod()}")
                print(f"\tNombre: {carrera.getNom()}")
                print(f"\tTítulo: {carrera.getTitulo()}")
                print(f"\tDuración: {carrera.getDuracion()}")
                print("-------------------------------")
            print()

# 1. Ingresar el código  de una facultad y mostrar nombre de la facultad, nombre  y duración de cada una de las carreras que se dictan en esa facultad.
    def ingresar_codigo(self):
        codigo=int(input("Ingresar codigo de facultad: "))
        facultades=self.obtener_facultades()
        
        for facultad in facultades:
            if facultad.getCodigo() == codigo:
                print("Facultad")
                print("Nombre: {}".format(facultad.getNombre()))
                print("-------------------------------")
                print("Carreras: ")
                carreras=facultad.getCarreras()
                for carrera in carreras:
                    print("Nombre: {}".format(carrera.getNom()))
                    print("Duracion: {}".format(carrera.getDuracion()))
                    print("-------------------------------")

# 2.  Dado el nombre de una carrera, mostrar código (se conforma con número de código de Facultad y código de carrera), nombre y localidad de la facultad donde esta se dicta.

    def mostrar_facultad_por_carrera(self):
        nombre_carrera=input("Ingresar el nombre de una carrera: ")
        facultades = self.obtener_facultades()

        for facultad in facultades:
            carreras = facultad.getCarreras()

            for carrera in carreras:
                if carrera.getNom() == nombre_carrera:
                    codigo_facultad = facultad.getCodigo()
                    codigo_carrera = carrera.getCod()
                    nombre_facultad = facultad.getNombre()
                    localidad_facultad = facultad.getLocalidad()

                    print("Carrera:")
                    print(f"Nombre: {nombre_carrera}")
                    print("-------------------------------")
                    print("Facultad:")
                    print(f"Código: {codigo_facultad}-{codigo_carrera}")
                    print(f"Nombre: {nombre_facultad}")
                    print(f"Localidad: {localidad_facultad}")
                    print("-------------------------------")
                    