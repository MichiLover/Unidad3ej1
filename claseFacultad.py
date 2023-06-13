from claseCarrera import Carrera
import csv
class Facultad:
    __codigo=''
    __nombre=''
    __direccion=''
    __localidad=''
    __telefono=''
    __carreras=[]

    def __init__(self,cod,nom,dire,loc,tel):
        self.__codigo=cod
        self.__nombre=nom
        self.__direccion=dire
        self.__localidad=loc
        self.__telefono=tel
        self.__carreras=[]

    def agregar_carrera(self, carrera):
        self.__carreras.append(carrera)

    def getCodigo(self):
        return self.__codigo

    def getNombre(self):
        return self.__nombre
    
    def getDireccion(self):
        return self.__direccion
    
    def getLocalidad(self):
        return self.__localidad

    def getTelefono(self):
        return self.__telefono

    def getCarreras(self):
        return self.__carreras