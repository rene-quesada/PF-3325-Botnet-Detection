# Dataset
El Dataset para este trabajo se localiza en la pagina
http://archive.ics.uci.edu/ml/datasets/detection_of_IoT_botnet_attacks_N_BaIoT

Sin embargo como todos los csv estan comprimidos no se puede acceder a el directamente,
por lo que se recomienda descargarlo y crear la siguiente jerarquia de archivos
(se utiliza bz2 para ahorrar espacio en disco)

```
│   demonstrate_structure.csv
│   demonstrate_structure.csv.bz2
│   features.csv
│   N_BaIoT_dataset_description_v1.txt
│
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
│
├───Ecobee_Thermostat
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
│           ack.csv
│           scan.csv
│           syn.csv
│           udp.csv
│           udpplain.csv
│
│
├───Philips_B120N10_Baby_Monitor
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
│
├───Provision_PT_737E_Security_Camera
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
│
├───Provision_PT_838_Security_Camera
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
│
├───SimpleHome_XCS7_1002_WHT_Security_Camera
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
│
└───SimpleHome_XCS7_1003_WHT_Security_Camera
    │   benign_traffic.csv.bz2
    │
    ├───gafgyt_attacks
    │       combo.csv.bz2
    │       junk.csv.bz2
    │       scan.csv.bz2
    │       tcp.csv.bz2
    │       udp.csv.bz2
    │
    └───mirai_attacks
            ack.csv.bz2
            scan.csv.bz2
            syn.csv.bz2
            udp.csv.bz2
            udpplain.csv.bz2
			
```
