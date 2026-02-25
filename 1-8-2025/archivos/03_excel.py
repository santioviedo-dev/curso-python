import pandas as pd

archivo = "ejemplo.xlsx"

df = pd.read_excel(archivo, sheet_name="ejemplo")

print(df)