from numpy import column_stack
import pandas as pd

# Metodo 1: lista de Listas

columns = ["Marca", "Precio", "Disponibilidad"]
cocheA = ["Mercedes", 10e3, True]
cocheB = ["BMW", 20e3, False]

df = pd.DataFrame([cocheA, cocheB], columns=columns)
print(df)

# Metodo 2: Usando ZIP

marcas = [
    "Audi",
    "BMW",
    "Mercedes",
    "Mercedes"
]
precio = [
    20e3,
    30e3,
    40e3,
    25e3
]

disponibilidad = [
    True,
    False,
    True,
    False
]

df = pd.DataFrame(
    list(zip(marcas, precio, disponibilidad)),
    columns=["marca", "precio", "disponibilidad"]
)
print(df)

# Metodo 3: Usando un diccionario


marcas = [
    "Audi",
    "BMW",
    "Mercedes",
    "Mercedes"
]
precio = [
    20e3,
    30e3,
    40e3,
    25e3
]

disponibilidad = [
    True,
    False,
    True,
    False
]

diccionario = {
    "marcas": marcas,
    "precio": precio,
    "disponibilidad": disponibilidad
}

dfdiccionario = pd.DataFrame(diccionario)
print(dfdiccionario)
