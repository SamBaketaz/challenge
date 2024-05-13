import requests

url = 'http://localhost:5000/usuarios'
data = {'prueba_creacion_usuario': 'creacion_usuario', 'role': 'films'}
response = requests.post(url, json=data)

print(response.json())  # Imprime la respuesta del servidor