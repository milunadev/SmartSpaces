
import json 
from channels.consumer import AsyncConsumer 
from channels.generic.websocket import WebsocketConsumer
from random import randint 
from time import sleep
from pruebas import sensores
from mqtt import camara

     

class WSConsumer(WebsocketConsumer): 

    def connect(self): 
        self.accept() 
        for i in range(5): 
            self.send(json.dumps({'message':randint(1,100)})) 
            sleep(3) 
        self.disconnect() 

    def disconnect(self): 
        print("Disconnecting") 
    
class WSConsumer_mqtt(WebsocketConsumer):
    def connect(self): 
        self.accept() 
    
class WSConsumer_laboratorio(WebsocketConsumer):
    def connect(self): 
        self.accept() 
        metricas = sensores()
        #n_personas = str(camara()) #+ ' personas'
        n_personas = str(2) #+ ' personas'
        self.send(json.dumps({'temperatura':metricas[2],'humedad':metricas[0],'puerta':metricas[1],'personas':n_personas})) 
        sleep(2)
        #self.disconnect()

    def disconnect(self): 
        print("Disconnecting") 


        