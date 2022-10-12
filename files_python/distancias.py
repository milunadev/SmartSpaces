import math
from mapa import graficar

from mqtt_consumer import general

def MR44(RSSI):
    RSSIo = -49.50817
    n = 1.617
    d_44 = pow(10,-((RSSI-RSSIo)/(10*n)))
    return d_44    
    
def MR74(RSSI):
    RSSIo = -51.624667
    n = 2.969
    d_74 = pow(10,-((RSSI-RSSIo)/(10*n)))
    return d_74     
    
#DUDOSO  
def MR33(RSSI):
    RSSIo = -56.2707
    n = 1.3465
    d_33 = pow(10,-((RSSI-RSSIo)/(10*n)))
    return d_33     

def APs(RSSI):
    RSSIo = -53.01093
    n = 2.029
    d = pow(10,-((RSSI-RSSIo)/(10*n)))
    return d    


def trilateration(r1,r2,r3):
    [x1,y1] = [1.611, 2.274] 
    [x2,y2] = [4.366, 4.144]
    [x3,y3] = [3.854, 2.887] 
    A = 2*x2 - 2*x1
    B = 2*y2 - 2*y1
    C = r1**2 - r2**2 - x1**2 + x2**2 - y1**2 + y2**2
    D = 2*x3 - 2*x2
    E = 2*y3 - 2*y2
    F = r2**2 - r3**2 - x2**2 + x3**2 - y2**2 + y3**2
    x = (C*E - F*B) / (E*A - B*D)
    y = (C*D - A*F) / (B*D - A*E)
    return x,y

rssi_avg_lista = general()
d_44 = MR44(rssi_avg_lista[0])
d_74 = MR74(rssi_avg_lista[1])
d_33 = MR33(rssi_avg_lista[2])
print(d_44,d_74,d_33)

[x,y]=trilateration(d_44,d_74,d_33)
print(x,y)
graficar(x,y)