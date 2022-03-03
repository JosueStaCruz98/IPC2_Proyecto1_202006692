from NodoCuadro import NodoCuadro

class listaCuadritos:
    def __init__(self):
        self.cabeza = None

    def insertarCuadrito(self, Cuadro):
        if self.cabeza is None:
            self.cabeza = NodoCuadro(Cuadro=Cuadro)
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = NodoCuadro(Cuadro=Cuadro)

    def recorrer(self):
        actual = self.cabeza
        while actual != None:
            print(" fila="+actual.Cuadro.x,"columna="+actual.Cuadro.y,"color:"+actual.Cuadro.valor,"->")
            actual=actual.siguiente
        