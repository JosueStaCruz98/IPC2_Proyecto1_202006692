from Listasss.Cuadritos import Cuadritos
class Patron:
    def __init__(self, codigo):
        self.codigo = codigo
        self.listaCuadritos = Cuadritos
    
    def setLista(self, listaCuadritos):
        self.listaCuadritos = listaCuadritos

    def getLista(self):
        return self.listaCuadritos