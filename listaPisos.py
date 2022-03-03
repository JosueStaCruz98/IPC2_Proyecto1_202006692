from NodoPiso import NodoPiso

class listaPisos:
    def __init__(self):
        self.cabeza = None

    def insertarPiso(self, Piso):
        if self.cabeza is None:
            self.cabeza = NodoPiso(Piso=Piso)
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = NodoPiso(Piso=Piso)

    def recorrer(self):
        actual = self.cabeza
        while actual != None:
            listaa=actual.Piso.getLista()
            print("Nombre:",actual.Piso.nombre)
            print("Filas:",actual.Piso.filas)
            print("Columnas:",actual.Piso.columnas)
            print("Precio volteo:",actual.Piso.volteo)
            print("Precio intercambio:",actual.Piso.intercambio)
            listaa.recorrer()
            print("===================================================")
            actual=actual.siguiente

    def buscarNombre(self, docu):
        actual = self.cabeza
        while actual != None:
            if actual.Piso.nombre == docu:     
                listaa=actual.Piso.getLista()
                listaa.recorrer()
                print("Nombre: ", actual.Piso.nombre)
                actual == None
                break
            actual=actual.siguiente
