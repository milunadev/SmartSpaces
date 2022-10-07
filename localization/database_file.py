from types import NoneType
import pymysql  
import requests
import datetime

def connect_db(name,freserva,init_time,end_time,email):
    now = datetime.datetime.now()
    fecha_registro = now.strftime("%d/%m/%Y")
    print(fecha_registro)
    hostaws = 'database-ss.cinsfnujndka.us-east-2.rds.amazonaws.com'
    connection = pymysql.connect(host = hostaws, user = 'admin', password= 'Cisco12345', database='LOGS')
    with connection:
        cur = connection.cursor()
        statement = "INSERT INTO {} (sala , fregistro , freserva , hinicio , hfinal , usuario) VALUES (%s,%s,%s,%s,%s,%s)".format(name)
        cur.execute(statement,('lab',fecha_registro,freserva,init_time, end_time, email))
        connection.commit()
        statement2 = "SELECT * FROM laboratorio"
        cur.execute(statement2)
        result = cur.fetchone()
        print(result)
    
def database_search(sala_id,sfreserva):
    freserva = datetime.datetime.strptime(sfreserva, '%Y-%m-%d')
    hostaws = 'database-ss.cinsfnujndka.us-east-2.rds.amazonaws.com'
    connection = pymysql.connect(host = hostaws, user = 'admin', password= 'Cisco12345', database='LOGS')
    with connection:
        cur = connection.cursor(pymysql.cursors.DictCursor)
        statement = "SELECT *  FROM {}  WHERE freserva = '{}' ".format(salas_id(sala_id),str(freserva))
        print(statement)
        cur.execute(statement)
        query = cur.fetchall()
        print('QUERY',query)
        ocupados = periodos_ocupados(query)
        print("RSERVADOS" , ocupados)
        connection.commit()
        return ocupados
        
def salas_id(sala_id):
    diccionario = { '1':'laboratorio', '2': 'MacchuPicchu'}
    sala = diccionario[sala_id]
    return sala

def periodos_ocupados(query):
    periodos = []
    print(query)
    if query != NoneType:
        for i in query:
            hinicio = calcular_hora(i['hinicio'])
            hfinal = calcular_hora(i['hfinal'])
            periodos.append('{}-{}'.format(hinicio,hfinal))
    return periodos
    
def calcular_hora(delta):
    sec = delta.seconds
    hours = sec // 3600
    minutes = (sec // 60) - (hours * 60)
    #print(hours,':',minutes)
    hora = str(hours)+':'+str(minutes)
    return hora

def snapshot():
    url = "https://api.meraki.com/api/v1/devices/Q2GV-2V9V-NMDF/camera/generateSnapshot"
    payload = '''{
        "fullframe": false
    }'''
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "X-Cisco-Meraki-API-Key": "771d04c7ce12516c5146a80cc17826d53bebc706"
    }
    response = requests.request('POST', url, headers=headers, data = payload)
    url = (response.json())['url']
    #print((response.json())['url'])
    return url