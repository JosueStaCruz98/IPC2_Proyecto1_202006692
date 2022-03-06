from re import X
from xml.dom import minidom 
from xml.dom.minidom import parse
from graphviz import Digraph
from Lista import Lista

from Listasss.Cuadritos import Cuadritos
from Listasss.Patrones import Patrones
from Listasss.Pisos import Pisos

from Piso import Piso
from Cuadro import Cuadro
from Patron import Patron

lista = Lista()

#Se abre cuando ya haya seleccionado un nombre y codigo
def MenuPisos(listaaa):
    while True:    
        print("|================MENÚ PRINCIPAL================|\n|  1. Mostrar patrón                           |\n|  2. Seleccionar Nuevo código                 |\n|  3. Salir.                                   |\n|==============================================|")
        print("Ingrese la opcion que desea")
        opcion = int(input())
        if opcion ==1:
            print(cadenaColores)#Se imprime la cadena de colores
            guardarPatron(cadenaColores, noFilas, noColumnas)
            lista.graficarLista(noColumnas,noFilas*noColumnas)
        elif opcion == 2:
            print("Seleccionar nuevo código")
            print("Esta opción aún no se encuentra disponible")
        else:
            False
            break

#Este menú se abre al momento de seleccionar la ruta del archivo
def MenuPrincipal():
    while True:    
        print("|================MENÚ PRINCIPAL================|\n|  1. Seleccionar Patrón y Código              |\n|  2. Salir.                                   |\n|==============================================|")
        print("Ingrese la opcion que desea")
        opcion = int(input())
        if opcion ==1:
            #ImprimirLista(listaPi)
            print("Ingrese el nombre del Patrón: ")
            nom = input()
            print("ingrese el código")
            cod = input()
            buscarImprimir(nom, cod)
        else:
            False
            break
#Imprime por completo el contenido del archivo 
def ImprimirLista(lista1):
    lista1.recorrer()

#Función que permite cargar el archivo
def cargaarchivo():
    try:
        global documentt
        documentt = minidom.parse(str(input("Ingrese la ruta de su archivo:\n")))
        global raiz
        raiz= documentt.documentElement
        
        listaPi = Pisos()
        
        todosLosPisos = raiz.getElementsByTagName("piso")
        for piso in todosLosPisos:
            if piso.hasAttribute("nombre"):
                nombrePiso = piso.getAttribute("nombre")

                FilaTotal = piso.getElementsByTagName("R")[0]
                noF = FilaTotal.childNodes[0].data

                ColumnaTotal = piso.getElementsByTagName("C")[0]
                noC = ColumnaTotal.childNodes[0].data

                VolteosTotales = piso.getElementsByTagName("F")[0]
                precioV = VolteosTotales.childNodes[0].data

                IntercambiosTotales = piso.getElementsByTagName("S")[0]
                precioI = IntercambiosTotales.childNodes[0].data

                lista_pa = Patrones()

                patrones = piso.getElementsByTagName("patron")
                pisoUno = Piso(nombrePiso,noF,noC,precioV,precioI)

                for patroncito in patrones:
                    if patroncito.hasAttribute("codigo"):
                        codigoPatron = patroncito.getAttribute("codigo")
                        patronColores = patroncito.childNodes[0].nodeValue.split("\n")[1]
                        x=1
                        y=1
                        z=0
                        lista_c=Cuadritos()
                        for fila in range(int(noF)):
                            for columna in range(int(noC)):                               
                                cuadritoUno=Cuadro(str(x),str(y),patronColores[z])
                                lista_c.insertarCuadrito(cuadritoUno)
                                y=y+1
                                z=z+1
                            y=1
                            x=x+1
                        patronUno = Patron(codigoPatron)
                        patronUno.setLista(lista_c)
                        lista_pa.insertarPatron(patronUno)
                        listax=patronUno.getLista()
                pisoUno.setLista(lista_pa)
                listaPi.insertarPiso(pisoUno)
        MenuPrincipal()#Ya cargado el archivo se activa el menú
    except:
        print("Por favor verifique que haya ingresado una ruta adecuada a su proyecto")
       
#Función que permite que se guarde el patron del código
def guardarPatron(patron, filas, columnas):
    #recorremos la cadena del string guardandolo en la lista
    for i in range(0, filas):
        for j in range(0, columnas):
            letra = patron[(i*columnas)+j]
            row = str(i)
            col = str(j)
            lista.añadirNodo(letra, row, col)

#Busca el nombre y el código y luego imprime el contenido de él
def buscarImprimir(noPiso, codito):
    global listaSelec 
    listaSelec = Pisos()
    raiz= documentt.documentElement    
    todosPisos2 = raiz.getElementsByTagName("piso")
    for piso in todosPisos2:
        if piso.hasAttribute("nombre"):
            if noPiso == piso.getAttribute("nombre"):
                #print("el nombre es:")
                nombrePiso = piso.getAttribute("nombre")

                fTotal = piso.getElementsByTagName("R")[0]
                global noFilas
                noFilas = int(fTotal.childNodes[0].data)

                cTotal = piso.getElementsByTagName("C")[0]
                global noColumnas
                noColumnas = int(cTotal.childNodes[0].data)

                vTotales = piso.getElementsByTagName("F")[0]
                precioVolteo = vTotales.childNodes[0].data

                iTotales = piso.getElementsByTagName("S")[0]
                precioIntercambio = iTotales.childNodes[0].data
            else:
                continue

            lista_pa2 = Patrones()

            patrones = piso.getElementsByTagName("patron")
            pisito = Piso(nombrePiso,noFilas,noColumnas,precioVolteo,precioIntercambio)

            for patroncito in patrones:
                if patroncito.hasAttribute("codigo"):
                    if codito == patroncito.getAttribute("codigo"):
                        #print("Lo encontró")
                        cPatron = patroncito.getAttribute("codigo")
                        patronColores = patroncito.childNodes[0].nodeValue.split("\n")[1]
                        global cadenaColores
                        cadenaColores = str(patronColores)                       
                        x=1
                        y=1
                        z=0
                        lista_c2=Cuadritos()
                        for fila in range(int(noFilas)):
                            for columna in range(int(noColumnas)):                               
                                cuadritoDos=Cuadro(str(x),str(y),patronColores[z])
                                lista_c2.insertarCuadrito(cuadritoDos)
                                y=y+1
                                z=z+1
                            y=1
                            x=x+1
                        patronDos = Patron(cPatron)
                        patronDos.setLista(lista_c2)
                        lista_pa2.insertarPatron(patronDos)
                        #Quiebre
                    else:
                        continue
            pisito.setLista(lista_pa2)
            listaSelec.insertarPiso(pisito)
            ImprimirLista(listaSelec)#Impresión de la lista seleccionada por el usuario
            MenuPisos(listaSelec)#Ya seleccionado el nombre y codigo se redirige que se quiere hacer

while True:
    cargaarchivo()






