import numpy as np
import pandas as pd

# Nahum flores NC 0065
## datos matriz 4 x 3
datos_alumno = [
    [100, 80, 10],
    [90, 70, 7],
    [120, 100, 14],
    [80, 50, 2]
]

# poner nombre a las columnas
# y almacenar la tabla en la variable df dataframe
print(" datos a a partir de una matriz 4 x 3")
df = pd.DataFrame(datos_alumno, columns=["ci", "marcas", "paquete"])
print(df)

# Se ajustan las listas para que todas tengan 6 elementos
alumno_diccionario = {
    "nombre": ["Hugo", "Michelle", "Iker", "Caro", "Ricardo", "Alan"],
    "califa": [60, 90, 100, 80, 70, 85],       # Se agregó un elemento
    "edad":   [67, 15, 16, 16, 16, 18]         # Se eliminó el último elemento sobrante
}

estudiante = pd.DataFrame(alumno_diccionario)
print(estudiante)

print("nahum flores NC 0065")