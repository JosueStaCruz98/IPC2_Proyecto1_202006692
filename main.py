#Variables Globales
global listaN
global listaPi
global lista_pa
global lista_c

from re import X
from xml.dom import minidom 
from xml.dom.minidom import parse
from listaCuadritos import listaCuadritos
from Cuadro import Cuadro
from Patron import Patron
from listaPatrones import listaPatrones
from Piso import Piso
from listaPisos import listaPisos
from tkinter import filedialog, Tk


#estructura de mi menu
def MenuPisos():
    while True:    
        print("|================MENÚ PRINCIPAL================|\n|  1. Mostrar patrón                           |\n|  2. Seleccionar Nuevo código                 |\n|  3. Salir.                                   |\n|==============================================|")
        print("Ingrese la opcion que desea")
        opcion = int(input())
        if opcion ==1:
            print("HOLAAAAA")
            #ImprimirLista(listaPi)
        elif opcion == 2:
            print("Seleccionar nuevo código")
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
            patron = input()
            print("Ingrese el código ")
            #lista_pa.buscarPatrones(doccc) La función no corre correctamente 
        else:
            False
            break
#Imprime por completo el contenido del archivo 
def ImprimirLista(lista):
    lista.recorrer()

#Función que permite cargar el archivo
def cargaarchivo():
    try:
        documentt = minidom.parse(str(input("Ingrese la ruta de su archivo:\n")))
        raiz= documentt.documentElement
        nombreFabrica = raiz.nodeName
        
        listaPi = listaPisos()
        
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

                lista_pa = listaPatrones()

                patrones = piso.getElementsByTagName("patron")
                pisoUno = Piso(nombrePiso,noFilas,noColumnas,precioVolteo,precioIntercambio)

                for patroncito in patrones:
                    if patroncito.hasAttribute("codigo"):
                        codigoPatron = patroncito.getAttribute("codigo")
                        patronColores = patroncito.childNodes[0].nodeValue.split("\n")[1]
                        x=1
                        y=1
                        z=0
                        lista_c=listaCuadritos()
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
        
while True:
    cargaarchivo()






