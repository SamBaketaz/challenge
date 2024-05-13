import requests

user_id = 1  # ID del usuario que deseas obtener
url = f'http://localhost:5000/usuarios/{user_id}'
response = requests.get(url)

print(response.json())  # Imprime la respuesta del servidor