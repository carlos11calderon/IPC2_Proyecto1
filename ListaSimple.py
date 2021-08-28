from NodoSimple import *
from NodoGeneral import *
class ListaSimple:
    def __init__(self):
        self.cabeza=None

    def EstadoLista(self):
        return self.cabeza == None


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
        


    
    def ObtenerNodo(self, x, y):
        auxiliar = self.cabeza
        while auxiliar != None:
            if (x==int(auxiliar.x)) and (y==int(auxiliar.y)):
                return auxiliar.valor
            auxiliar = auxiliar.siguiente
        return None


    def ImprimirSimple(self,filas,columnas):
        for i in range(1, int(filas)+1):
            auxFila=""
            for j in range(1,int(columnas)+1):
                auxFila += "["+ str(self.ObtenerNodo(i,j)) +"]"
            print(auxFila)

    def otroImprimir(self):
        auxiliar = self.cabeza
        while auxiliar is not None:
            print(auxiliar.nombre)
            print(auxiliar.relleno.recorrerFilas())
            auxiliar = auxiliar.siguiente

    def CaminoCorto(self, filas,columnas, poInix,poIniy, PoFinx,PoFiny, valor):
        auxiliar = self.cabeza
        while auxiliar != None:
            if(poInix==int(auxiliar.x)and poIniy==int(auxiliar.x)):
                ValorInicial = auxiliar.valor
                self.etiquetar(filas,columnas,poInix,poIniy,ValorInicial)

                    
    def etiquetar(self,filas,columnas, x,y,valor):
        aux = self.cabeza
        valorInicial = valor
            
        for i in range(1, int(filas)+1):
          
            for j in range(1, int(columnas)+1):
                valorInicial + aux.relleno.y


    def GetTodaMatriz(self,nombre):
        auxiliar = self.cabeza
        while auxiliar is not None:
            if auxiliar.nombre == nombre:
                return auxiliar
            auxiliar = auxiliar.siguiente
        return None
                    
        