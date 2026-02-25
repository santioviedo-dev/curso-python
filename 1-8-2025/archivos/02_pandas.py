# import pandas as pd


# # try:
# #     df = pd.read_csv('mi_csv.csv')
# #     print(df.describe())
# #     # print(df['nombre'])
# #     # print(df.iloc[0])
# # except FileNotFoundError:
# #     print("El archivo 'mi_csv.csv' no se encuentra.")
# # # try:
# # #     df = pd.read_csv('mi_csv.csv', dtype={'edad': int})
# # #     print(df)
# # #     # print(df['nombre'])
# # #     # print(df.iloc[0])
# # # except FileNotFoundError:
# # #     print("El archivo 'mi_csv.csv' no se encuentra.")


# # datos = {
# #     'nombre': ['Ana', 'Luis', 'Marta'],
# #     'apellido': ['Gomez', 'Perez', 'Lopez'],
# #     'edad': [28, 34, 22],
# # }

# # df = pd.DataFrame(datos)

# # df.head(2).to_csv('ejemplo.csv', encoding='utf-8', index=False, header=False)


# df = pd.read_csv('mi_csv.csv')

# # df = df.sort_values(by='edad', ascending=False)
# # print(df.groupby('nombre').mean())

# # df = df.fillna("Sin valor")
# # df.to_csv('mi_csv.csv', index=False, encoding='utf-8')

# # mayores = df[df['nombre'] == 'Santiago']

# # print(mayores)

# # df['edad'] = df['edad'] * 2

