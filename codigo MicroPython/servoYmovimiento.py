from machine import Pin, PWM
from time import sleep

# Configurar el sensor PIR
pir_sensor = Pin(13, Pin.IN)

#configurar leds
led1=Pin(12,Pin.OUT)
led2=Pin(14,Pin.OUT)
led3=Pin(27,Pin.OUT)

# Configurar los pines de los servos
servo_pin = PWM(Pin(15), freq=50)  # Servo principal
servo_pinizq = PWM(Pin(2), freq=50)  # Servo izquierdo
servo_pinder = PWM(Pin(4), freq=50)  # Servo derecho

# Función para mover los servos a un ángulo específico
def move_servo(servo, angle):
    min_duty = 26   # Corresponde a 0 grados 
    max_duty = 127  # Corresponde a 180 grados 
    
    # Calcular el ciclo de trabajo según el ángulo deseado
    duty = int(min_duty + (angle / 180) * (max_duty - min_duty))
    servo.duty(duty)

# Bucle principal
while True:
    if pir_sensor.value():  # Detecta movimiento
        print("Movimiento detectado. Moviendo servos...")
        led1.value(True)
        led2.value(True)
        led3.value(True)
        # Mover los servos
        move_servo(servo_pin, 0)      # Servo principal a 0°
        move_servo(servo_pinizq, 0)  # Servo izquierdo a 180°
        move_servo(servo_pinder, 180)  # Servo derecho a 90°
        sleep(2)  # Mantener la posición por 2 segundos

        # Regresar los servos a la posición inicial
        move_servo(servo_pin, 90)      # Servo principal a 90°
        move_servo(servo_pinizq, 90)   # Servo izquierdo a 90°
        move_servo(servo_pinder, 90)    # Servo derecho a 0°
        sleep(2)  # Mantener la posición por 2 segundos
    else:
        led1.value(False)
        led2.value(False)
        led3.value(False)
        print("Sin movimiento detectado.")
        sleep(0.1)  # Esperar un momento antes de volver a comprobar
