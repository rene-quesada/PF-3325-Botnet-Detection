
# TITULO
  Uso de IA para detección de comunicación de botnets y ataques de DDOS en un set de datos reducido.

# Resumen

  Los dispositivos embebidos en IOT conocidos como dispositivos IOT están más presentes en la cotidianidad de nuestras vidas que nunca, desde un bombillo inteligente hasta un sistema de cámaras. La principal característica de estos dispositivos es su simplicidad esto debido a que tienen limitaciones de poder y de procesamiento.   

  Esto puede ser una ventaja en muchas formas, pero también son abiertas a problemas de seguridad en este proyecto estudiaremos una solución usando machine learning para detectar ataques de tipo botnet los cuales pueden tomar posesión del dispositivo y desde el mismo crear ataques de tipo DDOS y otros.
  
  Un estudio anterior llamado "N-BaIoT: Network-based Detection of IoT Botnet Attacks Using Deep Autoencoders" ha demostrado una gran precisión con modelos como SVM, isolation forrest y otros, cuando se utiliza un dataset extenso de hasta 115 features.
  
  Los datos recolectados en este estudio utilizan una gran basta cantidad de características que facilitan el entrenamiento de los modelos, todos los modelos tienen una precisión muy alta, sin embargo al final del estudio se hace una pregunta fundamental, se podrá calificar cada uno de los features para saber cuáles son los que mejor ayudan en la precisión.   Tratar de darle una nota a cada uno de los 115 features puede ser mucho para nuestra investigación sin embargo es una buena pregunta que queremos contestar, al menos parcialmente.
  En esta investigación analizaremos una característica principal de este dataset, las ventanas de tiempo usada en la obtención de datos, el dataset posee mediciones usando 5 ventanas de tiempo diferente, poder reducir al menos una de ellas significaría una reducción de 22 features en el dataset, nuestra meta es entender cuál es el impacto de usar diferentes ventanas de tiempo de nuestro modelo.

# Introducción


## Problema


## Pregunta de Investigación

   ¿Cuál es el impacto de usar diferentes ventanas de tiempo en la precisión de un modelo de machine learning para la detección de botnet en una red?

# Objetivos

## General
  Hacer uso de machine and Deep learning para la detección y clasificación de flujos en una red con dispositivos IOT.  
  Poder clasificar flujos normales de los dispositivos de las comunicaciones de dispositivos contaminados con botnets, tales flujos los denominaremos benignos y malignos respectivamente usando diferentes ventanas de tiempo en nuestras mediciones.
  Comparar y entender el efecto de reducir los parámetros antes mencionados en la precisión del modelo.
  
## Especifico
  
### Examinar los diferentes dataset relacionados a IOT y Botnets
  Revisar la disponibilidad de datasets relacionados a Botnets.
  Examinar y entender los diferentes datasets relacionados a Botnets.
  Explicar los features o características, así como los posibles labels.

### Identificar cual ventana de tiempo es la mejor para la detección de flujo maligno
  Utilizar SVM (el modelo utilizado en la investigación previa) para hacer pruebas con un set de features reducidos según sus ventanas de tiempo.
  Identificar cual ventana de tiempo que me brinda mayor precisión.

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
