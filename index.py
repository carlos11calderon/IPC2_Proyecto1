#import
from typing import List
from _elementtree import *
from ListaSimple import *
from MatrizOrtogonal import Ortogonal
from NodoSimple import *
import xml.etree.cElementTree as ET
import os
import time
from graphviz import *



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
        Menu()
    elif opcion==2: 
        
        Menu()
        print()
    elif opcion==3:
        print()
    elif opcion==4:
        print("> Carlos Augusto Calderon Estrada\n> 201905515\n> Introduccion a la Programacion y computacion 2 Seccion D\n >Ingenieria en Ciencias y Sistemas\n >4to Semestre")
    elif opcion==5:
        graficarMatriz()
    elif opcion==6:
        print()
    else: 
        print("Elija una de las opciones que se le presentan ")

def CargarArchivo():
    global Lista
    global ruta
    try:
        # obtengo ruta del archivo
        ruta = input("Escriba la ruta del archivo: ")
        tree = ET.parse(ruta)
        root = tree.getroot()
        #objeto de la lista
        Lista=ListaSimple()
        
        #con este for recorro el root, la lista
        for elemento in root:
            Lista2 = ListaSimple() #con esto es un segundo objeto que pertenece a la lista de posiciones
            matrixOrto = Ortogonal()
            nombreTerreno = elemento.attrib['nombre']   ##aqui obtengo el nombre del terreno
            contadorDimension = 1
            for di in elemento:
                if contadorDimension!=3:
                    for d in di:

                        if contadorDimension==1:
                            DimensionN = d.text
                            contadorDimension+=1
                        elif contadorDimension ==2:
                            DimensionM = d.text
                            contadorDimension+=1
                else:
                    break
                
               
            contadorposicion=1          ## este contador permite tener control de la lectura de las coordeneadas iniciales y finales 
            for ele in elemento: # con este for valuno las etiquetas despues de obtener el nombre del terreno
                if ele.tag != "dimension" and ele.tag != "DIMENSION":
                    for e in ele: # con este for evaluo las etiquetas de las posiciones iniciales y finales
                        texto = ele.tag
                        print(texto)
                        ## Esta serie de if obtiene los valores de las posiciones iniciales y finales, y las guarda en una variable local
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
                    ## Este if valua los recorridos adicionales despues de obtener las posiciones iniciales y finales, y omite el bucle para avanzar
                    if ele.tag=='posicionfin':
                        continue
                    elif ele.tag == 'posicioninicio':
                        continue
                    # este elif valua cuando el for entra en las posiciones de la segunda lista
                else: 
                    continue
                Lista2.InsertarSimple(ele.attrib['x'], ele.attrib['y'], ele.text) ## mandamos al objeto de la segunda lista las posiciones
                matrixOrto.InsertarMatriz(ele.attrib['x'],ele.attrib['y'],ele.text)

            Lista.InsertarS(nombreTerreno, xInicial, yinicial, xfinal, yfinal, matrixOrto)# mandamos al objeto del nodo las coordenadas iniciales y finales más la informacion del terreno

            #Lista2.ImprimirSimple(DimensionN,DimensionM)
    except IOError:#exceptiones
        print("Error")
    Lista.otroImprimir()

def graficarMatriz():
    global ruta
    linea=""
    print("--------------------Generar grafica-------------------------")
    print("******Se esta generando la grafica...******")
    time.sleep(3)
    tree = ET.parse(ruta)
    root = tree.getroot()
    for elemento in root:
        nombreTerreno = elemento.attrib['nombre']
        contadorDimension = 1
        for di in elemento:
            if contadorDimension != 3:
                for d in di:

                    if contadorDimension == 1:
                        DimensionN = d.text
                        contadorDimension += 1
                    elif contadorDimension == 2:
                        DimensionM = d.text
                        contadorDimension += 1
            else:
                break
        contadorposicion = 1  ## este contador permite tener control de la lectura de las coordeneadas iniciales y finales
        c3 = 1
        c5 = 0
        f = open('archivo.dot', 'w', encoding='utf-8')
        f.write("digraph dibujo{\n")
        f.write('rankdir=UD;\n')
        f.write('node [shape = ellipse, style=filled, fillcolor=white]edge [arrowhead="none"];\n')

        for ele in elemento:  # con este for valuno las etiquetas despues de obtener el nombre del terreno
            if ele.tag != "dimension":
                for e in ele:  # con este for evaluo las etiquetas de las posiciones iniciales y finales
                     pass
                if ele.tag == 'posicionfin':
                        continue
                elif ele.tag == 'posicioninicio':
                        continue
                    # este elif valua cuando el for entra en las posiciones de la segunda lista
            else:
                continue
            f.write('valor' + str(c3) + '[ label ="' + ele.text + '"];\n')
            DimensionM = int(DimensionM)
            DimensionN = int(DimensionN)
            if c3 <= int(DimensionM):
                f.write('valor' + str(c3) + '->valor' + str(c3 + DimensionM) + ';\n')
            elif c3 > DimensionM and c3 <= (DimensionM * DimensionN) - DimensionM:
                f.write('valor' + str(c3) + '->valor' + str(c3 + DimensionM) + ';\n')
            elif c3 == (DimensionM * DimensionN) - DimensionM:
                break
            c3 = c3 + 1

        for i in range(1, DimensionN + 1):
            c4=i*DimensionM
            for j in range(DimensionM):
                c5 += 1
                if(j!=DimensionM-1):
                    f.write('valor' + str(c5) + '->valor' + str(c5 + 1) + ';\n')
                    linea = linea + "valor" + str(c5) + ";"
            linea = linea + "valor" + str(c5) + ";"
            f.write('{rank = same;' + linea + '};\n')
            linea=""

        f.write('labelloc="t";')
        f.write('label="' + nombreTerreno + '";')
        f.write('}')
        f.close()

        os.system('dot -Tpdf archivo.dot -o reporte_'+nombreTerreno+'.pdf')
        os.system('reporte_'+nombreTerreno+'.pdf')

Menu()