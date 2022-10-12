

# Avance de programada

## Investigacion previa de las comunicaciones IOT

A diferencia de un computador un dispositivo de IOT no realiza múltiples tareas, usualmente está programado para llevar a cabo una sola tarea, por lo que sus comunicaciones son más limitadas y menos variantes

Muchos de los dispositivos usan comunicaciones en tiempo real, por ejemplo una cámara de video, un Alexa, etc.. por lo que mantener una comunicación compleja como en TCP donde los paquetes pueden llegar en desorden y hay controles para asegurarnos que la información llega mas bien es un exceso que causaría un retraso en una señal de tiempo real.

Los dispositivos IOT tienden a usar UDP para comunicarse ya que ocupa menos recursos, consume menos potencia ya que puede operar en redes  LLNs (Low power, Lossy Networks)


 
Diferencias entre el header UDP y TCP.


Los principales features que podemos obtener de un flujo UDP son:
	Source port: de donde viene
	Destination port: adónde va
	UDP length: el tamaño en bytes del header y de la informacion
	Checksum: chequeo de errores


Los dispositivos IOT también funcionan en redes con protocolos menos complejos como 6LoWPAN, WSNs o CoAP entre otros.


 

Comparación de protocolos web vs IOT. Source: Zach Shelby, Micro:bit Foundation[1].]

Uno de los principales problemas de UDP es que son mas vulnerables a seguridad y por eso nos vamos a enfocar en ataques de botnet de estos dispositivos.


##Recolección de datos 

Para la recolección de datos se usara el paper “N-BaIoT: Network-based Detection of IoT Botnet Attacks Using Deep Autoencoders” en el cual usando diferentes dispositivos tomamos datos de los mismo en caso de estar infectado, y en caso de estar limpio
 

Usando esta configuración podemos obtener los siguiente flujos de datos

Para el Bashlite attack:
•	Flujo de Scan: es el flujo de escaneo del botnet buscando vulnerabilidades
•	Junk: Un ataque donde se envia información de spam
•	UDP:  el Ataque DDOS usando el protocolo UDP
•	TCP: el ataque DDOS usando el protocolo TCP
•	COMBO: que es el envio de spam y abriendo conexiones a direcciones IPs y puertos
Estas comunicaciones se guardan en diferentes archivos CSV con algunos features extras que discutiremos mas adelante
 

Para el ataque mirai se usa obtiene algo parecido
•	Flujo de Scan: es el flujo de escaneo del botnet buscando vulnerabilidades
•	UDP:  el Ataque DDOS usando el protocolo UDP
•	Ack:  el Ataque DDOS usando la bandera de  ACK
•	Syn:  el Ataque DDOS usando la bandera de  Syn
•	UDPplain: un tipo de ataque DDOS por protocolo UDP con menos datos pero mayor cantidad de package per seconds
Para los demás flujos benignos se guardan todos en una csv pero contienen comunicaciones normales de los dispositivos
Ahora bien si el protocolo UDP tiene tan pocos espacio que podemos obtener de ellos bueno para cada flujo podemos obtener por ejemplo el tamaño promedio del paquete, si por ejemplo se hace un ataque DDOS el tamaño de los paquete pueden ser grandes pero constantes en longitud y tipo de datos, por lo que no debería tener mucha variedad y la media debería ser constante, entonces ese va a ser un feature la media y la varianza del tamaño de los datos.
De esta forma podemos elaborar una tabla como la siguiente donde mostramos toda la cantidad de features que podemos tener
 
## EDA
  TBD.
  Ya tengo unos graficos muy interesantes en la carpeta de EDA pero me falta agregarlos en el README y agregar el codigo usado.
# TITULO:
  Uso de IA para deteccion de comunicacion de botnets y ataques de DDOS.

# Objetivos

## General
  Hacer uso de IAs para la deteccion y clasificacion de diferente flujos relacionados con botnets los cuales denominaremos malignos, en los dispositivos de IOT. 
  
## Especifico
  
  ### Objetivo de identificar flujo maligno de benigno
  Hacer uso de diferentes modelos como Random Forrest o deep learning para poder clasificar entre el flujo normal de un dispositivo IOT de un flujo anormal causado por un botnet.
  
  ### Objetivo de identificar tipo de botnet
  Utilizar el modelo para poder detectar que tipo de botnet es el que esta causando el ataque si es un botnet de tipo mirai o bashlite attack
  
  ### Objetivo de identificar tipo de flujo de la botnet
  (Extra) Poder detectar si se esta realizando un ataque DDOS o si es un escaneao del botnet buscando vilnerabilidades en la red.
  
# Metodologia

  ## Dataset.
   Nuestro enfoque en este trabajo sera en el uso del modelo para la clasificacion de datos, por lo que en vez de recolectar la informacion manualmente vamos a utilizar un dataset ya creado para la investigacion del paper: “N-BaIoT: Network-based Detection of IoT Botnet Attacks Using Deep Autoencoders” 
  
  ## Features.
  Se utilizaran los mismo features ya propuestos por el paper “N-BaIoT: Network-based Detection of IoT Botnet Attacks Using Deep Autoencoders” esto debido a que la cantidad de parametros de los flujos IOT son mas limitados y son cubiertos por los features de este dataset.  

  ## Labels.
   Iniciamos con el labels de maligno el cual sera 0 si es un flujo benigno o 1 si es un flujo relacionado a un botnet, luego agregaremos un label de botnet el cual nos dira que tipo de botnet es este flujo, y por ultimo un label de tipo de ataque el cual nos informara si es un ataque de DDOS o un escaneo del botnet a nuestra red.

  ## Modelo.
   Para el modelo se utilizara Random Forrest y deep learning, esto para poder comparar con los modelos utlizados en proyectos similares que utilizan este mismo dataset.    Una vez propuestos uno o dos modelos probaremos nuestro precision y exactitud con respecto a otro proyectos.
  
  ## Ejecucion.
  Se propone ejecutar una muestra en un computador personal, pero con ayuda de cuda podriamos ejecutar todo los datos en el servidor de la maestria de la ECCI.
