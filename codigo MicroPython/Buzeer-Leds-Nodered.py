import network
import time
from umqtt.simple import MQTTClient
from machine import Pin, PWM
from time import sleep
from dht import DHT11
import _thread  # Para multitarea

# Configuración WiFi
SSID = "Galaxy S22 Ultra"
PASSWORD = "Jp159000"

# Configuración del broker MQTT
BROKER = "broker.emqx.io"
TOPIC = b"gds0643/jdpz/main"

# Configuración del LED en el pin 32
led = Pin(32, Pin.OUT)

# Conexión WiFi
def connect_wifi():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(SSID, PASSWORD)
    while not wlan.isconnected():
        print("Conectando a WiFi...")
        time.sleep(1)
    print("Conectado:", wlan.ifconfig())

# Función para controlar el LED
def control_led(msg):
    if msg == b'1':
        led.on()
    elif msg == b'2':
        led.off()

# Función para cambiar la melodía
def control_buzzer(msg):
    if msg == b'true' or msg == b'false':
        change_melody(None)

# Callback para manejar mensajes MQTT
def sub_cb(topic, msg):
    print((topic, msg))
    control_led(msg)
    control_buzzer(msg)

# Conectar al broker MQTT
def connect_mqtt():
    client = MQTTClient("esp32_unique", BROKER)
    client.set_callback(sub_cb)
    try:
        client.connect()
    except Exception as e:
        print("Error conectando al broker:", e)
    client.subscribe(TOPIC)
    print(f"Conectado al broker {BROKER} y suscrito a {TOPIC}")
    return client

# Ejecutar el programa MQTT
def run_mqtt():
    try:
        connect_wifi()
        client = connect_mqtt()
        while True:
            client.check_msg()  # Revisa si hay mensajes
            time.sleep(1)
    except Exception as e:
        print("Error:", e)
    finally:
        try:
            client.disconnect()
        except Exception as e:
            print("Error al desconectar:", e)

# Configuración del buzzer
buzzer = PWM(Pin(27))  # Cambia el pin al que está conectado tu buzzer
button = Pin(14, Pin.IN, Pin.PULL_UP)  # Botón en el GPIO 14

# Configuración de LEDs
led1 = Pin(5, Pin.OUT)
led2 = Pin(18, Pin.OUT)
led3 = Pin(19, Pin.OUT)

# Configurar sensor DHT11 en el pin 25
dht_pin = Pin(25)
sensor = DHT11(dht_pin)

# Función para medir temperatura y humedad
def temperatura():
    while True:
        try:
            sensor.measure()
            t = sensor.temperature()
            h = sensor.humidity()
            print("Temperatura:", t, "C")
            print("Humedad:", h, "%")
            if t <= 20:
                led1.value(True)
                led2.value(False)
                led3.value(False)
            elif t <= 25:
                led1.value(False)
                led2.value(True)
                led3.value(False)
            else:
                led1.value(True)
                led2.value(True)
                led3.value(True)
                sleep(1)
                led1.value(False)
                led2.value(False)
                led3.value(False)
                sleep(1)
        except OSError as e:
            print("Error al leer el sensor:", e)
        sleep(1)

# Diccionario de frecuencias de las notas musicales (en Hz)
notes = {
    "B0": 31, "C1": 33, "D1": 37, "E1": 41, "F1": 44, "G1": 49, "A1": 55, "B1": 62,
    "C2": 65, "D2": 73, "E2": 82, "F2": 87, "G2": 98, "A2": 110, "B2": 123,
    "C3": 131, "D3": 147, "E3": 165, "F3": 175, "G3": 196, "A3": 220, "B3": 247,
    "C4": 262, "D4": 294, "E4": 330, "F4": 349, "G4": 392, "A4": 440, "B4": 494,
    "C5": 523, "D5": 587, "E5": 659, "F5": 698, "G5": 784, "A5": 880, "B5": 988,
    "C6": 1047, "D6": 1175, "E6": 1319, "F6": 1397, "G6": 1568, "A6": 1760, "B6": 1976,
    "C7": 2093, "D7": 2349, "E7": 2637, "F7": 2794, "G7": 3136, "A7": 3520, "B7": 3951,
    "C8": 4186, "D8": 4699, "E8": 5274, "F8": 5588, "G8": 6272, "A8": 7040, "B8": 7902
}

# Melodías navideñas
jingle_bells = [
    ("E4", 0.4), ("E4", 0.4), ("E4", 0.8),
    ("E4", 0.4), ("E4", 0.4), ("E4", 0.8),
    ("E4", 0.4), ("G4", 0.4), ("C4", 0.4), ("D4", 0.4), ("E4", 0.8),
    ("F4", 0.4), ("F4", 0.4), ("F4", 0.4), ("F4", 0.4),
    ("F4", 0.4), ("E4", 0.4), ("E4", 0.4), ("E4", 0.4),
    ("E4", 0.4), ("D4", 0.4), ("D4", 0.4), ("E4", 0.4), ("D4", 0.8), ("G4", 0.8)
]

we_wish_you = [
    ("G4", 0.4), ("A4", 0.4), ("G4", 0.4), ("E4", 0.8),
    ("G4", 0.4), ("A4", 0.4), ("G4", 0.4), ("E4", 0.8),
    ("C4", 0.4), ("D4", 0.4), ("E4", 0.4), ("F4", 0.4), ("E4", 0.4), ("C4", 0.8)
]

silent_night = [
    ("G4", 0.8), ("A4", 0.8), ("G4", 0.8), ("E4", 0.8),
    ("G4", 0.8), ("A4", 0.8), ("G4", 0.8), ("E4", 0.8),
    ("D4", 0.8), ("C4", 0.8), ("G4", 0.8), ("E4", 0.8),
    ("C4", 1.2)
]

feliz_navidad = [
    ("G4", 0.4), ("A4", 0.4), ("B4", 0.4), ("G4", 0.4), 
    ("G4", 0.4), ("A4", 0.4), ("B4", 0.4), ("G4", 0.4),
    ("C5", 0.4), ("C5", 0.4), ("B4", 0.4), ("A4", 0.4), 
    ("G4", 0.4), ("A4", 0.4), ("B4", 0.4), ("G4", 0.8),
    ("G4", 0.4), ("E4", 0.4), ("G4", 0.4), ("C5", 0.4), 
    ("C5", 0.4), ("B4", 0.4), ("A4", 0.4), ("G4", 1.2)
]

oh_christmas_tree = [
    ("C4", 0.4), ("E4", 0.4), ("G4", 0.8), ("G4", 0.4),
    ("A4", 0.4), ("A4", 0.4), ("G4", 0.8), ("F4", 0.4),
    ("E4", 0.4), ("E4", 0.4), ("D4", 0.4), ("D4", 0.4),
    ("C4", 0.8), ("G4", 0.4), ("C4", 0.8)
]

campanas_belen = [
    ("E4", 0.4), ("F4", 0.4), ("G4", 0.4), ("E4", 0.4),
    ("E4", 0.4), ("F4", 0.4), ("G4", 0.4), ("E4", 0.4),
    ("G4", 0.4), ("A4", 0.4), ("G4", 0.4), ("F4", 0.4),
    ("E4", 0.4), ("F4", 0.4), ("G4", 0.8),
    ("G4", 0.4), ("A4", 0.4), ("G4", 0.4), ("F4", 0.4),
    ("E4", 0.4), ("F4", 0.4), ("G4", 0.8)
]

silencio = []

# Lista de melodías
melodies = [jingle_bells, we_wish_you, silent_night, feliz_navidad, oh_christmas_tree, campanas_belen, silencio]
current_melody_index = 0  # Índice de la melodía actual
melody_change_requested = False  # Variable para indicar cambio de melodía

# Configuración del motor paso a paso
IN1 = Pin(15, Pin.OUT)
IN2 = Pin(2, Pin.OUT)
IN3 = Pin(4, Pin.OUT)
IN4 = Pin(16, Pin.OUT)
steps_per_revolution = 400
step_sequence = [
    [1, 0, 0, 0],
    [1, 1, 0, 0],
    [0, 1, 0, 0],
    [0, 1, 1, 0],
    [0, 0, 1, 0],
    [0, 0, 1, 1],
    [0, 0, 0, 1],
    [1, 0, 0, 1]
]

# Función para tocar una nota
def play_tone(note, duration):
    if note == " ":
        buzzer.duty(0)  # Silencio
    else:
        buzzer.freq(notes[note])
        buzzer.duty(512)  # Volumen medio
    sleep(duration)
    buzzer.duty(0)  # Apagar el buzzer
    sleep(0.05)

# Reproducir una melodía
def play_melody():
    global current_melody_index, melody_change_requested
    while True:
        melody = melodies[current_melody_index]
        for note, duration in melody:
            if melody_change_requested:
                melody_change_requested = False
                break
            play_tone(note, duration)

# Interrupción para cambiar de melodía
def change_melody(pin):
    global current_melody_index, melody_change_requested
    current_melody_index = (current_melody_index + 1) % len(melodies)
    melody_change_requested = True
    print(f"Cambiando a la melodía {current_melody_index + 1}")

button.irq(trigger=Pin.IRQ_FALLING, handler=change_melody)

# Motor paso a paso
def step_motor(steps, direction=1, delay=0.005):
    for _ in range(steps):
        for step in step_sequence[::direction]:
            IN1.value(step[0])
            IN2.value(step[1])
            IN3.value(step[2])
            IN4.value(step[3])
            sleep(delay)

def motor_task():
    while True:
        print("Motor: sentido horario")
        step_motor(steps_per_revolution, direction=1)
        sleep(1)
        print("Motor: sentido antihorario")
        step_motor(steps_per_revolution, direction=-1)
        sleep(1)

# Ejecutar tareas en paralelo
_thread.start_new_thread(play_melody, ())  # Melodías en un hilo
_thread.start_new_thread(motor_task, ())  # Motor en un hilo
_thread.start_new_thread(temperatura, ())  # Sensores en un hilo
_thread.start_new_thread(run_mqtt, ())  # MQTT en un hilo

# Mantener el programa principal corriendo
while True:
    sleep(1)  # Evita que el programa principal termine