from paho.mqtt import client as mqtt_client
import json
import time
from kalman import kalman_lista


broker = '192.168.128.17'
topic74 = 'meraki/v1/mr/N_611363649415560954/0C:8D:DB:D9:17:32/ble/#'
topic33 = 'meraki/v1/mr/N_611363649415560954/68:3A:1E:83:31:8F/ble/#'
topic44 = 'meraki/v1/mr/N_611363649415560954/F8:9E:28:74:51:F9/ble/#'

def on_connect(client, userdata, flags, rc): 
      if rc==0: 
          print("connected OK") 
      else: 
            print("Bad connection Returned code= ",rc) 

def on_message(client, userdata, message):
        global message_dic
        message = json.loads(message.payload.decode("utf-8")) 
        metrics = '\n' + message['mrMac'] + ',' + message['clientMac'] + ',' +message['rssi'] 
        if message['clientMac']== beacon_mac:
            print(message['mrMac'] + '    ' + message['clientMac'] + '    ' +message['rssi']) 
        #print(message['mrMac'] + '    ' + message['clientMac'] + '    ' +message['rssi']) 
            message_dic.append(int(message['rssi']))
        
        return message_dic

def filtro_max_min(message):
    message.sort()
    n=round(0.1*len(message))
    datos = list(message[n:(len(message)-n)])
    print('ORDENA ',datos)
    lst3 = []
    for value in message_dic:
        if value in datos:
            lst3.append(value)
            datos.remove(value)         
    print(message_dic)
    print('FINAL ',lst3)
    return lst3
    
def toma_muestra(topics):
    global message_dic
    rssi_avg_lista = []
    for topic in topics:
        client.connect(broker)
        client.subscribe(topic)
        print("suscrito a " + topic)
        client.on_message = on_message
        client.loop_start()
        time.sleep(3)
        #message_dic_or = message_dic[:]
        #message_filtrado = filtro_max_min(message_dic_or)
        rssi_avg = kalman_lista(message_dic)
        rssi_avg_lista.append(rssi_avg_lista)
        message_dic = []
        client.loop_stop()
        client.disconnect()
        
    return rssi_avg_lista

def general():
    global client 
    client = mqtt_client.Client('mqtt_client')
    client.on_connect = on_connect
    topics = [topic44,topic74,topic33]
    rssi_avg_lista = toma_muestra(topics)
    return rssi_avg_lista 

beacon_mac ='00:FA:B6:01:E8:6D'