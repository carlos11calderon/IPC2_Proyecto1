from NodoSimple import *
from NodoGeneral import *
class ListaSimple:
    def __init__(self):
        self.cabeza=None

    def InsertarS(self, nombre,pinicialx, pinicialy, pfinalx,pfinaly,relleno):
        nuevo = NodoGeneral(nombre,pinicialx, pinicialy, pfinalx,pfinaly,relleno, None)
        if self.cabeza is None:
            self.cabeza = nuevo
        else:
            auxiliar = self.cabeza
            while auxiliar.siguiente is not None:
                auxiliar = auxiliar.siguiente
            auxiliar.siguiente = nuevo

    def InsertarSimple(self, x, y, valor):
        nuevo = NodoSimple(x, y, valor)
        if self.cabeza is None:
            self.cabeza = nuevo
        else:
            auxiliar = self.cabeza
            while auxiliar.siguiente is not None:
                auxiliar = auxiliar.siguiente
            auxiliar.siguiente = nuevo

    def ImprimirSimple(self):
        auxiliar = self.cabeza
        while auxiliar is not None:
            print("x: " + auxiliar.x + " | y: " + auxiliar.y + " | Valor: " + auxiliar.valor)
            auxiliar=auxiliar.siguiente