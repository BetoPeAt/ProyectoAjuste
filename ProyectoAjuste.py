import random
import decimal

class ProyectoAjuste:
    '''
    Genera aleatorio dentro de un rango
    for x in range(8):
        Va de 1 a 10 el número aleatorio
        print(random.randrange(1,11), end=', ')
    '''
    #Creando nuestra lista bidimensional
    def __init__(self,tablaPuntos=[['Punto','x','y']],tablaIteraciones=[['Id','a','b','c','Z']],
                 tablaConMejorMinimo=['Min Z','a','b','c'],minimo=100000,maximo=-100000,noPunto=1,noId=1):

        self.tablaPuntos=tablaPuntos        #Tabla con los puntos
        self.tablaIteraciones=tablaIteraciones  #Tabla que tiene los valores aleatorios de acuerdo a rangos
        self.tablaConMejorMinimo=tablaConMejorMinimo    #Tabla que tiene el mejor mínimo
        self.minimo=minimo  #Límite inferior
        self.maximo=maximo  #Límite superior
        self.noPunto=noPunto    #Número de punto para las tablas
        self.noId=noId          #Número de Id para las tablas

    #Llenando la lista bidimensional tablaPuntos con puntos dados
    def agregaPunto(self,x,y): #noDePut= Número de punto
        nuevaFila=[self.noPunto,x,y]        #Guardando en una lista para agregarla a lista bidimensional tablaPuntos
        self.tablaPuntos.append(nuevaFila)
        self.noPunto+=1

    def verTablaPuntos(self):
        for fila in self.tablaPuntos:   #Recorriendo filas
            for elemento in fila:        #Recorriendo columnas o elementos de filas
                print(f'{elemento}'.center(10),end='')
            print()

    #Este método recorre la tabla de puntos para hallar los valores cuadráticos
    #Sólo se puede invocar si se ha llenado la tabla
    def encuentraLimitesCuadraticos(self):
        #Los límites para la función cuadrática, son el doble de 'x' o 'y' más grande

        #Encontrando el máximo y el mínimo de la columna 'X'
        for elementoX in self.tablaPuntos:
            #Elemento se va moviendo entre filas
            if(elementoX[0]!='Punto'):
                if(elementoX[1]>self.maximo):
                    self.maximo=elementoX[1]
                if(elementoX[1]<self.minimo):
                    self.minimo=elementoX[1]

        # Encontrando el máximo y el mínimo de la columna 'Y' y reemplazando a los de la X, de ser necesario
        for elementoY in self.tablaPuntos:
            #Elemento se va moviendo entre filas
            if(elementoY[0]!='Punto'):
                if(elementoY[2]>self.maximo):
                    self.maximo=elementoY[2]
                if(elementoY[2]<self.minimo):
                    self.minimo=elementoY[2]
        print(f'\nMínimo de "x" y de "y": {self.minimo}')
        print(f'Máximo de "x" y de "y": {self.maximo}')

        #Obteniendo el quintuple del mínimo y el máximo, **ESTO LO DETERMINAMOS NOSOTROS***
        self.minimo*=5
        self.maximo*=5

    #Método que calcula la F.O Z
    def calculaZCuadratica(self,a=0,b=0,c=0):
        #Iré recorriendo la tabla de puntos por que tendré que utilizarlos
        Z=0 #Aquí iré guardando mis valores

        #Prueba de Funcionamiento
        for element in self.tablaPuntos:
            if element[0]!='Punto':#Evitando la primera columna
                #Moviendome entre filas
                y=element[2]
                x=element[1]
                Z+=round(abs((y)-((a*(x**2))+(b*x)+c)),3)

        Z=round(Z,3)

        return Z


    # Encontrando un aleatorio con 3 decimales, multiplicando los límites por 1000 y luego dividiendo entre 1000
    def encuentraAleatorio(self):
        valor = float(decimal.Decimal(random.randrange(self.minimo * 1000, (self.maximo + 1) * 1000)) / 1000)
        return valor

    #Este método sólo se puede aplicar una vez calculados los límites
    def llenaTablaIteraciones(self):

        for x in range(10):     #Si se aumenta el rango se pueden añadir más elementos a la tabla
            Id=self.noId
            a=self.encuentraAleatorio()
            b=self.encuentraAleatorio()
            c=self.encuentraAleatorio()
            Z=self.calculaZCuadratica(a,b,c)
            nuevaFila=[self.noId,a,b,c,Z]
            self.tablaIteraciones.append(nuevaFila)
            self.noId+=1

    def verTablaIteraciones(self):
        for fila in self.tablaIteraciones:   #Recorriendo filas
            for elemento in fila:        #Recorriendo columnas o elementos de filas
                print(f'{elemento}'.center(10),end='')
            print()



proyecto= ProyectoAjuste()

proyecto.agregaPunto(-7,-9)
proyecto.agregaPunto(9,-4)
proyecto.agregaPunto(6,-9)
proyecto.agregaPunto(7,1)
proyecto.agregaPunto(0,6)
proyecto.agregaPunto(-7,5)
proyecto.agregaPunto(9,-9)
proyecto.agregaPunto(4,8)
proyecto.agregaPunto(-1,9)
proyecto.agregaPunto(9,1)
print()

proyecto.verTablaPuntos()
proyecto.encuentraLimitesCuadraticos()

print(f'\nMáximo: {proyecto.maximo}, Minimo: {proyecto.minimo} Cuadráticos')

print()
proyecto.llenaTablaIteraciones()
proyecto.verTablaIteraciones()

print()
Z=proyecto.calculaZCuadratica()
print(f"\n *{Z}")

'''
for x in range(100):
    print(proyecto.encuentraAleatorio())
'''