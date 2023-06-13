from claseCarrera import Carrera
from claseFacultad import Facultad
from manejadorFacultades import Manejador
import csv

if __name__=="__main__":

    MF=Manejador()
    MF.cargar_facultades()
    MF.imprimir_facultades_carreras()
    menu=int(input("Elegir la opcion:\n 1-Ingresar codigo de facultad\n 2-Ingresar nombre de una carrera\n"))
    while menu!=0:
        if menu == 1:
            print("Actividad 1")
            # 1. Ingresar el código  de una facultad y mostrar nombre de la facultad, nombre  y duración de cada una de las carreras que se dictan en esa facultad.
            MF.ingresar_codigo()
        elif menu == 2:
            print("Actividad 2")
            # 2.  Dado el nombre de una carrera, mostrar código (se conforma con número de código de Facultad y código de carrera), nombre y localidad de la facultad donde esta se dicta.
            MF.mostrar_facultad_por_carrera()
        else:
            print("Opcion incorrecta, presione cero para finalizar")
        menu=int(input("Elegir la opcion:\n 1-Ingresar codigo de facultad\n 2-Ingresar nombre de una carrera\n"))