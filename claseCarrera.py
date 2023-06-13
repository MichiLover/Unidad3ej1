class Carrera:
    __cod=''
    __nom=''
    __titulo=''
    __duracion=''

    def __init__(self,cod,nom,tit,dur):
        self.__cod=cod
        self.__nom=nom
        self.__titulo=tit
        self.__duracion=dur

    def getCod(self):
        return self.__cod

    def getNom(self):
        return self.__nom
    
    def getTitulo(self):
        return self.__titulo
    
    def getDuracion(self):
        return self.__duracion
