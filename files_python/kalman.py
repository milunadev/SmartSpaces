from logging import handlers
import math
import os
from turtle import delay
from kalman_class import KalmanFilter
import matplotlib.pyplot as plt
import numpy as np
 
#import matplotlib.pyplot as plt
#import numpy as np

lista = []
n_lista = []
promedios_rssi = []



                
def listar_archivos(d):
    l_archivos = os.listdir("./files/{}m".format(d))
    l_archivos.remove('MR33') , l_archivos.remove('MR44'), l_archivos.remove('MR74')
    return l_archivos


def calculo_n(RSSI1m,avr_filtrado,d,d0):
    global n_lista
    n = (RSSI1m-avr_filtrado)/(10*math.log10(d/d0))
    print("N es: ", n)
    n_lista.append(n)
    return n_lista

# lista_datos son los valores del archivo, solo han pasado por el filtro de eliminar el max10% y min10%
def filtro_kalman(d,grafica = 'NO',calcula_n = 'NO'):
    l_archivos = listar_archivos(d)
    for i in l_archivos:
        if 'filtrado' in i:
            print("PARA EL ARCHIVO: ",i) 
            lista_datos = []
            with open("./files/{}m/".format(d)+i) as archivo:
                for linea in archivo:
                    datos = (linea.rstrip()).split(',')
                    #print(datos)
                    for i in datos:
                        lista_datos.append(int(i))
            testData = lista_datos
            filterData = []               
            ##DEFINIR LOS PARÁMETROS DEL FILTRO KALMAN            
            test = KalmanFilter(0.01, 3)
            
            for x in testData:
                #print ("Data:", x)
                filterData.append(test.filter(x))
                #print ("Filtered Data: ", test.filter(x))
            
            promedio_datos  = sum(testData)/len(testData)
            promedio_filtro = sum(filterData)/len(filterData)
            print("Promedio sin filtro: ", promedio_datos, "  Promedio con filtro: ",promedio_filtro)
            promedios_rssi.append(promedio_filtro)
            print('RSSI prom: ',promedio_filtro)
            
            if grafica == 'SI':
                graficas_rssi(testData,filterData)
        
            if calcula_n == 'SI':  
                calculo_n(RSSIo,promedio_filtro,d,d0)
            
    print("El promedio final para {} metro(s) es: ".format(d),sum(promedios_rssi)/len(promedios_rssi))    
    if calcula_n == 'SI':    
        print("El promedio final de N para {} metro(s) es: ".format(d),sum(n_lista)/len(n_lista))
        grafica_n(n_lista) 
 
def kalman_lista(lista_datos):
    print("Enrando al filtro Kalman, lista de entrada: ", lista_datos)
    testData = lista_datos
    filterData = []  
    test = KalmanFilter(0.01, 3)
    for x in testData:
            filterData.append(test.filter(x))
    promedio_filtro = sum(filterData)/len(filterData)
    return promedio_filtro
            
def graficas_rssi(testData,filterData):    
        #Gráficas
        lista1 = testData
        lista2 = filterData
        plt.plot(lista1, marker='.',color = '#94e630',label = 'RSSI')   # Dibuja el gráfico
        plt.xlabel("N° muestra (s)", fontsize = 10)
        plt.ylabel("RSSI(dbm)", fontsize = 10)
        plt.ioff()   # Desactiva modo interactivo de dibujo
        #plt.plot(lista2)   # No dibuja datos de lista2
        plt.ion()   # Activa modo interactivo de dibujo
        plt.plot(lista2,marker='.',color = '#fabbf4',label = 'RSSI Kalman')   # Dibuja datos de lista2 sin borrar datos de lista1
        plt.legend(('RSSI','RSSI Kalman'), loc = 'lower center')
        plt.axis([0,len(lista1),max(lista1)-3,min(lista1)+3])
        plt.show(block = True)
  
def grafica_n(n_lista):       
    plt.plot(n_lista, marker='.',color = '#94e630',label = 'RSSI')   # Dibuja el gráfico
    plt.legend(('n'), loc = 'lower center')
    plt.show(block = True)

#-53.01093   
RSSIo = -58.21809
d0 = 2
d = 4
filtro_kalman(d,grafica='NO',calcula_n = 'SI')          
    
    


#calculo_n(RSSI1m= -53.070601 , d, avr_filtrado=promedio_filtro )   






