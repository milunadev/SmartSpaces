from django import forms

class Reserva(forms.Form):
    sala = forms.CharField(label='sala', max_length=100)
    fecha = forms.DateField()

class Reserva_sala(forms.Form):
    email  = forms.CharField(label='email', max_length=100)
    fecha = forms.DateField()
    init_time = forms.TimeField()
    end_time = forms.TimeField()
    data = [email,init_time,end_time]
    