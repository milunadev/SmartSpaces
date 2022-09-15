import requests
import json 
from channels.consumer import AsyncConsumer 
from channels.generic.websocket import WebsocketConsumer
from random import randint 
from time import sleep

## REQUEST INFO ###

url = "https://api.meraki.com/api/v1/organizations/122494/sensor/readings/latest" 
payload = None
headers = { 
    "Content-Type": "application/json", 
    "Accept": "application/json", 
    "X-Cisco-Meraki-API-Key": "771d04c7ce12516c5146a80cc17826d53bebc706" 
} 

def sensores():
    response = requests.request('GET', url, headers=headers, data = payload) 
    print(response.json()[0]['readings'])
    temp_hum= response.json()[0]['readings'][1]
    if 'temperature' in temp_hum:
        temperature = response.json()[0]['readings'][1]['temperature']['celsius']
        humidity = response.json()[0]['readings'][2]['humidity']['relativePercentage']
    else: 
        temperature = response.json()[0]['readings'][2]['temperature']['celsius']
        humidity = response.json()[0]['readings'][1]['humidity']['relativePercentage']
    door_o = response.json()[2]['readings'][1]['door']['open']
    if door_o==True: door='Abierto' 
    else: door= 'Cerrado'
    metricas = [str(humidity)+'%', door, str(temperature)+'º']
    print(humidity, door, temperature, '   ',response.json()[0]['readings'])
    return metricas

#sensores()