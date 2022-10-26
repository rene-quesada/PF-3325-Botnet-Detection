
# TITULO
  Detección de ataques de botnets usando aprendizado automatico en un conjunto de datos dado.
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

   ¿Cuál es el impacto de las diferentes caracteristicas en un conjunto de datos en la precisión de un modelo de machine learning para la detección de botnet en una red?

# Objetivos

## General
  Evaluar el impacto de diferentes caracteristicas del conjunto de datos en el entrenamiento de los modelos.
  Medir la precision del modelo para diferentes caracteristicas y comparar los resultados.
  
## Especifico

  Construir un clasificador con todas las caracteristicas del conjunto de datos.
  
  Entrenar el clasificador solo con caracteristicas claves del conjunto de datos.

  Medir el impacto en la precision, eficiencia y tiempos de desempeño.

  Comparar el impacto de las caracteristicas claves en los resultados.

# Metodología

## Dataset



Para la recolección de datos se usará el paper “N-BaIoT: Network-based Detection of IoT Botnet Attacks Using Deep Autoencoders” en el cual usando diferentes dispositivos se tomaron datos estando infectado, y limpios

En este data set podemos encontrar hasta 115 features, por dispositivo, se tiene 23 features únicos, se recolectaron 4 tipos de flujos diferentes y se usan 5 ventanas de tiempo diferentes.

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
Source Mac-IP: es la dirección del gateway.
Los sockets son determinados por el dispositivo de origen y el puerto de destino ya sea de TCP o UDP, por ejemplo tráfico enviado de 192.168.1.12:1234 hacia 192.168.1.50:80
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

  Para el modelo se propone utilizar uno que tenga una ejecución y entrenamiento rápido ya que se necesita correr con diferentes datasets.\
  Este puede ser supervisado y dados los datos podemos asumir que para la clasificación entre maligno y benigno podemos utilizar algoritmos sencillos como SVM.
  
## Ejecución.
  Replicando las mismas condiciones lo más exacto posible se entrenar un modelo de SVM con el dataset completo.\
  Se repite el proceso pero solamente se usa el dataset con una ventana de tiempo para cada una de las 5 ventanas.\
  Se propone ejecutar una muestra en un computador personal, pero con ayuda de cuda podríamos ejecutar todos los datos en el servidor de la maestría de la ECCI.
  Cada ejecución debe poseer un diagrama de Fisher así como su tiempo de ejecución.

# Referencias

Yair Meidan, Michael Bohadana, Yael Mathov, Yisroel Mirsky,
Dominik Breitenbacher, Asaf Shabtai, and Yuval Elovici, "N-BaIoT: Network-based Detection
of IoT Botnet Attacks
Using Deep Autoencoders", IEEE PERVASIVE COMPUTING, VOL. 13, NO. 9, JULY-SEPTEMBER 2018 

https://towardsdatascience.com/do-you-know-how-to-choose-the-right-machine-learning-algorithm-among-7-different-types-295d0b0c7f60


