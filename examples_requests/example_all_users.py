import requests

url = 'http://localhost:5000/usuarios'
response = requests.get(url)

print(response.json())  # Imprime la respuesta del servidor