
# TITULO
  Uso de IA para detección de comunicación de botnets y ataques de DDOS en un set de datos reducido.

# Resumen

  Los dispositivos embebidos en IOT conocidos como dispositivos IOT están más presentes en la cotidianidad de nuestras vidas, desde un bombillo inteligente hasta un sistema de cámaras. Los podemos ver en todas partes.
  
  La principal característica de estos dispositivos es su simplicidad esto debido a que tienen limitaciones de poder y de procesamiento.   Esto puede ser una ventaja en muchas formas, pero también son abiertas a problemas de seguridad, en este proyecto estudiaremos una solución usando machine learning para detectar ataques de tipo botnet los cuales pueden tomar posesión del dispositivo y desde el mismo crear ataques de tipo DDOS y otros.
  
  Un estudio anterior llamado "N-BaIoT: Network-based Detection of IoT Botnet Attacks Using Deep Autoencoders" ha demostrado una gran precisión con modelos como SVM, isolation forrest y otros, cuando se utiliza un dataset extenso de hasta 115 features.
  
  Los datos recolectados en este estudio utilizan una gran basta cantidad de características que facilitan el entrenamiento de los modelos, todos los modelos tienen una precisión muy alta, sin embargo al final del estudio se hace una pregunta fundamental:
  
  ¿Se podrá calificar cada uno de los features para saber cuáles son los que mejor ayudan en la precisión? Tratar de darle una nota a cada uno de los 115 features puede ser mucho para nuestra investigación sin embargo es una buena pregunta que queremos contestar, al menos parcialmente.
    
  En esta investigación analizaremos una característica principal de este dataset, las ventanas de tiempo usada en la obtención de datos, el dataset posee mediciones usando 5 ventanas de tiempo diferente, poder reducir al menos una de ellas significaría una reducción de 22 features en el dataset, nuestra meta es entender cuál es el impacto de usar diferentes ventanas de tiempo de nuestro modelo.

# Introducción


## Problema

Los Features en el dataset usado en la investigación "N-BaIoT: Network-based Detection of IoT Botnet Attacks Using Deep Autoencoders" fueron tomados de forma empírica y los modelos entrenados en dicho dataset muestran una alta precisión, sin embargo no hay una medición formal de que tanto afectan dichos features en la creación del modelo y si de verdad es necesario tener 115 de ellos.

## Pregunta de Investigación

   ¿Cuál es el impacto de usar diferentes ventanas de tiempo en la precisión de un modelo de machine learning para la detección de botnet en una red?

# Objetivos

## General
  Replicar el trabajo de investigación "N-BaIoT: Network-based Detection of IoT Botnet Attacks Using Deep Autoencoders" para comprender el impacto de los diferentes features del dataset en el entrenamiento de los modelos.
  Con el fin de comparar los resultados con diferentes ventanas de tiempo a la hora, las cuales son un feature importante en el dataset. 
  Concluir si el dataset actual de 115 features puede reducirse y brindar un impacto positivo en el tiempo de ejecucion con una perdida de precision aceptable.
  
## Especifico
  
### Examinar el dataset y los modelos usados de la investigacion previa
  Examinar y comprender los diferentes datasets relacionados a Botnets.
  Identificar los modelos usados para la deteccion de botnets y encontrar cual fue la metodologia a seguir.

### Replicar el modelo y obtener resultados semejantes
  Replicar las condiciones del experimento con alguno de los modelos, SVM,isolation forrest.
  Realizar el mismo entrenamiento pero solo con una ventana de tiempo en el dataset.

### Comparar y concluir los resultados
  Comparar los resultados de la precision y ejecucion del modelo con el dataset completo contra el dataset reducido.

# Metodología

## Dataset


Para la recolección de datos se usará el paper “N-BaIoT: Network-based Detection of IoT Botnet Attacks Using Deep Autoencoders” en el cual usando diferentes dispositivos se tomaron datos estando infectado, y limpios

En este data set podemos encontrar hasta 115 features, por dispositivo, se tiene 23 features unicos, se recolectaron 4 tipos de flujos diferentes y se usan 5 ventanas de tiempo diferentes.


La lista de features se compone de la siguiente manera:

|Value| Statistic| Aggregated by| Total Number of Features|
|-----|----------|--------------|-------------------------|
|Packet size (of outbound packets only)| Mean, Variance| Source IP, Source MAC-IP, Channel, Socket| 8|
|Packet count| Number| Source IP, Source MAC-IP, Channel, Socket| 4|
|Packet jitter (the amount of time between packet arrivals)| Mean, Variance, Number| Channel| 3|
|Packet size (of both inbound and outbound together)|Magnitude, Radius, Covariance,Correlation coefficient| Channel, Socket| 8|
||

```
Source IP: es el ip del host
Source Mac-IP: es la direccion del gateway.
Los sockets son determinados por el dispositivo de origen y el puerto de destino ya sea de TCP o UDP, por ejemplo trafico enviado de 192.168.1.12:1234 hacia 192.168.1.50:80
```


Los 4 flujos que se toman son los siguientes\
H: Trafico desde un host (IP)\
MI: Trafico desde un Mac-IP\
HpHp: trafico desde un host port a otro host port\
HH_jit: trafico jitter desde un host port a otro host port\

Ademas se toman datos con 5 ventanas de tiempo diferentes.\
L5: 1min\
L3: 10sec\
L1: 1.5sec\
L0.1: 500ms\
L0.01: 100ms

Los diferentes tipos de ataques en este dataset son:

Para el Bashlite attack:

• Flujo de Scan: es el flujo de escaneo del botnet buscando vulnerabilidades

• Junk: Un ataque donde se envía información de spam

• UDP:  el Ataque DDOS usando el protocolo UDP

• TCP: el ataque DDOS usando el protocolo TCP

• COMBO: que es el envío de spam y abriendo conexiones a direcciones IPs y puertos

Estas comunicaciones se guardan en diferentes archivos CSV con algunos features extras que discutiremos más adelante
 

Para el ataque mirai se usa obtiene algo parecido

• Flujo de Scan: es el flujo de escaneo del botnet buscando vulnerabilidades

• UDP:  el Ataque DDOS usando el protocolo UDP

• Ack:  el Ataque DDOS usando la bandera de  ACK

• Syn:  el Ataque DDOS usando la bandera de  Syn

• UDPplain: un tipo de ataque DDOS por protocolo UDP con menos datos, pero mayor cantidad de package per seconds

Para los demás flujos benignos se guardan todos en una csv y contienen comunicaciones normales de los dispositivos
 

## Labels.

  Iniciamos con el labels de maligno el cual será 0 para cualquiera de los ataques antes mencionados o 1 cuando es un proceso normal del dispositivo

## Modelo.

  Para el modelo se propone utilizar uno que tenga una ejecucion y entrenamiento rapido ya que se necesita correr con diferentes datasets.\
  Este puede ser supervisado y dados los datos podemos asumir que para la clasificacion entre maligno y benigno podemos utilizar algoritmos sencillos como SVM.
  
## Ejecución.
  Replicando las mismas condiciones lo mas exacto posible se entrenar un modelos de SVM con el dataset completo.\
  Se repite el proceso pero solamente se usa el dataset con una ventana de tiempo para cada una de las 5 ventanas.\
  Se propone ejecutar una muestra en un computador personal, pero con ayuda de cuda podríamos ejecutar todos los datos en el servidor de la maestría de la ECCI.
  Cada ejecucion debe poseer un diagrama de Fisher asi como su tiempo de ejecucion.


# Referencias

Yair Meidan, Michael Bohadana, Yael Mathov, Yisroel Mirsky,
Dominik Breitenbacher, Asaf Shabtai, and Yuval Elovici, "N-BaIoT: Network-based Detection
of IoT Botnet Attacks
Using Deep Autoencoders", IEEE PERVASIVE COMPUTING, VOL. 13, NO. 9, JULY-SEPTEMBER 2018 


https://towardsdatascience.com/do-you-know-how-to-choose-the-right-machine-learning-algorithm-among-7-different-types-295d0b0c7f60
