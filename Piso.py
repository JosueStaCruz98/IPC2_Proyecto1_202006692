from Listasss.Patrones import Patrones
class Piso:
    def __init__(self, nombre, filas, columnas, volteo, intercambio):
        self.nombre = nombre
        self.filas = filas
        self.columnas = columnas
        self.volteo = volteo
        self.intercambio = intercambio
        self.listaPatrones = Patrones

    def setLista(self, lista):
        self.listaPatrones = lista

    def getLista(self):
        return self.listaPatrones