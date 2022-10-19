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



                
def listar_archivos(d,ap):
    l_archivos = os.listdir("./files/{}m/MR{}".format(d,ap))
    #l_archivos.remove('MR33') , l_archivos.remove('MR44'), l_archivos.remove('MR74')
    return l_archivos


def calculo_n(RSSI1m,avr_filtrado,d,d0):
    global n_lista
    n = (RSSI1m-avr_filtrado)/(10*math.log10(d/d0))
    print("N es: ", n)
    n_lista.append(n)
    return n_lista

# lista_datos son los valores del archivo, solo han pasado por el filtro de eliminar el max10% y min10%
def filtro_kalman(d,ap,grafica = 'NO',calcula_n = 'NO'):
    l_archivos = listar_archivos(d,ap)
    testData = []
    for i in l_archivos:
        if 'filtrado' and '5b' in i:
            print("Para el archivo: ",i)
            lista_datos = []
            with open("./files/{}m/MR{}/".format(d,ap)+i) as archivo:
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
        plt.axis([0,len(lista1),min(lista1)-5,max(lista1)+5])
        plt.show(block = True)
  
def grafica_n(n_lista):       
    plt.plot(n_lista, marker='.',color = '#94e630',label = 'RSSI')   # Dibuja el gráfico
    plt.legend(('n'), loc = 'lower center')
    plt.show(block = True)

#-53.07061  
#  -66.5436 2M
 
RSSIo = -63.020
d0 = 1
d = 4
ap = '74'
filtro_kalman(d,ap,grafica='SI',calcula_n = 'SI')          
    
    


#calculo_n(RSSI1m= -53.070601 , d, avr_filtrado=promedio_filtro )   






