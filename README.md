
# TITULO
  Detección de ataques de botnets usando aprendizaje automático en un conjunto de datos dado.
# Resumen

  Un estudio anterior titulado "N-BaIoT: Network-based Detection of IoT Botnet Attacks Using Deep Autoencoders" ha demostrado que los clasificadores de aprendizaje automático para detectar flujo maligno o benigno en varios dispositivos embebidos posee una gran precisión y eficiencia, esto utilizando un conjunto de datos extenso de hasta 115 features.
  Como conclusión de la investigación mencionada al final del estudio se hace una pregunta fundamental:
  
  ¿Se podrá calificar cada uno de los features para saber cuáles son los que mejor ayudan en la precisión?
  
  Tratar de darle una nota a cada uno de los 115 features puede ser mucho para nuestra investigación sin embargo si podemos tratar de analizar el impacto de características claves en un conjunto de datos, este impacto puede ser negativo o positivo en cuanto a precisión, eficiencia y tiempos de desempeño de la detección de botnets.
  
  ----si las ventanas de tiempo es la característica a analizar----
  En esta investigación analizaremos una característica importante de este conjunto de datos el cual son las ventanas de tiempo usada en la obtención de datos, los cuales poseen mediciones usando 5 ventanas de tiempo diferente.
  
  se concluye que....

# Introducción



## Problema

Los Features en el dataset usado en la investigación "N-BaIoT: Network-based Detection of IoT Botnet Attacks Using Deep Autoencoders" fueron tomados de forma empírica y los modelos entrenados en dicho dataset muestran una alta precisión, sin embargo no hay una medición formal de que tanto afectan dichos features en la creación del modelo y si de verdad es necesario tener 115 de ellos.

## Pregunta de Investigación

   ¿Cuál es el impacto de las diferentes características en un conjunto de datos en la precisión de un modelo de machine learning para la detección de botnet en una red?

# Objetivos

## General
  Evaluar el impacto de diferentes características del conjunto de datos en la construcción y desempeño de un clasificador.
  
## Especifico
  
  Construir un clasificador con todas las características del conjunto de datos, y también solo con características claves del conjunto de datos.
  
  Medir el impacto en la precisión, eficiencia y tiempos de desempeño.

  Comparar el impacto de las características claves en los resultados.

# Metodología

  Identificar los estudios e investigaciones relacionadas al tema.
  
  Analizar los diferentes ataques y dispositivos del conjunto de datos usado en la investigación "N-BaIoT: Network-based Detection of IoT Botnet Attacks Using Deep Autoencoders".
  
  Distinguir que características del conjunto de datos pueden ser claves para detectar flujos anormales.
  
  Implementar un modelo One-Class SVM con el conjunto de datos completo y medir resultados de precisión, eficiencia y tiempos de desempeño.
  
  Entrenar el mismo modelo con solo las características que se desea comparar y medir resultados.
  
  Comparar los resultados obtenidos.
  
  
# Referencias

Yair Meidan, Michael Bohadana, Yael Mathov, Yisroel Mirsky,
Dominik Breitenbacher, Asaf Shabtai, and Yuval Elovici, "N-BaIoT: Network-based Detection
of IoT Botnet Attacks
Using Deep Autoencoders", IEEE PERVASIVE COMPUTING, VOL. 13, NO. 9, JULY-SEPTEMBER 2018 

https://towardsdatascience.com/do-you-know-how-to-choose-the-right-machine-learning-algorithm-among-7-different-types-295d0b0c7f60
