from Nodos.NodoPiso import NodoPiso

class Pisos:
    def __init__(self):
        self.head = None

    def insertarPiso(self, Piso):
        if self.head is None:
            self.head = NodoPiso(Piso=Piso)
        else:
            actual = self.head
            while actual.next:
                actual = actual.next
            actual.next = NodoPiso(Piso=Piso)

    def recorrer(self):
        actual = self.head
        while actual != None:
            listaa=actual.Piso.getLista()
            print("Nombre:",actual.Piso.nombre)
            print("Filas:",actual.Piso.filas)
            print("Columnas:",actual.Piso.columnas)
            print("Precio volteo:",actual.Piso.volteo)
            print("Precio intercambio:",actual.Piso.intercambio)
            listaa.recorrer()
            print("===================================================")
            actual=actual.next

