#Variables Globales
global listaN
global listaPi
global lista_pa
global lista_pa2
global lista_c
global lista_c2
global d

from re import X
from xml.dom import minidom 
from xml.dom.minidom import parse
from Listasss.Cuadritos import Cuadritos
from Cuadro import Cuadro
from Patron import Patron
from Listasss.Patrones import Patrones
from Piso import Piso
from Listasss.Pisos import Pisos
from tkinter import filedialog, Tk
from graphviz import Digraph
from Lista import Lista

lista = Lista()


#Se abre cuando ya haya seleccionado un nombre y codigo
def MenuPisos(listaaa):
    while True:    
        print("|================MENÚ PRINCIPAL================|\n|  1. Mostrar patrón                           |\n|  2. Seleccionar Nuevo código                 |\n|  3. Salir.                                   |\n|==============================================|")
        print("Ingrese la opcion que desea")
        opcion = int(input())
        if opcion ==1:
            print(cadenaColores)
            guardarPatron(cadenaColores, noFilas, noColumnas)
            lista.graficarLista(4,8)
            #ImprimirLista(listaPi)
        elif opcion == 2:
            print("Seleccionar nuevo código")
        else:
            #listaPisos.clear()
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
        nombreFabrica = raiz.nodeName
        
        listaPi = Pisos()
        
        todosLosPisos = raiz.getElementsByTagName("piso")
        for piso in todosLosPisos:
            if piso.hasAttribute("nombre"):
                nombrePiso = piso.getAttribute("nombre")

                filaTotal = piso.getElementsByTagName("R")[0]
                noFilas = filaTotal.childNodes[0].data

                columnaTotal = piso.getElementsByTagName("C")[0]
                noColumnas = columnaTotal.childNodes[0].data

                volteosTotales = piso.getElementsByTagName("F")[0]
                precioVolteo = volteosTotales.childNodes[0].data

                intercambiosTotales = piso.getElementsByTagName("S")[0]
                precioIntercambio = intercambiosTotales.childNodes[0].data

                lista_pa = Patrones()

                patrones = piso.getElementsByTagName("patron")
                pisoUno = Piso(nombrePiso,noFilas,noColumnas,precioVolteo,precioIntercambio)

                for patroncito in patrones:
                    if patroncito.hasAttribute("codigo"):
                        codigoPatron = patroncito.getAttribute("codigo")
                        patronColores = patroncito.childNodes[0].nodeValue.split("\n")[1]
                        x=1
                        y=1
                        z=0
                        lista_c=Cuadritos()
                        for fila in range(int(noFilas)):
                            for columna in range(int(noColumnas)):                               
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
            print("letra: "+letra+" fila: "+row+" columna: "+col)
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

                filaTotal = piso.getElementsByTagName("R")[0]
                global noFilas
                noFilas = int(filaTotal.childNodes[0].data)

                columnaTotal = piso.getElementsByTagName("C")[0]
                global noColumnas
                noColumnas = int(columnaTotal.childNodes[0].data)

                volteosTotales = piso.getElementsByTagName("F")[0]
                precioVolteo = volteosTotales.childNodes[0].data

                intercambiosTotales = piso.getElementsByTagName("S")[0]
                precioIntercambio = intercambiosTotales.childNodes[0].data
            else:
                continue

            lista_pa2 = Patrones()

            patrones = piso.getElementsByTagName("patron")
            pisito = Piso(nombrePiso,noFilas,noColumnas,precioVolteo,precioIntercambio)

            for patroncito in patrones:
                if patroncito.hasAttribute("codigo"):
                    if codito == patroncito.getAttribute("codigo"):
                        #print("Lo encontró")
                        codigoPatron = patroncito.getAttribute("codigo")
                        patronColores = patroncito.childNodes[0].nodeValue.split("\n")[1]
                        global cadenaColores
                        cadenaColores = str(patronColores)
                        
                        x=1
                        y=1
                        z=0
                        lista_c2=Cuadritos()
                        for fila in range(int(noFilas)):
                            for columna in range(int(noColumnas)):                               
                                cuadritoUno=Cuadro(str(x),str(y),patronColores[z])
                                lista_c2.insertarCuadrito(cuadritoUno)
                                y=y+1
                                z=z+1
                            y=1
                            x=x+1
                        patronUno = Patron(codigoPatron)
                        patronUno.setLista(lista_c2)
                        lista_pa2.insertarPatron(patronUno)
                        listax=patronUno.getLista()
                        #Quiebre
                    else:
                        continue
            pisito.setLista(lista_pa2)
            listaSelec.insertarPiso(pisito)
            ImprimirLista(listaSelec)
            MenuPisos(listaSelec)#Ya seleccionado el nombre y codigo se redirige que se quiere hacer

while True:
    cargaarchivo()






