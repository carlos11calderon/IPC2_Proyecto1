#import
from tkinter import filedialog, Tk
from typing import List
from _elementtree import *
from ListaSimple import *
from NodoSimple import *
import xml.etree.cElementTree as ET


 
def Menu():
    print("==============MENU==============")
    print("1. Cargar Archivo")
    print("2. Procesar Archivo")
    print("3. Escribir Archivo de salida")
    print("4. Mostrar datos del Estudiante")
    print("5. Generar Grafica")
    print("6. Salida")
    opcion = int(input("Ingrese una opcion: "))
    if opcion == 1: 
        CargarArchivo()
    elif opcion==2: 
        print()
    elif opcion==3:
        print()
    elif opcion==4:
        print("> Carlos Augusto Calderon Estrada\n> 201905515\n> Introduccion a la Programacion y computacion 2 Seccion D\n >Ingenieria en Ciencias y Sistemas\n >4to Semestre")
    elif opcion==5:
        print()
    elif opcion==6:
        print()
    else: 
        print("Elija una de las opciones que se le presentan ")

def CargarArchivo():
    ruta = input("Escriba la ruta del archivo: ")
    tree = ET.parse(ruta)
    root = tree.getroot()
    Lista = ListaSimple()
    
    for elemento in root:
        Lista2 = ListaSimple()
        nombreTerreno = elemento.attrib['nombre']
        contadorposicion=1
        for ele in elemento:
               
            for e in ele:
                texto = ele.tag
                print(texto)
                if contadorposicion !=5:
                    if contadorposicion==1:
                        xInicial = e.text
                        contadorposicion+=1
                        
                    elif contadorposicion==2:
                        yinicial = e.text
                        contadorposicion+=1
                        
                    elif contadorposicion ==3 :
                        xfinal = e.text
                        contadorposicion+=1
                        
                    elif contadorposicion==4:
                        yfinal = e.text
                        contadorposicion+=1
                        
            if ele.tag=='posicionfin':
                continue
            elif ele.tag=='posicion':
                Lista2.InsertarSimple(ele.attrib['x'], ele.attrib['y'], ele.text)
            
        Lista.InsertarS(nombreTerreno, xInicial, yinicial,xfinal,yfinal,Lista2)            

    
Menu()