
from django.shortcuts import redirect, render
from django.http import HttpResponse 
from .database_file import connect_db, database_search, snapshot    
from .forms import *
from django.http import HttpResponseRedirect
from datetime import *

def index(request): 
    return render(request, 'index2.html', context={'text': 'Hello world'})

def monitoring(request): 
    
    if request.method == "POST":
        sala = request.POST.get('salaescogida')
        freserva = request.POST.get('freserva')
        
        request.session['sala']= sala
        data = {'sala': sala, 'freserva': freserva}
        return redirect(reservar, sala = sala, freserva= freserva)
    url = snapshot()
    return render(request, 'monitoring.html', context={'url': url})

def reservar(request,sala,freserva): 
    context = {}
    context['form'] = Reserva_sala()    
    #print('AQUII',sala, type(freserva))
    fechas_reservadas = database_search(sala, freserva)
    context['sala']=sala
    context['freservada']=freserva
    context['fechasocupadas'] = fechas_reservadas
    
    if request.method == "POST":
        freserva = request.POST.get('freserva')
        email = request.POST.get('email')
        init_time = request.POST.get('horainicio')
        end_time = request.POST.get('horafin')
        print(init_time)
        connect_db('laboratorio',freserva,init_time,end_time,email) 
        fechas_reservadas = database_search(sala, freserva)
        context['sala']=sala
        context['freservada']=freserva
        context['fechasocupadas'] = fechas_reservadas

    return render(request, 'reserva.html', context)

def index_oficial(request): 
    return render(request, 'index_oficial.html', context={'text': 'Hello world'})
  
def landing(request):
    context = {}
    context['form'] = Reserva()   
    if request.method == "POST":
        sala = request.POST.get('salaescogida')
        freserva = request.POST.get('freserva')   
        request.session['sala']= sala
        data = {'sala': sala, 'freserva': freserva}
        return redirect(reservar, sala = sala, freserva= freserva)
        #return render(request, 'reserva.html', data)
    
    return render(request, 'environment.html', context)

