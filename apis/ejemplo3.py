import requests

# Ejemplo: consumo de la API pública de Rick and Morty (https://rickandmortyapi.com)
# Obtiene información de personajes por nombre

def buscar_personaje(nombre):
    url = "https://rickandmortyapi.com/api/character/"
    params = {"name": nombre}
    respuesta = requests.get(url, params=params)
    datos = respuesta.json()  # Diccionario con los datos
    return datos

if __name__ == "__main__":
    nombre = input("Ingrese el nombre del personaje: ")
    resultado = buscar_personaje(nombre)
    print("\nDatos recibidos de la API:")
    print(resultado)
    # Mostrar información principal si hay resultados
    personajes = resultado.get("results", [])
    if personajes:
        for p in personajes:
            print(f"\nNombre: {p['name']}")
            print(f"Estado: {p['status']}")
            print(f"Especie: {p['species']}")
            print(f"Género: {p['gender']}")
            print(f"Origen: {p['origin']['name']}")
            print(f"Imagen: {p['image']}")
    else:
        print("No se encontraron personajes con ese nombre.")
