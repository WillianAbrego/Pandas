from cProfile import label
from turtle import color
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("avocado.csv")

atlanta = df[df["region"] == "Atlanta"]

precio = atlanta["AveragePrice"]
# toma los datos de precio y aplica una ventana deslizante de 25 muestras y toma la media
# se agrega min_periods =1 para que empieze a ejecutar la operacion sin tener que esperar 30 muestras
precioPromediado = precio.rolling(30, min_periods=1).mean()
volumen = atlanta["Total Volume"]

bolsasAguacate = atlanta["Total Bags"]
sbosas = atlanta["Small Bags"]
lbosas = atlanta["Large Bags"]
xlbosas = atlanta["XLarge Bags"]

plt.subplot(221)
plt.title("Precio Aguacate")
plt.plot(precio, label="Precio", color="green")
plt.plot(precioPromediado, label="Precio Promediado", color="orange")
plt.legend()

plt.subplot(222)
plt.title("Volumen de aguacates")
plt.plot(volumen, label="Volumen total", color="red")
plt.legend()

plt.subplot(223)
plt.title("Bolsas totales de aguacates")
plt.plot(bolsasAguacate, label="Bolsas total", color="blue")
plt.legend()

plt.subplot(224)
plt.title("Bolsas por tamaño ")
plt.plot(sbosas, label="Bolsas - S", color="black")
plt.plot(lbosas, label="Bolsas - L", color="cyan")
plt.plot(xlbosas, label="Bolsas - XL", color="yellow")
plt.legend()

plt.tight_layout()  # espaciar los diferentes elementos para que no se superpongan
plt.show()
