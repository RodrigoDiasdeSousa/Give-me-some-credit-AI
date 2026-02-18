import pandas as pd

# Caminho relativo para o arquivo dentro da pasta data
df = pd.read_csv("data/cs-training.csv")

# Ver as primeiras linhas
print(df.head())
