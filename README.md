
# TITULO
  Impacto de variables en la detección de ataques DDOS provenientes de botnets Miria y bashlite usando aprendizaje automático.
# Resumen

  Un estudio anterior titulado "N-BaIoT: Network-based Detection of IoT Botnet Attacks Using Deep Autoencoders" ha demostrado que los clasificadores de aprendizaje automático para detectar flujo maligno o benigno en varios dispositivos embebidos posee una gran precisión y eficiencia, esto utilizando un conjunto de datos extenso de hasta 115 features.
  Como conclusión de la investigación mencionada al final del estudio se hace una pregunta fundamental:
  
  ¿Se podrá calificar cada uno de los features para saber cuáles son los que mejor ayudan en la precisión?
  
  Mas alla de tratar de darle una nota a cada uno de los 115 variables el enfoque de este trabajo es de analizar el impacto de las varaibles de un conjunto de datos, en la construcción del modelo y de la detección de ataques de botnets.
  
  ----si las ventanas de tiempo es la característica a analizar----
  En esta investigación analizaremos una característica importante de este conjunto de datos el cual son las ventanas de tiempo usada en la obtención de datos, los cuales poseen mediciones usando 5 ventanas de tiempo diferente.
  
  se concluye que....

# Introducción

   La proliferación de dispositivos de embebidos conectados a la Red ha ido en aumento en los últimos años, y con ello el aumento de ataques hacia y desde estos dispositivos.   Las formas más conocidas de infectar estos dispositivos son mediante el uso de botnets, estos son capaces de controlar estos dispositivos y causar ataques distribuidos de denegación de servicio a cualquier IP deseada por el botnet.
   
   Debido a este nuevo tipo de amenazas muchos han empezado a usar con éxito aprendizaje automático para la detección de botnet y entre los más populares son la deteccion de botnets Mirai y Bashlite. Sin embargo como algunas investigaciones apuntan la selección de las variables del conjunto de datos se toman de una forma empírica.
   
   La motivación de este trabajo es analizar el impacto de las variables usadas en la detección de los ataques de negación de servicios, mediante el uso de aprendizaje automático y la construcción de modelos con cada una de las 115 variables utilizadas.


## Problema

Las variables en el conjunto de datos usado en la investigación "N-BaIoT: Network-based Detection of IoT Botnet Attacks Using Deep Autoencoders" fueron tomados de forma empírica y los modelos entrenados en dicho dataset muestran una alta precisión, sin embargo no hay una medición formal que nos indique que tanto afectan las variables en la creación del modelo y si de verdad es necesario tener 115 de ellos.

## Pregunta de Investigación

   ¿Cuál es el impacto de las diferentes características en un conjunto de datos en la precisión de un modelo de machine learning para la detección de botnet en una red?

# Objetivos

## General
  Evaluar el impacto de diferentes características del conjunto de datos en la construcción y desempeño de un clasificador.
  
## Especifico
  
  Revisión de literatura
  
  Construir un clasificador las distintas variables del conjunto de datos.
  
  Medir el impacto en la precisión, eficiencia.

  Comparar el impacto de las características claves en los resultados.


# Marco Conceptual
## Comunicaciones IOT
A diferencia de un computador un dispositivo de IOT no realiza múltiples tareas, usualmente está programado para llevar a cabo una sola tarea, por lo que sus comunicaciones son más limitadas y posee menos características en sus encabezados.

Muchos de los dispositivos usan comunicaciones en tiempo real, por ejemplo una cámara de video, un dispositivo de comunicación como Alexa, un monitor de bebe, etc. por lo que mantener una comunicación compleja como en TCP donde los paquetes pueden llegar en desorden y hay controles para asegurarnos que toda la información llega se convierte en un exceso que causaría un retraso en una señal de tiempo real.

Los dispositivos IOT tienden a usar UDP para comunicarse ya que ocupa menos recursos, consume menos potencia y que permiten perdidas de paquetes este tipo de redes se le denomina por su nombre en inglés como LLNs (Low power, Lossy Networks)

 
### Caracteristicas del encabezado de UDP


Las principales variables o características que podemos obtener de un flujo UDP son:
- Puerto de salida: de donde viene la comunicación
- Puerto de destino: a dónde va la comunicación
- Tamaño del segmento: el tamaño en bytes del encabezado y de la información
- Bit de chequeo de errores


Los dispositivos IOT también funcionan en redes con protocolos menos complejos como 6LoWPAN, WSNs o CoAP entre otros, en la actualidad se poseen alternativas en cada capa del protocolo de internet que nos puedan brindar una solución similar.


 
| ![Diferencias entre el header UDP y TCP.](EDA/UPDvsTCP.png?raw=true "Diferencias entre el header UDP y TCP.") |
|:--:| 
| *fig 1. Diferencias entre el header UDP y TCP.[1]"* |


Uno de los principales problemas de UDP es que son más vulnerables a seguridad y por eso nos vamos a enfocar en ataques de botnet de estos dispositivos.

## Botnets

Botnets es la definicion dada para una red de dispositivos embebidos que fueron secuestrados mediante un ciber ataque, una vez infiltrados estos sirven como herramientas para realizar otro tipo de ataques como ataques de negacion de servicio, robo de datos, ataques a servidores, distribuicion entre otros.

El exito de este tipo de ataques nace gracias a su bajo tiempo requerido y costo ya que el mismo automatiza el infiltrar nuevos dispositivos y agregarlos a la red existente creando lo que llamamos como bots o computadores Zombies.

Todos los bots estan diseñados para operar bajo el comando de un tercero que es el dueño de la red de bots y siguen las siguientes etapas:

- Preparar y exponer: El hacker usa las debilidades de un dispositivo para poder infiltralos con el uso de un malware

- Infectar: el dispositivo es infectado con el malware

- activar: el hacker envia sus ataques.



### Mirai

### Bashlite

#### historia
Bashlite conocido también como Gafgyt, Lizkebab, PinkSlip, Qbot, Torlus y LizardStresser, originalmente llamado bashdoor[b1] su versión original data del 2014 y fue creado para tomar ventaja de las vulnerabilidades de Linux y macOs las cuales permiten al atacante ejecutar código y brindarle acceso no autorizado en la maquina infectada usando una puerta trasera del bash Shell que fue agregada en el código desde 1989.\
La idea es que cada proceso de bash puede compartir scripts y comandos con otros procesos de tipo bash, esta función de exportar permitía que los usuarios pudieran ejecutar códigos y scripts en terminales diferentes sin necesidad de volverlos a definir.\
Para poder compartir estos scripts los procesos accedían una tabla compartida, los cuales no tenían forma de verificar la procedencia de los scripts y simplemente asumían que venia de otro proceso de tipo bash.\
El atacante encontraba la forma de insertar su código en esta tabla y manipulando variables del sistema podían forzar que un nuevo proceso bash los ejecutara.\
Una vez dentro de el atacante puede hacer que el computado o el dispositivo ejecute un ataque de negación de servicio, el primer tipo de ataques de negación de servicio usando esta esta debilidad del bash ocurrió en setiembre del 2014 en contra de la empresa Akamai.\[b2]

#### Propagación 

El botnet bashlite fue creado para utilizar esta debilidad pero en una distribución de Linux llamada Busy box, la cual en el momento era utilizada en dispositivos embebidos como cámaras de seguridad y sus grabadores, rúters, teléfonos Android entre otros [b3] de los cuales las cámaras componían un 95% de los dispositivos infectados.\
Una vez infiltrado en una maquina bashlite automáticamente revisa la red usando Telnet scanners y busca todos los dispositivos con esta distribución y usando una lista de usuarios y contraseñas comunes lograba acceder a los dispositivos, contraseñas como “root” ó “12345” y usuarios como “admin” o “support” que vienen de fabrica con los componentes.\
Una vez dentro de la nueva maquina usando 2 scripts y la debilidad de bash obtenía control sobre el sistema y seguía el ciclo de buscar nuevos dispositivos con telnet scanners y de propagarse automáticamente.
Bashlite en versiones actualizadas utiliza otras debilidades además de la de bashdoor, como RCE metasploit module la cual podría insertar comandos de manera remota en dispositivos de la marca belkin conectados a la red los cuales van desde luces, cámaras hasta sensores de movimiento. [b5]\
Para el 2016 se estimo que aproximadamente un millón de dispositivos estaban infectados con este botnet.[b4]
#### Comando y control
Una vez bajo el control del malware, este inicia conexión con la red del botnet, la dirección de IP a cuál comunicarse fue escrita en su código de antemano y queda a espera de comandos, además para prevenir ataques de otro botones desconectado los servicios de telnet y SSH del dispositivo. 
los Comandos son escritos y enviados en un archivo de texto sin encriptar.\
En ocasiones se han detectado botnets que además de ejecutar comandos pueden emular un dispositivo infectado, este tiene monitores y respuestas programadas para poder engañar a otros dispositivos en la red.

#### Comandos
Hay botnets que contiene 80 o más comandos los cuales se pueden dividir en 6 tipos
- Ataques: negación de servicio usando TCP flood, entre otros por ejemplo
```
TCPFLOOD <IP> <Puerto>
```
- Gerencia: comandos para actualizar binarios, remover bots de la red o habilitar escanear 
```
UPDATE , BOTKILL, SCAN ON
```
- Informativos: revisar estado de bots y documentación
```
HELP, STATUS
```
- Interrupción: Comandos para parar  un ataque
KILLATTK
- otros: otros comandos que no entran en las categorías anteriores
CLEAR
La gran mayoría de los ataques de Bashlite son de tipo flooding los cuales son ataques en capas muy bajas y generalmente en el puerto 80 pero puede utilizar otros. 

## Tipos de ataques

## Recolección de datos

Para la recolección de datos se usa el obtenido en el paper “N-BaIoT: Network-based Detection of IoT Botnet Attacks Using Deep Autoencoders” en el cual usando diferentes dispositivos se tomaron datos de los mismo en caso de estar infectado, y en caso de estar limpio.
La captura de datos se realiza en un ambiente de laboratorio donde se conectaron diferentes dispositivos IoT vía wifi a varios puntos, y vía cable hacia un switch, el cual usando un port mirroring se logra un "sniffing" del tráfico, y para luego conectarse a un router.

| ![lab setup](EDA/labsetup.png?raw=true "lab setup") |
|:--:| 
| *fig 2. Lab setup para detectar IoT botnet attacks[2]"* |


Usando esta configuración el equipo detrás de la investigación de la universidad de Ben-Gurion  obtuvieron los siguientes flujos de datos.
Se obtiene información del host, y la dirección física MAC, esto es muy importante ya que ataques de la botnet Mirai son capaces de mandar un mensaje con un IP falso, por lo que utilizar el IP físico puede darnos un mejor resultado.
Para el Bashlite attack:

-	Flujo de Scan: es el flujo de escaneo del botnet buscando vulnerabilidades
-	Junk: Un ataque donde se envia información de spam
-	UDP:  el Ataque DDOS usando el protocolo UDP
-	TCP: el ataque DDOS usando el protocolo TCP
-	COMBO: que es el envio de spam y abriendo conexiones a direcciones IPs y puertos

Estas comunicaciones se guardan en diferentes archivos CSV con algunas variables extras que discutiremos más adelante
Para el ataque mirai se usa obtiene algo parecido:
-	Flujo de Scan: es el flujo de escaneo del botnet buscando vulnerabilidades
-	UDP:  el Ataque DDOS usando el protocolo UDP
-	Ack:  el Ataque DDOS usando la bandera de  ACK
-	Syn:  el Ataque DDOS usando la bandera de  Syn
-	UDPplain: un tipo de ataque DDOS por protocolo UDP con menos datos pero mayor cantidad de paquetes por segundo.

Para los demás flujos benignos se guardan todos en un solo archivo que contienen comunicaciones normales o esperadas de los dispositivos.

## de pcap a dataset

La cantidad de variables obtenidas en cada flujo puede parecer pequeña en comparación con encabezados más complejos como el del protocolo TCP, sin embargo podemos obtener diferentes variables de una sola medida por ejemplo.
Para comprende un poco como se convierte el pcap a dataset veamos el siguiente ejemplo de un pcap de una red con un dispositivo Iot:

| ![Ejemplo de pcap](EDA/ejemplopcap.png?raw=true "Ejemplo de pcap") |
|:--:| 
| *fig 3. Ejemplo de pcap de una cámara de seguridad"* |

Como se menciona anteriormente el dispositivo usa el protocolo UDP para comunicarse y la información que posee este protocolo es más menor que el protocolo TCP.

Sin embargo aun podemos obtener muchas variables de esta información como por ejemplo:

- Podemos identificar flujo del dispositivo a otro dispositivo, o del  dispositivo hacia la red y viceversa.

- Agregando hardware especializado como el que se menciona en el experimento se obtienen el flujo del host y del puerto MAC.

- Del tamaño podemos obtener la media, la varianza, la cantidad de paquetes enviados durante un ataque en específico, un ejemplo de estadísticas que podemos obtener con wireshark:

| ![Ejemplo de estadística](EDA/Estadisticasbasicaswireshark.png?raw=true "Ejemplo de pcap") |
|:--:| 
| *fig 4. Ejemplo estadístico de pcap del flujo de un dispositivo Iot infectado"* |

- En caso de tener una comunicación de dispositivo a dispositivo podemos obtener la varianza de ambos flujos y obtener el radio (mediante la suma de ambos), Así como la magnitud si sumamos la media. Por último también podemos obtener la covarianza entre los dos flujos.

- Si usamos ventanas de diferentes tiempos podemos observar cual es el flujo de paquetes durante 100ms, 500ms, 1.5sec, 10sec, y 1min. Clasificar la información de esta forma es muy relevante puesto que un flujo normal de una cámara sería algo relativamente constante, pero un ataque de mirai podría tener ciclos diferente de envío de información.

Por ejemplo en esta captura a primera vista no parece haber ningún problema cuanto usamos un intervalo de 100ms
| ![Ejemplo de estadística intervalo de 100ms](EDA/ActividadDedispositivointervalo100ms.png?raw=true "Ejemplo de estadística intervalo de 100ms") |
|:--:| 
| *fig 5. Numero de paquetes de un dispositivo Iot infectado en una ventana de 100ms"* |

Pero si cambiamos la ventana de tiempo de captura a 1 segundo se puede observar con claridad algún tipo de ataque o de flujo anormal.

| ![Ejemplo de estadistica intervalo de 1s](EDA/ActividadDedispositivointervalo1s.png?raw=true "Ejemplo de estadistica intervalo de 1s") |
|:--:| 
| *fig 6. Numero de paquetes de un dispositivo Iot infectado en una ventana de 1s"* |


## características del dataset

El dataset o conjunto de datos se divide por dispositivo y cada dispositivo posee archivos para su flujo benigno y para sus diferentes flujos malignos.
Aquí se puede observar un ejemplo de cómo se guardan los archivos

```
├───Danmini_Doorbell
│   │   benign_traffic.csv.bz2
│   │
│   ├───gafgyt_attacks
│   │       combo.csv.bz2
│   │       junk.csv.bz2
│   │       scan.csv.bz2
│   │       tcp.csv.bz2
│   │       udp.csv.bz2
│   │
│   └───mirai_attacks
│           ack.csv.bz2
│           scan.csv.bz2
│           syn.csv.bz2
│           udp.csv.bz2
│           udpplain.csv.bz2
```


### Variables

En este data set podemos encontrar hasta 115 variables, por dispositivo, tenemos 23 variables únicas para 4 tipo de flujos diferentes y diferentes ventanas de tiempo.
La lista de variables se compone de la siguiente manera:

|Value| Statistic| Aggregated by| Total Number of Features|
|-----|----------|--------------|-------------------------|
|Packet size (of outbound packets only)| Mean, Variance| Source IP, Source MAC-IP, Channel, Socket| 8|
|Packet count| Number| Source IP, Source MAC-IP, Channel, Socket| 4|
|Packet jitter (the amount of time between packet arrivals)| Mean, Variance, Number| Channel| 3|
|Packet size (of both inbound and outbound together)|Magnitude, Radius, Covariance, Correlation coefficient| Channel, Socket| 8|
||

```
Source IP: es el ip del host
Source Mac-IP: es la dirección del gateway.
Los sockets son determinados por el dispositivo de origen y el puerto de destino ya sea de TCP o UDP, por ejemplo tráfico enviado de 192.168.1.12:1234 hacia 192.168.1.50:80

```
Podemos identificar los diferentes flujos y las diferentes ventanas de tiempo usando la nomenclatura:
```
Prefijos:
H: Trafico desde un host (IP)
MI: Trafico desde un Mac-IP
HpHp: tráfico desde un host port a otro host port
HH_jit: tráfico jitter desde un host port a otro host port

Otras abreviaciones en el nombre del feature:
time windows:
L5: 1min
L3: 10sec
L1: 1.5sec
L0.1: 500ms
L0.01: 100ms

```
Finalmente usamos lo nombre de los variable:

```
weight: Peso del flujo, numero de ítems observados
mean: media
std: media estándar
radius: La raíz cuadrada de la suma de dos varianzas
magnitude: La raíz cuadrada de la suma de dos medias
cov: covarianza de dos flujos
```
Si unimos todo podemos leer cada variable con facilidad por ejemplo:
```
Peso del flujo de Mac-IP con una ventana de tiempo de 1 min:
MI_dir_L5_weight
Varianza de flujo del host en una ventana de tiempo de 10sec:
H_L3_variance
La covarianza del flujo de una comunicación de host a host en una ventana de tiempo de 1.5sec:
HH_L1_covariance

```


# Metodología

  Identificar los estudios e investigaciones relacionadas al tema.
  
  Analizar los diferentes ataques y dispositivos del conjunto de datos usado en la investigación "N-BaIoT: Network-based Detection of IoT Botnet Attacks Using Deep Autoencoders".
  
  Distinguir que características del conjunto de datos pueden ser claves para detectar flujos anormales.
  
  Implementar un modelo SVM con el conjunto de datos completo y medir resultados de precisión, eficiencia y tiempos de desempeño.
  
  Entrenar el mismo modelo con solo las características que se desea comparar y medir resultados.
  
  Comparar los resultados obtenidos.

  
# Referencias

Yair Meidan, Michael Bohadana, Yael Mathov, Yisroel Mirsky,
Dominik Breitenbacher, Asaf Shabtai, and Yuval Elovici, "N-BaIoT: Network-based Detection
of IoT Botnet Attacks
Using Deep Autoencoders", IEEE PERVASIVE COMPUTING, VOL. 13, NO. 9, JULY-SEPTEMBER 2018 

https://towardsdatascience.com/do-you-know-how-to-choose-the-right-machine-learning-algorithm-among-7-different-types-295d0b0c7f60

[1] https://www.emnify.com/iot-glossary/udp

[2] "N-BaIoT: Network-based Detection
of IoT Botnet Attacks
Using Deep Autoencoders"

https://iotanalytics.unsw.edu.au/attack-data

https://www.kaspersky.com/resource-center/threats/botnet-attacks

https://www.usenix.org/system/files/conference/usenixsecurity17/sec17-antonakakis.pdf

http://www.cs.ucf.edu/~jcchoi/pub/idsc19.pdf

https://ieeexplore.ieee.org/document/8538636

https://www.trendmicro.com/en_us/research/19/d/bashlite-iot-malware-updated-with-mining-and-backdoor-commands-targets-wemo-devices.html

https://www.trendmicro.com/en_us/research/19/h/back-to-back-campaigns-neko-mirai-and-bashlite-malware-variants-use-various-exploits-to-target-several-routers-devices.html

[b1] https://www.zdnet.com/article/first-attacks-using-shellshock-bash-bug-discovered/

[b2]https://www.itnews.com.au/news/first-shellshock-botnet-attacks-akamai-us-dod-networks-396197

[b3] https://thehackernews.com/2014/11/bashlite-malware-leverages-shellshock.html

[b4] https://www.securityweek.com/bashlite-botnets-ensnare-1-million-iot-devices

[b6]https://honeytarg.cert.br/honeypots/docs/papers/honeypots-iscc18.pdf

[b5]https://www.trendmicro.com/en_us/research/19/d/bashlite-iot-malware-updated-with-mining-and-backdoor-commands-targets-wemo-devices.html

[d1] https://developer.okta.com/books/api-security/dos/what/

[d2] https://www.spiceworks.com/it-security/network-security/articles/what-is-botnet/#:~:text=A%20botnet%20is%20a%20cyberattack,%2C%20other%20devices%2C%20or%20individuals.

[d3]https://www.imperva.com/learn/ddos/ddos-attacks/

[d4]https://www.radware.com/security/ddos-knowledge-center/ddospedia/tcp-flood/
https://sites.cs.ucsb.edu/~kemm/courses/cs595G/TM06.pdf

