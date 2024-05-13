import requests

user_id = 1  # ID del usuario que deseas actualizar
url = f'http://localhost:5000/usuarios/{user_id}'
data = {'username': 'nuevo_nombre', 'role': 'people'}
response = requests.put(url, json=data)

print(response.json())  # Imprime la respuesta del servidor