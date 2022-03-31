from cProfile import label
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

df = pd.read_csv("avocado.csv")
# print(df.head(5))

# print(df["region"][:49])

chicago = df[df["region"] == "Chicago"]
# print(chicago.head(5))
chicago = chicago.set_index("Date")  # Cambia indice numerico a  Date
chicago = chicago.sort_values(by="Date")  # ordenado por fecha

# print(chicago.head(5))

MAX_SAMPLES = 100
precio = chicago["AveragePrice"][:MAX_SAMPLES]
cantidad = chicago["Total Volume"][:MAX_SAMPLES]

plt.plot(precio, label="Precio Medio")
plt.plot(cantidad, label="Volumen total")
plt.title("Precio de los aguacates vs tiempo")
plt.xlabel("Fecha")
plt.xticks(rotation=90)
plt.ylabel("Precio en $")
plt.legend()
plt.show()
