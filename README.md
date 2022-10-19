
# TITULO
  Uso de IA para detección de comunicación de botnets y ataques de DDOS.

# Resumen

  Los dispositivos embebidos en IOT conocidos como dispositivos IOT están más presentes en la cotidianidad de nuestras vidas que nunca, desde un bombillo inteligente hasta un sistema de cámaras. 

  Estos dispositivos se han incorporado de forma silenciosa en nuestras casas y nuestras vidas.  La principal característica de estos dispositivos es su simplicidad esto debido a que tienen limitaciones de poder y de procesamiento.   

  Esto puede ser una ventaja en muchas formas, pero también son abiertas a problemas de seguridad en este proyecto nos enfocaremos como podemos usar machine learning para detectar ataques de tipo botnet los cuales pueden tomar posesión del dispositivo y desde el mismo crear ataques de tipo DDOS y otros.
  ...TBD


# Introducción


## Problema

## Pregunta de Investigación

# Objetivos

## General
  Hacer uso de machine and deep learning para la detección y clasificación de flujos en una red con dispositivos IOT.  
  Clasificando flujos normales de los dispositivos de las comunicaciones de dispositivos contaminados con botnets, tales flujos los denominaremos benignos y malignos respectivamente.
  
## Especifico
  
### Examinar los diferentes dataset relacionados a IOT y Botnets
  Revisar la disponibilidad de datasets relacionados a Botnets.
  Examinar y entender los diferentes datasets relacionados a Botnets.
  Explicar los features o características, así como los posibles labels.

### Identificar flujo maligno de benigno
  Hacer uso de diferentes modelos como Random Forrest o deep learning para poder clasificar entre el flujo normal de un dispositivo IOT de un flujo anormal causado por un botnet.
  
# Metodología

## Dataset

Para la recolección de datos se usará el paper “N-BaIoT: Network-based Detection of IoT Botnet Attacks Using Deep Autoencoders” en el cual usando diferentes dispositivos tomamos datos de los mismo en caso de estar infectado, y en caso de estar limpio
 

Usando esta configuración podemos obtener los siguientes flujos de datos

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

Para los demás flujos benignos se guardan todos en una csv pero contienen comunicaciones normales de los dispositivos
Ahora bien si el protocolo UDP tiene tan pocos espacios que podemos obtener de ellos bueno para cada flujo podemos obtener por ejemplo el tamaño promedio del paquete, si por ejemplo se hace un ataque DDOS el tamaño de los paquetes pueden ser grandes pero constantes en longitud y tipo de datos, por lo que no debería tener mucha variedad y la media debería ser constante, entonces ese va a ser un feature la media y la varianza del tamaño de los datos.
De esta forma podemos elaborar una tabla como la siguiente donde mostramos toda la cantidad de features que podemos tener
 

  
## Features.
  Se utilizarán los mismo features ya propuestos por el paper “N-BaIoT: Network-based Detection of IoT Botnet Attacks Using Deep Autoencoders” esto debido a que la cantidad de parámetros de los flujos IOT son más limitados y son cubiertos por los features de este dataset.  

## Labels.
  Iniciamos con el labels de maligno el cual será 0 si es un flujo benigno o 1 si es un flujo relacionado a un botnet, luego agregaremos un label de botnet el cual nos dirá que tipo de botnet es este flujo, y por último un label de tipo de ataque el cual nos informara si es un ataque de DDOS o un escaneo del botnet a nuestra red.

## Modelo.
  Para el modelo se utilizará Random Forrest y deep learning, esto para poder comparar con los modelos utilizados en proyectos similares que utilizan este mismo dataset.    Una vez propuestos uno o dos modelos probaremos nuestro precisión y exactitud con respecto a otros proyectos.
  
## Ejecución.
  Se propone ejecutar una muestra en un computador personal, pero con ayuda de cuda podríamos ejecutar todos los datos en el servidor de la maestría de la ECCI.


# Referencias

Yair Meidan, Michael Bohadana, Yael Mathov, Yisroel Mirsky,
Dominik Breitenbacher, Asaf Shabtai, and Yuval Elovici, "N-BaIoT: Network-based Detection
of IoT Botnet Attacks
Using Deep Autoencoders", IEEE PERVASIVE COMPUTING, VOL. 13, NO. 9, JULY-SEPTEMBER 2018 


https://towardsdatascience.com/do-you-know-how-to-choose-the-right-machine-learning-algorithm-among-7-different-types-295d0b0c7f60