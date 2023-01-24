from matplotlib import markers
from pylab import *

from PIL import Image

import matplotlib.cbook as cbook



def graficar(x,y):
    datafile = cbook.get_sample_data('/home/cisco/mluna_proyect/smart_spaces/files_python/mapa.png')
    h = Image.open(datafile)
    #dpi = rcParams['figure.dpi']
    #print(dpi)
    dpi= 50
    figsize = h.size[0]/dpi, h.size[1]/dpi

    figure(figsize=figsize)
    ax = axes([0,0,1,1], frameon=False)
    ax.set_axis_off()
    ax.set_xlim(0,50)
    ax.set_ylim(0,54)
    [x44,y44] = [13.68,16.26]
    [x33,y33] = [32.20,22.24]
    [x74,y74] = [40,50]
    d44 =  sqrt((x44-x)**2 + (y44-y)**2)
    d33 =  sqrt((x33-x)**2 + (y33-y)**2)
    d74 =  sqrt((x74-x)**2 + (y74-y)**2)
    print("Distancias-> d44: ",d44, " d33: ",d33, " d74: ",d74)
    #im = imshow(h, origin='upper',extent=[-2,4,-2,4])  # axes zoom in on portion of image
    #im2 = imshow(h, origin='lower',extent=[0,6,0,7]) # image is a small inset on axes
    plt.plot(x,y,marker='*',color = 'blue')
    plt.plot([x44,x],[y44,y],color = 'red')
    plt.plot(13.68,16.26,marker='$4$',color = 'red')
    plt.plot([x74,x],[y74,y],color = 'red')
    plt.plot(40,50,marker='$7$',color = 'red')
    plt.plot([x33,x],[y33,y],color = 'red')
    plt.plot(32.20,22.24,marker='$3$',color = 'red')
    plt.imshow(h, origin='lower',extent=[0,50,0,54])
    plt.show()

graficar(4,5)