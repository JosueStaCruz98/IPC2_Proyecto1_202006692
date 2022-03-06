from Nodos.NodoPatron import NodoPatron

class Patrones:
    def __init__(self):
        self.head = None

    def insertarPatron(self, Patron):
        if self.head is None:
            self.head = NodoPatron(Patron=Patron)
        else:
            actual = self.head
            while actual.next:
                actual = actual.next
            actual.next = NodoPatron(Patron=Patron)

    def recorrer(self):
        actual = self.head
        while actual != None:
            print("==========================================")
            listadelpatron = actual.Patron.getLista()
            print(actual.Patron.codigo)#obtengo el código 
            listadelpatron.recorrer()
            actual=actual.next
          
        

        
    