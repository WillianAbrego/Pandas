import pandas as pd

personas = {
    "nombre": ["Dimas", "Juan", "Ana"],
    "edad": [23, 24, 25],
    "pais": ["España", "Mexico", "Chile"]
}

df = pd.DataFrame(personas)
print(df)
