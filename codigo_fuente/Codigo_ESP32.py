import time
import network
from umqtt.simple import MQTTClient
from machine import Pin
import machine
import dht
import neopixel

#Pines de sonido
pin_analogo = machine.ADC(machine.Pin(32))  # Cambia el número de pin según corresponda
pin_digital = machine.ADC(machine.Pin(33))  # Cambiado a pin 27

#Pin de fotoResistencia
digital_resistencia_pin = machine.ADC(machine.Pin(34))  # Cambiado a pin 27

# Configurar el pin del zumbador o altavoz como PWM
buzzer_pin = machine.PWM(machine.Pin(22))

# Pines y variables para PIR.
motion = False
led = Pin(4, Pin.OUT)
pir = Pin(18, Pin.IN)
#buzzer= Pin(23, Pin.OUT)

# Configuración del pin del sensor MQ-2
pin_sensor = Pin(35, Pin.IN)

# Motor
pin_motor = Pin(27, Pin.OUT)
#LED RGB
#neo_rojo = neopixel.NeoPixel(Pin(23), 256)
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
MQTT_TOPIC_5 = "utng/sonido"
MQTT_TOPIC_6 = "utng/fotoresistencia"
MQTT_TOPIC_6 = "sd/ventilador"


MQTT_PORT = 1883


#Medicion de temperatura y humedad
def sensor_temp():
    sensor.measure()
    temp = sensor.temperature()
    if temp >= 35:
        publish_tem(1)
    elif temp >= 30:
        publish_tem(2)
    elif temp >= 26:
        publish_tem(3)
    else:
        publish_tem(0)
    print("temperatura",temp)
    return round(temp,1)

# Medición de Humedad
def sensor_hum():
    hum = sensor.humidity()
    print("humedad",hum)
    print(hum)
    return round(hum, 1)

# Función para reproducir un tono
def play_tone(frequency, duration):
    buzzer_pin.freq(frequency)
    buzzer_pin.duty(512)
    time.sleep(duration)
    buzzer_pin.duty(0)

def sensor_sound():
     # Lee el valor analógico del sensor
    analog_value = pin_analogo.read_u16() // 10

    # Lee el valor digital del sensor (lectura analógica para pines digitales también)
    digital_value = pin_digital.read_u16() // 10

    time.sleep(1)  # Espera 1 segund
    
    return str(digital_value)

def sensor_foto_resistencia():
    # Lee el valor digital del sensor (lectura analógica para pines digitales también)
    digital_value = digital_resistencia_pin.read() 
    # Imprime los valores
    print("Valor digital:", digital_value)
    if digital_value >=4000:
        led.value(1)
    else:
        led.value(0)
    time.sleep(1)  # Espera 1 segund
    
    return str(digital_value)


# Función para conectar al WiFi
def wifi_connect():
    print("Conectando al WiFi...")
    sta_if = network.WLAN(network.STA_IF)
    sta_if.active(True)
    
    if not sta_if.isconnected():
        sta_if.connect('POCO X3 Pro', '12345678')
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
        play_tone(1000, 0.5)  # Reproducir un tono de 1000 Hz durante 0.5 segundos
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
    
def publishSound(sound):
    client = MQTTClient(MQTT_CLIENT_ID, MQTT_BROKER, port=MQTT_PORT, user=MQTT_USER, password=MQTT_PASSWORD, keepalive=30)
    client.connect()
    print("[OK]")
    client.publish(MQTT_TOPIC_5, str(sound))
    print("Sonido:", sound)
    client.disconnect()

def publishFotoResistencia(foto_resistencia):
    client = MQTTClient(MQTT_CLIENT_ID, MQTT_BROKER, port=MQTT_PORT, user=MQTT_USER, password=MQTT_PASSWORD, keepalive=30)
    client.connect()
    print("[OK]")
    client.publish(MQTT_TOPIC_6, str(foto_resistencia))
    print("FotoResistencia:", foto_resistencia)
    client.disconnect() 

#Controlar ventilador
def publish_tem(estado):
    client = MQTTClient(MQTT_CLIENT_ID, MQTT_BROKER, port=MQTT_PORT, user=MQTT_USER, password=MQTT_PASSWORD, keepalive=30)
    client.connect()
    print("[OK]")
    client.publish(MQTT_TOPIC_6, str(estado))
    print("Ventilador a:", estado)
    client.disconnect()
    
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

play_tone(0, 0.5)

# Programa principal
wifi_connect()
#Temperatura y Humedad
sensor = dht.DHT11(Pin(5))

  
while True:
    try:
        temp = sensor_temp()
        hum = sensor_hum()
        publishTempHum(temp, hum)
        #time.sleep(4)
        valor = leer_sensor()
        publishGas(valor)
        sound = sensor_sound()
        print("Sonido",sound)
        foto_resistencia = sensor_foto_resistencia()
        print("Valor foto_resistencia",foto_resistencia)
        if motion:
            print("Movimiento detectado")
            play_tone(1000, 0.5)
            #alerta_policia()
            #publish(motion)
            print("Movimiento detenido")
            motion = False
    except Exception as e:
        print("Error:", e)
        #wifi_connect()
con