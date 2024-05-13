import requests

def obtener_pelicula(id_pelicula):
    """
    Obtiene los detalles de una película específica de Studio Ghibli por su ID.
    """
    url = f"https://ghibliapi.vercel.app/films/{id_pelicula}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print("Error al obtener la película:", response.status_code)
        return None

# Ejemplo de uso
if __name__ == "__main__":
    id_pelicula = "58611129-2dbc-4a81-a72f-77ddfc1b1b49"  # ID de la película My Neighbor Totoro
    pelicula = obtener_pelicula(id_pelicula)
    if pelicula:
        print("Título:", pelicula["title"])
        print("Descripción:", pelicula["description"])
        print("Director:", pelicula["director"])
