# 🎄 Proyecto Navideño IoT (Dr.Finkelstein)

## Descripción
El proyecto navideño que se propone integra diversas tecnologías de Internet de las Cosas (IoT) mediante el uso de dos microcontroladores ESP32, los cuales se encargarán de controlar luces LED, sonido, movimiento y sensores. Este sistema no solo busca embellecer el ambiente festivo, sino también ofrecer una experiencia interactiva y automatizada.

## Integrantes
- Juan Diego Pardo Zamarripa
- Carlos Samael Aguayo Santana
- Grupo: GDS0643

## Características Técnicas

### 💡 Sistema de Iluminación
- LEDs controlados por la temperatura del ambiente
- Patrones de iluminación
- Control mediante Node-RED

### 🔊 Sistema de Sonido
- Buzzer integrado
- Reproducción de melodías navideñas

### ⚙️ Sistema de Movimiento
- Servomotores
- Motores paso a paso
- Sincronización con luces y sonido

### 📡 Control Remoto
- Implementación con Node-RED
- Protocolo MQTT

### 🔍 Sensores
- Sensor de movimiento
- Sensor de temperatura

## Materiales Utilizados
| Nombre del Componente | Descripción | Cantidad | Precio Total |
|-----------------------|-------------|----------|--------------|
| ESP32                 | El ESP32 es un microcontrolador de bajo costo y bajo consumo de energía que se utiliza comúnmente en proyectos de Internet de las cosas (IoT) y desarrollo de hardware. | 2 | $150.00 |
| Cables Dupont         | Los cables Dupont son un tipo de cable utilizado comúnmente en electrónica y robótica para conectar componentes y dispositivos. Estos cables suelen tener conectores de tipo macho y hembra que se acoplan fácilmente, lo que facilita la conexión y desconexión de componentes en prototipos y proyectos. | Muchos | $100.00 |
| LEDs                  | Los LED (diodos emisores de luz) son dispositivos electrónicos que emiten luz cuando una corriente eléctrica pasa a través de ellos. | Muchos | $100.00 |
| Servomotor            | Es un tipo de motor eléctrico que se utiliza para controlar con precisión la posición, la velocidad y la aceleración de un sistema mecánico. | 1 | $70.00 |
| Motor a pasos         | El motor paso a paso es un motor de corriente continua sin escobillas en el que la rotación se divide en un cierto número de pasos resultantes de la estructura del motor. Normalmente, una revolución completa del eje de 360° se divide en 200 pasos, lo que significa que se realiza una sola carrera del eje cada 1,8°. | 1 | $58.00 |
| Protoboard            | Es una herramienta simple que se usa en proyectos de robótica que permite conectar fácilmente componentes electrónicos entre sí, sin necesidad de realizar una soldadura. | 2 | $80.00 |
| Serie de LEDs         | Una pequeña serie de luces LED que reciben corriente mediante cables Dupont. | 1 | $10.00 |
| Buzzer                | Un zumbador (en inglés buzzer) es un transductor electroacústico que produce un sonido o zumbido continuo o intermitente de un mismo tono (generalmente agudo). | 2 | $20.00 |
| Sensor de movimiento  | Un sensor de presencia o sensor de movimiento es un dispositivo electrónico que pone en funcionamiento un sistema (encendido o apagado) cuando detecta movimiento en el área o ambiente en el que está instalado. | 1 | $50.00 |
| Bola de unicel        | Las bolas de unicel la usamos como la cabezas del personaje. | 1 | $10.00 |
|foami moldeable        |foami moldeable para hacer las manos y narices. | 5 paquetitos de foami moldeable | $120.00 |
| Resistol, silicón, cinta | Los usamos para pegar los materiales. | Varios | $50.00 |
| Pintura               | Usamos pintura para pintar las cabezas, manos y otras cosas. | 2 | $40.00 |

## Software Utilizado
| Nombre de Software | Versión | Tipo |
|--------------------|---------|------|
| Thonny             | Reciente| Editor |
| Node-RED           | Reciente| Conexión WiFi |


### Código Fuente
- `/codigo MicroPython/Buzzer-Leds-Nodered.py` - Código MicroPython (control de LEDs, sensor de temperatura, Node-RED, motor de pasos)
- `/codigo MicroPython/Control-Articulaciones-Servomotores.py` - Código MicroPython (control de las articulaciones, servomotores)
- `/Node-red/flows (1) (1).json` - Flujos de Node-RED

## Evidencias
### 📸 Imágenes del Proyecto
![image](https://github.com/user-attachments/assets/adc0ea1c-fdd9-4844-8cf2-abfdaa4b92d4)
![image](https://github.com/user-attachments/assets/5b102b30-8f62-4dd8-a3a2-ebf468056b29)
![image](https://github.com/user-attachments/assets/dd6df926-5d12-418d-a782-7193c20475cc)
![image](https://github.com/user-attachments/assets/697538bc-f426-4cc6-b782-b7d8a6972a3e)

### 🎥 Video Demostrativo
[https://youtu.be/MvWyDBvwN9Q]

### 📱 TikTok Promocional
[Enlace al TikTok](https://vm.tiktok.com/ZMkdtPQNb/)

### 📱 Instagram Reels
[Enlace al Instagram Reels](https://www.instagram.com/reel/DDKqrYuJevt/?igsh=ZW1qYngxczUyaDI2)

### 📜 Certificaciones
- Certificado JavaScript NetAcad
  - Capítulo 1
    ![image](https://github.com/user-attachments/assets/698c7110-d1dd-4da7-a0da-9d75405301af)
  - Capítulo 2
    ![image](https://github.com/user-attachments/assets/a52db099-6d6a-4d1d-af59-4c04731553be)
  - Capítulo 3
    ![image](https://github.com/user-attachments/assets/c5dddfca-f713-4f7d-8d9d-401840949b3e)
  - Capítulo 4
    ![image](https://github.com/user-attachments/assets/d1b1baed-a243-43d8-890a-e5c09a56c7a8)
  - Capítulo 5
    ![image](https://github.com/user-attachments/assets/ca6cae0b-bd74-4ea4-a50b-3e237bcb0567)
  - Capítulo 6
    ![image](https://github.com/user-attachments/assets/390ff04c-3e03-46a8-aa39-38576e97aed9)
  - Examen final
    ![image](https://github.com/user-attachments/assets/f88c7eb3-c71c-4ff6-a55f-720589603c28)

## Demostración
El proyecto estará en exhibición durante 3 días en el área de TI, demostrando todas las funcionalidades mencionadas.

## Coevaluación
### Evaluación Para Carlos Samael Aguayo Santana
- **Participación:** [Descripción de la participación de Carlos Samael]
- **Contribuciones Técnicas:** [Descripción de las contribuciones técnicas de Carlos Samael]
- **Trabajo en Equipo:** [Descripción del trabajo en equipo de Carlos Samael]
- **Puntaje General:** [Puntaje de 1 a 10]

---

Desarrollado para la materia Principios de IoT
