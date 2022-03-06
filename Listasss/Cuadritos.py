from Nodos.NodoCuadro import NodoCuadro

class Cuadritos:
    def __init__(self):
        self.head = None

    def insertarCuadrito(self, Cuadro):
        if self.head is None:
            self.head = NodoCuadro(Cuadro=Cuadro)
        else:
            actual = self.head
            while actual.next:
                actual = actual.next
            actual.next = NodoCuadro(Cuadro=Cuadro)

    def recorrer(self):
        actual = self.head
        while actual != None:
            print("Fila="+actual.Cuadro.x,"Columna="+actual.Cuadro.y,"Color -> "+actual.Cuadro.valor,"")
            actual=actual.next
        