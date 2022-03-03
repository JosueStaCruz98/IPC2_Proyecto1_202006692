from NodoPatron import NodoPatron

class listaPatrones:
    def __init__(self):
        self.cabeza = None

    def insertarPatron(self, Patron):
        if self.cabeza is None:
            self.cabeza = NodoPatron(Patron=Patron)
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = NodoPatron(Patron=Patron)

    def recorrer(self):
        actual = self.cabeza
        while actual != None:
            print("==========================================")
            listadelpatron = actual.Patron.getLista()
            print(actual.Patron.codigo)#obtengo el código 
            listadelpatron.recorrer()
            actual=actual.siguiente

        
    