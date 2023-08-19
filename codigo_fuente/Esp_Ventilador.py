from machine import Pin
from time import sleep
import random
import network
from umqtt.simple import MQTTClient

rojo = Pin(4, Pin.OUT)
amarilla = Pin(5, Pin.OUT)
verde = Pin(21, Pin.OUT)

#Variable global del mensaje.
mensaje= None

#Hacemos las configuraciónes de MQTT
MQTT_BROKE = "broker.hivemq.com"
MQTT_USER = ""
MQTT_PASSWORD = ""
MQTT_CLIENTE_ID = ""
MQTT_TOPIC_1 = "sd/ventilador"
MQTT_PORT = 1883

# Función para conectar al WiFi
def wifi_conect():
    print("Conectando al WiFi...", end="")
    sta_if = network.WLAN(network.STA_IF)
    sta_if.active(True)
    while not sta_if.isconnected():
        try:
            sta_if.connect('POCO X3 Pro', '12345678')
            while not sta_if.isconnected():
                print(".", end="")
                sleep(0.3)
        except OSError as e:
            print("Error de WiFi:", e)
            sleep(5)  # Esperar antes de intentar nuevamente

    print("WiFi conectado")

    
# Función para procesar los mensajes recibidos
def callback(topic, msg):
    #Indica que se utiliza una variable globan en lugar de una local
    global mensaje
    mensaje= msg.decode()
    print("Mensaje recibido - Tópico: {}, Mensaje: {}".format(topic, msg.decode()))

def connect_and_subscribe():
    client = MQTTClient(MQTT_CLIENTE_ID,MQTT_BROKE, port = MQTT_PORT,user = MQTT_USER, password = MQTT_PASSWORD, keepalive = 30)
    client.set_callback(callback)
    client.connect();
    print("OK")
    client.subscribe(MQTT_TOPIC_1)
    #print("Conectado al servidor MQTT y suscrito al tópico: {}".format(MQTT_TOPIC_1))
    return client

#Programa principal
wifi_conect()
client = connect_and_subscribe()

#Apagando todos los pines
rojo.value(1)
amarilla.value(1)
verde.value(1)


while True:
    try:
        client.wait_msg()
        print(mensaje)
        rojo.value(1)
        amarilla.value(1)
        verde.value(1)
        
        estatus = int(mensaje)

        if estatus == 1:
            #sleep(2)
            rojo.value(0)
            amarilla.value(1)
            verde.value(1)
        elif estatus == 2:
            #sleep(2)
            rojo.value(1)
            amarilla.value(0)
            verde.value(1)
        elif estatus == 3:
            #sleep(2)
            rojo.value(1)
            amarilla.value(1)
            verde.value(0)
        else:
            rojo.value(1)
            amarilla.value(1)
            verde.value(1)
    except Exception as e:
        print("Error durante la espera de mensajes:", e)
        try:
            client.disconnect()  # Intentar desconectar en caso de error
        except:
            pass  # Puede que la desconexión también falle, no es un problema
        client = connect_and_subscribe()  # Intentar reconectar a MQTT
