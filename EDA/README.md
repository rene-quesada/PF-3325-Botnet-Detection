# EDA

A diferencia de un computador un dispositivo de IOT no realiza múltiples tareas, usualmente está programado para llevar a cabo una sola tarea, por lo que sus comunicaciones son más limitadas y menos variantes

Muchos de los dispositivos usan comunicaciones en tiempo real, por ejemplo, una cámara de video, un Alexa, etc.… por lo que mantener una comunicación compleja como en TCP donde los paquetes pueden llegar en desorden y hay controles para asegurarnos que la información llega más bien es un exceso que causaría un retraso en una señal de tiempo real.

Los dispositivos IOT tienden a usar UDP para comunicarse ya que ocupa menos recursos, consume menos potencia ya que puede operar en redes  LLNs (Low power, Lossy Networks)

Diferencias entre el header UDP y TCP.


Los principales features que podemos obtener de un flujo UDP son:
  Source port: de donde viene
  Destination port: adónde va
  UDP length: el tamaño en bytes del header y de la información
  Checksum: chequeo de errores

Los dispositivos IOT también funcionan en redes con protocolos menos complejos como 6LoWPAN, WSNs o CoAP entre otros.

 

Comparación de protocolos web vs IOT. Source: Zach Shelby, Micro:bit Foundation[1].]

Uno de los principales problemas de UDP es que son más vulnerables a seguridad y por eso nos vamos a enfocar en ataques de botnet de estos dispositivos.



## pcap a dataset

## caracteristicas del dataset
benign data description
       MI_dir_L5_weight  ...  HpHp_L0.01_pcc
count     464682.000000  ...    4.646820e+05
mean           4.551462  ...    4.930225e-02
std           12.337134  ...    2.004442e-01
min            1.000000  ...   -2.252107e+00
25%            1.000003  ...   -2.410000e-17
50%            1.243612  ...    0.000000e+00
75%            2.868521  ...    4.560013e-02
max          234.055965  ...    2.811226e+00

[8 rows x 115 columns]

Mirai data description
       MI_dir_L5_weight  ...  HpHp_L0.01_pcc
count     154894.000000  ...        154894.0
mean         116.017470  ...             0.0
std           44.661682  ...             0.0
min            1.000000  ...             0.0
25%           88.621061  ...             0.0
50%          116.100444  ...             0.0
75%          146.090197  ...             0.0
max          434.164516  ...             0.0

[8 rows x 115 columns]

baschlite data description
       MI_dir_L5_weight  ...  HpHp_L0.01_pcc
count     154894.000000  ...   154894.000000
mean          50.323870  ...        0.000415
std           73.233787  ...        0.022596
min            1.000000  ...       -0.146202
25%            1.000000  ...        0.000000
50%            1.000000  ...        0.000000
75%          136.978047  ...        0.000000
max          301.516086  ...        1.531159


![Alt text](HH_jit_L3_variance_benign_hist.png?raw=true "Title")

## Features

## Maligno vs Benigno

### Caracteristicas por Dispositivos

## Mirai vs Bashlite

### Caracteristicas por Dispositivos
