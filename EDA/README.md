# EDA

A diferencia de un computador un dispositivo de IOT no realiza múltiples tareas, usualmente está programado para llevar a cabo una sola tarea, por lo que sus comunicaciones son más limitadas y menos variantes

Muchos de los dispositivos usan comunicaciones en tiempo real, por ejemplo, una cámara de video, un Alexa, etc.… por lo que mantener una comunicación compleja como en TCP donde los paquetes pueden llegar en desorden y hay controles para asegurarnos que la información llega más bien es un exceso que causaría un retraso en una señal de tiempo real.

Los dispositivos IOT tienden a usar UDP para comunicarse ya que ocupa menos recursos, consume menos potencia ya que puede operar en redes  LLNs (Low power, Lossy Networks)
| ![Diferencias entre el header UDP y TCP.](UPDvsTCP.png?raw=true "Diferencias entre el header UDP y TCP.") |
|:--:| 
| *fig 1. Diferencias entre el header UDP y TCP.[1]"* |

Los principales features que podemos obtener de un flujo de IOT son:

  Source port: de donde viene

  Destination port: adónde va

  UDP length: el tamaño en bytes del header y de la información

  Checksum: chequeo de errores

Tambien usando el equipo adecuado podemos obtener el Flujo saliendo del host, flujo saliente del puerto.

Para este proyecto se utiliza el dataset obtenido en el paper "N-BaIoT: Network-based Detection
of IoT Botnet Attacks
Using Deep Autoencoders"

La captura de datos se realiza en un ambiente de laboratorio donde se conectan el dispositivo IoT via wifi a varios puntos, y via cable hacia un switch, el cual usando un port mirroring se logra un "sniffing" del trafico, y para luego conectarse a un router.

Se obtiene informacion del host, y la direccion fisica MAC, esto es muy imporante ya que ataques de la botnet Mirai es capaz de mandar un mensaje con un IP falso, por lo que utilizar el IP fisico puede darnos un mejor resultado.

Se colecta la informacion en un PCAP para 9 dispositivos Iot en tres condiciones. 

1. Sin botnets, obteniendo un flujo normal del dispositivo
2. infectado con el botnet Miria y usando comandos C&C para que el botnet envie ataques
3. infectado con el flujo Bashlite y usando comandos C&C para que el botnet envie ataques

Por lo que se logra obtener flujos esperados del dispositivos, flujos del botnet Miria, flujos de bashlite por separado
| ![lab setup](labsetup.png?raw=true "lab setup") |
|:--:| 
| *fig 2. Lab setup para detectar IoT botnet attacks[2]"* |

Los tipos de ataques capturados por aparte para cada botnet son:
```
BASHLITE Attacks:

1) Scan: Scanning the network for vulnerable devices
2) Junk: Sending spam data
3) UDP: UDP flooding
4) TCP: TCP flooding
5) COMBO: Sending spam data and opening a connection
to a specified IP address and port

Mirai Attacks

1) Scan: Automatic scanning for vulnerable devices
2) Ack: Ack flooding
3) Syn: Syn flooding
4) UDP: UDP flooding
5) UDPplain: UDP flooding with fewer options, optimized
for higher PPS
```
## pcap a dataset

Para comprende un poco como se convierte el pcap a dataset veamos el siguiente ejemplo de un pcap de una red con un dispositivo Iot:

| ![Ejemplo de pcap](ejemplopcap.png?raw=true "Ejemplo de pcap") |
|:--:| 
| *fig 3. Ejemplo de pcap de una camara de seguridad"* |


Como se observa el dispositivo usa UDP para comunicarse, y como vimos en la figura 1 el informacion que posee este protocolo es mas simple que el TCP.

Sin embargo aun podemos obtener muchos features de esta informacion como por ejemplo:

- Podemos obtener el IP de destino y de fuente: Este no podemos usarlo directamente en nuestro dataset puesto que lo que queremos hacer es entrenar a nuestro modelo sin importar el IP de destino o de envio. Sin embargo podemos usar este IP para catalogar que este es un flujo que proviene del dispositivo.

       Esto significa que podemos identificar flujo del dispositivo a otro dispositivo, del  dispositivo hacia la red o de la red hacia el dispositivo.
       Agregando hardware especializado podriamos tambien obtener flujo del host y del puerto MAC.
- Del tamaño podemos obtener la media, la varianza, la cantidad de paquetes enviados durante un ataque en especifico, un ejemplo de estadisticas que podemos obtener con wireshark:

| ![Ejemplo de estadistica](Estadisticasbasicaswireshark.png?raw=true "Ejemplo de pcap") |
|:--:| 
| *fig 4. Ejemplo estadistica de pcap del flujo de un dispositivo Iot infectado"* |


- En caso de tener una comunicacion de dispositivo a dispositivo podemos obtener la varianza de ambos flujos y obtener el radio (mediante la suma de ambos), Asi como la magnitud si sumamos la media. Por ultimo tambien podemos obtener la covarianza entre los dos flujos.

- Si usamos ventanas de diferentes tiempo podemos observar cual es el flujo de paquetes durante 100ms, 500ms, 1.5sec, 10sec, y 1min. Clasificar la informacion de esta forma es muy relevante puesto que un flujo normal de una camara seria algo relativamente constante, pero un ataque de mirai podria tener ciclos diferente de envio de informacion.

Por ejemplo en esta captura a primera vista no parece haber ningun problema cuanto usamos un intervalo de 100ms
| ![Ejemplo de estadistica intervalo de 100ms](ActividadDedispositivointervalo100ms.png?raw=true "Ejemplo de estadistica intervalo de 100ms") |
|:--:| 
| *fig 5. Numero de paquetes de un dispositivo Iot infectado en una ventana de 100ms"* |

Pero si cambiamos la ventana de tiempo de captura a 1 segundo se puede observar con claridad algun tipo de ataque o de flujo anormal.

| ![Ejemplo de estadistica intervalo de 1s](ActividadDedispositivointervalo1s.png?raw=true "Ejemplo de estadistica intervalo de 1s") |
|:--:| 
| *fig 6. Numero de paquetes de un dispositivo Iot infectado en una ventana de 1s"* |


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

# referencias
[1] https://www.emnify.com/iot-glossary/udp

[2] "N-BaIoT: Network-based Detection
of IoT Botnet Attacks
Using Deep Autoencoders"

https://iotanalytics.unsw.edu.au/attack-data