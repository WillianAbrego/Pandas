import pandas as pd

df = pd.read_csv("avocado.csv", index_col=["Date"])
print(df.head(4))
