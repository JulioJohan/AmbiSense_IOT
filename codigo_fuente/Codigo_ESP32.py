import time
import network
from umqtt.simple import MQTTClient
from machine import Pin
import dht
import neopixel


# Pines y variables para PIR.
motion = False
led = Pin(4, Pin.OUT)
pir = Pin(18, Pin.IN)
buzzer= Pin(23, Pin.OUT)

# Configuración del pin del sensor MQ-2
pin_sensor = Pin(35, Pin.IN)

# Motor
pin_motor = Pin(27, Pin.OUT)
#LED RGB
neo_rojo = neopixel.NeoPixel(Pin(23), 256)
neo_azul = neopixel.NeoPixel(Pin(21), 256)

# Configuraciones de MQTT	
MQTT_BROKER = "broker.hivemq.com"
MQTT_USER = ""
MQTT_PASSWORD = ""
MQTT_CLIENT_ID = ""
MQTT_TOPIC_1 = "utng/pir"
MQTT_TOPIC_2 = "utng/gas"
MQTT_TOPIC_3 = "utng/temp"
MQTT_TOPIC_4 = "utng/humedad"

MQTT_PORT = 1883


#Medicion de temperatura y humedad
def sensor_temp():
    sensor.measure()
    temp = sensor.temperature()
    return round(temp,1)

# Medición de Humedad
def sensor_hum():
    hum = sensor.humidity()
    return round(hum, 1)


# Función para conectar al WiFi
def wifi_connect():
    print("Conectando al WiFi...")
    sta_if = network.WLAN(network.STA_IF)
    sta_if.active(True)
    
    if not sta_if.isconnected():
        sta_if.connect('LAPTOP-EEKAKGFK 7335', '12345678')
        while not sta_if.isconnected():
            pass
    print("WiFi conectado:", sta_if.ifconfig())

# Función de Publicador de MQTT
def publish(estado):
    client = MQTTClient(MQTT_CLIENT_ID, MQTT_BROKER, port=MQTT_PORT, user=MQTT_USER, password=MQTT_PASSWORD, keepalive=30)
    client.connect()
    print("[OK]")
    client.publish(MQTT_TOPIC_1, str(estado))
    print("Movimiento detectado:", estado)
    client.disconnect()

# Configuración para el funcionamiento del PIR
def handle_interrupt(pin):
    global motion
    motion = True
    


def publishGas(estado):
    client = MQTTClient(MQTT_CLIENT_ID, MQTT_BROKER, port=MQTT_PORT, user=MQTT_USER, password=MQTT_PASSWORD, keepalive=30)
    client.connect()
    print("[OK]")
    client.publish(MQTT_TOPIC_2, str(estado))
    print("Estado del aire:", estado)
    client.disconnect()

def leer_sensor():
    lectura = pin_sensor.value()
    if lectura == 1:
        pin_motor.value(1)
        print("Se detectó gas de hidrógeno")
        # Aquí puedes agregar las acciones que deseas realizar cuando se detecte el gas de hidrógeno
    else:
        pin_motor.value(0)
        print("No se detectó gas de hidrógeno")
    return lectura


# Función de Publicador  de MQTT
def publishTempHum(temp, hum):
    client = MQTTClient(MQTT_CLIENT_ID, MQTT_BROKER, port=MQTT_PORT, user=MQTT_USER, password=MQTT_PASSWORD, keepalive=30)
    client.connect()
    print("[OK]")
    client.publish(MQTT_TOPIC_3, str(temp))
    print("Publicando temperatura: ", temp, "ºC")

    client.publish(MQTT_TOPIC_4, str(hum))
    print("Publicando humedad: ", hum, "%")
    
def alerta_policia():
    for i in range(5):
        for i in range(n):
            neo_rojo[i] = (255, 0, 0)  # Establecer el LED i en rojo

        neo_rojo.write()

        time.sleep(0.6)  # Retardo de 0.5 segundos
        
        for i in range(n):
            neo_azul[i] = (0, 0, 255)  # Establecer el LED i en azul
        
        neo_azul.write()
        
        time.sleep(0.5)  # Retardo de 0.5 segundos
        
# Bucle principal

pir.irq(trigger=Pin.IRQ_RISING, handler=handle_interrupt)

# Programa principal
wifi_connect()
sensor = dht.DHT11(Pin(5))


while True:
    try:
        temp = sensor_temp()
        hum = sensor_hum()
        publishTempHum(temp, hum)
        time.sleep(4)
        valor = leer_sensor()
        publishGas(valor)
        if motion:
            print("Movimiento detectado")
            alerta_policia()
            publish(motion)
            print("Movimiento detenido")
            motion = False
    except Exception as e:
        print("Error:", e)
        wifi_connect()
con
