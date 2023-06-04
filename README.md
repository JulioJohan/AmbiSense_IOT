# AmbiSense
<!-- Subtitulo -->
## Objetivo del proyecto
El objetivo principal del proyecto de Sistema de Monitoreo Ambiental es diseñar y desarrollar un sistema que permita a los usuarios monitorear y controlar los diferentes parámetros ambientales en la oficina de manera eficiente y conveniente. El proyecto busca crear un entorno más saludable y confortable para los ocupantes, al tiempo que promueve la eficiencia energética y la sostenibilidad.

##Beneficiario
Empresa ITTIVA (Isamar Ríos Bocanegra)

## Integrantes
- David Enrique Lopez Juarez
- Julio Johan Jaramillo Mejia
- Alejandro Rafael Guerrero Lozano
- Itzel Juliza Guerrero Rodriguez

<!--Componentes electricos-->
## Hardware
| Num.| Componente | Descripción | Imagen | Costo | Cantidad |
|-----|------------|-------------|--------|-------|----------|
|  1  | Sensor de temperatura y de humedad (ambos) (DHT11) |Mide la temperatura del entorno	|<img src="https://cdn.shopify.com/s/files/1/1040/8806/products/photo_IC-20010_DHT11_DigitalTemperatureHumiditySensor_DHT11_01_700x700.png?v=1627344523" width="200px">|  $62.16 | 2
|  2  | Sensor de gas	(MQ-2) |Detecta la presencia de gases		|<img src="https://uelectronics.com/wp-content/uploads/AR0221_MQ5-2-2.jpg" width="200px">|  $63.20 | 2
|  3  | Sensor de movimiento	(PIR) | Detecta el movimiento en un área			|<img src="https://epyelectronica.com/wp-content/uploads/2020/09/Sensor-de-Movimiento-PIR-HC-SR501.png" width="200px">|  $49.99 | 2
|  4  | Sensor de sonido	(KY-038)| Detecta el nivel de sonido en el entorno	|<img src="https://aelectronics.com.mx/metepec/14-thickbox_default/sensor-de-sonido-modulo.jpg" width="200px">|  $54.32 | 1
|  5  | Sensor de luz (LDR) | Detecta el nivel de luz que llega el entorno donde se instala| <img src="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Falltopnotch.co.uk%2Fwp-content%2Fuploads%2Fimported%2F4%2FLDR-Photoresistor-Light-Detection-Sensor-Module-Dependent-Resistor-Arduino-PIC-362145909694-3.JPG&f=1&nofb=1&ipt=af7dcf6ccfd78be6e179b256ead52b857ef81326e18d09c3f71ff85addf5cbdd&ipo=images" width="200px">  | $50.00 | 1 |
|  6  | Pulsador | Botón para encender el circuito | <img src="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fmundoelectronica.es%2Fwp-content%2Fuploads%2F2019%2F11%2F0005142_pulsador-12x12x6mm-5uds.jpeg&f=1&nofb=1&ipt=f9093726acfacaaa522536ae6193169ff18d7711e48c0e6e944417f3c8a7f4da&ipo=images" width="200px"> | $15.00 | 1 |
|  7  | Esp32 | Microcontrolador necesario para programar | <img src="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2F2.bp.blogspot.com%2F-ClnQs3RcnZ0%2FW0azbQRZ4lI%2FAAAAAAAACXQ%2F9ufe7ojc5D8yBZkDld0C_yvu094xClgLwCLcBGAs%2Fs1600%2Fesp32-main-board-with-wifi-and-bluetoothImageMain-900.jpg&f=1&nofb=1&ipt=1a013d506f5d160dfce6532648d6089020dc56eb80385c9517605d0bede06b5e&ipo=images" width="200px">| $152.83| 1 |
|  8  | Diodo led | Indicador del estado del circuito |<img src="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fi5.walmartimages.com%2Fasr%2F467a1c06-c707-43bd-9dd6-f2bde50086d6_1.46be4bbbeaa72e5d1ce6fceb8eb4fa7a.jpeg&f=1&nofb=1&ipt=acb4025ae62aaae1ef372f43b6a372b16217627968395110b1c392b945c711aa&ipo=images" width="200px">|$3.00|3|
|  9  | Buzzer | Bocina que indica cuando se detectan anomalias |<img src="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fpotentiallabs.com%2Fcart%2Fimage%2Fcache%2Fcatalog%2Fbuzzer-800x800.jpg&f=1&nofb=1&ipt=3b56cdb0fcfd01d8d7c1e0bf65a5e3c6d7356cdd065e45e56835d1ae0bdce3d6&ipo=images" width="200px">|$39.00|1|
|  10 | Resistencia | Dispositivo necesario para proteger los componentes electronicos |<img src="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Flaelectronica.com.gt%2Fimage%2Fcache%2Fcatalog%2FProductos%2FResistencias%2Fr12w-800x800.jpeg&f=1&nofb=1&ipt=955a09c07ce6ef6ad656b09f4e71e42f38c3dc55e9c959f9f158379187ec3bd0&ipo=images" width="200px">|$13.00|6|
|  11 | Placa fenolica | Componente donde se soldaran el circuito |<img src="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fcdn.shopify.com%2Fs%2Ffiles%2F1%2F0409%2F9041%2Fproducts%2F44_342e822f-be1e-4c04-948f-158b45932f71_1024x1024.jpg%3Fv%3D1571438837&f=1&nofb=1&ipt=be442d7ef34966e3e8c0c9fb7c8b6e6973b87a89313ab0632c83a8a8ce2d723e&ipo=images" width="200px">| $45.00 |1|
|12|Raspberry Pi 4|Microcomputador reciente|<img src="https://m.media-amazon.com/images/I/41cn6diLE0L.jpg" width="200px">|$2500.00|1| 
|13|ESP32 LVGL|ESP32 con pantalla táctial integrada|<img src="https://ae01.alicdn.com/kf/S6217779f602244088b8e2fda5f6c97f5v/Placa-de-desarrollo-ESP32-Arduino-LVGL-WIFI-y-Bluetooth-pantalla-de-3-5-pulgadas-320x480-IPS.jpg_Q90.jpg_.webp" width="200px">|$168.53|1| 



## Tabla de Software utilizado
| Id | Software | Version | Tipo |
|----|----------|---------|------|
| SF01 | Node- Red | v3.0.2 |  Software    |
| SF02 | MQTT | v3.1.0 |   Libreria  |
| SF03 | Python | v3.9.5 |   Lenguaje de programación  |
| SF04 | Tinkercad | Actual |   Software  |
| SF05 | Fritzing | v0.9.3 |   Software  |


## Tabla de historias de usuario
| Id | Historia de usuario | Prioridad | Estimación | Como probarlo | Responsable |
|----|---------------------|-----------|------------|---------------|-------------|
|HU001| Como usuario, quiero poder monitorear la temperatura ambiente del espacio de trabajo de mis empleados en tiempo real para ajustar la climatización de manera eficiente y asegurar el confort de mis empleados| Debe | 4 | El usuario entra en LVGL dentro de la aplicación para poder navegar y monitorer la temperatura |  Julio Johan Jaramillo Mejia |
| HU002   |  Como usuario, quiero poder supervisar la humedad relativa del aire del espacio de trabajo de mis empleados para controlar y evitar problemas de humedad, como el moho y la condensación excesiva.  |    Debe   |   4   | El usuario entra en LVGL dentro de la aplicación para poder navegar y monitorer la humedad |  Itzel Juliza Guerrero Rodriguez  |
| HU003 | Como usuario, quiero ser alertado inmediatamente si se detecta una fuga de gas o una concentración peligrosa del espacio de trabajo, para tomar medidas de seguridad y evitar accidentes.  |  Debe |   4   |  El usuario entra en LVGL dentro de la aplicación para poder navegar y checar si hay una fuga | David Enrique Lopez Juarez |
| HU004 | Como usuario, quiero recibir alertas cuando se detecte movimiento en áreas específicas  del espacio de trabajo  mientras estoy ausente, para tomar medidas de seguridad y precaución. |  Debe |   4   |  El usuario entra en LVGL dentro de la aplicación para poder navegar y checar si hay un excesivo de movimiento |  Alejandro Rafael Guerrero Lozano |
| HU005 | Como usuario, quiero supervisar los niveles de ruido  del espacio de trabajo de mis empleados para evaluar el ambiente sonoro y tomar acciones para reducir el ruido excesivo o identificar situaciones inusuales. Ademas de tener un control con los empleados|  Debe |   4   |  El usuario entra en LVGL dentro de la aplicación para poder navegar y checar si existe un ruedo excesivo |  David Enrique Lopez Juarez |
| HU006 | Como usuario, quiero supervisar los niveles de luz del espacio de trabajo de mis empleados.|  Debe |   4   |  El usuario entra en LVGL dentro de la aplicación para poder navegar y checar los niveles de luz |  Alejandro Rafael Guerrero Lozano |

## Prototipo en dibujo
![Carcasa del dispositivo para monitorear](https://github.com/JulioJohan/Social_Hub_IOT/blob/main/59b66046-de32-4683-b355-f47a140f9e83.jpeg)
![Carcasa del dispositivo para monitorear medidas](https://github.com/JulioJohan/Social_Hub_IOT/blob/main/324cf8b0-4d27-4943-ab37-0e067d3ed931.jpeg)
![Carcasa del dispositivo del smarwatch ](https://github.com/JulioJohan/Social_Hub_IOT/blob/main/d1cdfbf2-3c57-4323-a2b8-95e6568c3d88.jpeg)

## Prototipo en Fritzing 
![image](https://github.com/JulioJohan/Social_Hub_IOT/assets/92689016/83f0b4f8-b656-4159-823b-e841490cf50c)
Archivo para importa a Fritzing
https://drive.google.com/file/d/1hTj0Yit1YV8chYnKZ-L4cELiSmPzCCmE/view?usp=sharing
## Placa PCB
![image](https://github.com/JulioJohan/Social_Hub_IOT/assets/92689016/f1482343-17b9-444a-ac60-fee20b4c01d9)
![image](https://github.com/JulioJohan/Social_Hub_IOT/assets/92689016/5de45c54-2eb1-4dfe-a9df-51f6a97b9d83)
![image](https://github.com/JulioJohan/Social_Hub_IOT/assets/92689016/a8f1ee7b-cd9f-4f3d-9161-c0d63a9c7184)

Archivo para importa a Fritzing
https://drive.google.com/file/d/1hTj0Yit1YV8chYnKZ-L4cELiSmPzCCmE/view?usp=sharing

## Prototipo en 3D

![Carcasa del dispositivo para monitorear 3D](https://github.com/JulioJohan/Social_Hub_IOT/blob/main/c4a88b76-bfaf-43d6-9086-7c03bc590762.jpeg)
![Carcasa del dispositivo para smarwatch 3D](https://github.com/JulioJohan/Social_Hub_IOT/blob/main/62b0dfc3-ee43-4020-9fa4-9f2033622546.jpeg)

Archivos para importar en tinkercard
https://drive.google.com/drive/folders/17Y6I6Qh2MGuPxudXHm-QEi41wmYJhm28?usp=sharing
