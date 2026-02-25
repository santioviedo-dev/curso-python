"""
GET: Trae una petición HTTP GET y devuelve un mensaje de éxito.
POST: hace una petición HTTP POST enviando datos y devuelve un mensaje de éxito.
PUT: hace una petición HTTP PUT actualizando datos y devuelve un mensaje de éxito.

status_code: 200 para todas las peticiones exitosas.
status_code: 400 para peticiones con errores.
"""


# import requests

# # respuesta = requests.get('https://jsonplaceholder.typicode.com/posts/1')
# # print(respuesta.json()['body'])


# post = {
#     "userId": 1,
#     "title": "foo",
#     "body": "bar",
# }

# respuesta = requests.post('https://jsonplaceholder.typicode.com/posts', json=post)

# print(respuesta.status_code)
# print(respuesta.json()["id"])


# from openai import OpenAI
# client = OpenAI()

# response = client.responses.create(
#     model="gpt-3.5-turbo",
#     input="Decime un poema."
# )

# print(response.output_text)
