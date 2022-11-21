# Modelos usados 

Para la implementacion del modelo se usara alguno de los modelos ya implementados en la investigacion previa:

| ![lab setup](modelospaper.png?raw=true "modelos utilizados") |
|:--:| 
| *fig 1. Modelos usados en la investigacion"* |


En este caso se usara SVM por ser facil de entrenar y por que es uno que beinda mejores resultados ademas en otras investigaciones ""< Agregar papers>"" el uso de SVC es uno de lo que brindan mayor precision.

Se utilizara las variables de C y de gamma con un valor de 100 y 0.1 respectivamente.

## Entrenamiento del modelo

El entrenamiento del modelo se realizara las siguientes pruebas:
- Un entrenamiento con los 117 features con una muestra de 100000 datos malignos y 100000 datos benignos provenientes de flujos obtenidos con camaras de seguridad y ataques de tipo DDOS. El 80% sera usado en el entrenamiento y 20 para el testing.

- Se repetira el mismo entrenamiento con cada uno de los features.

-Con el analisis de los datos se hara un ultimo entrenamiento con el top de los 5 features que dio mayor precision.

## s 

