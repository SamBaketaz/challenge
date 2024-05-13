import requests

user_id = 1  # ID del usuario que deseas eliminar
url = f'http://localhost:5000/usuarios/{user_id}'
response = requests.delete(url)

print(response.json())  # Imprime la respuesta del servidor