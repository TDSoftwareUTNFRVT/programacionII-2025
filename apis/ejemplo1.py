import requests

# Ejemplo sencillo: consumo de la API "Agify" (https://agify.io)
# Esta API predice la edad a partir de un nombre

def consultar_edad(nombre):
    url = "https://api.agify.io"
    p= {"name": nombre}
    respuesta = requests.get(url, params=p)
    datos = respuesta.json()  # Los datos vienen en formato diccionario
    print(f"Respuesta de la API: {datos}")
    return datos

if __name__ == "__main__":
    nombre = input("Ingrese un nombre: ")
    resultado = consultar_edad(nombre)
    print("\nDatos recibidos de la API:")
    print(resultado)
    print(f"\nEl nombre '{nombre}' tiene una edad estimada de: {resultado.get('age', 'No disponible')}")
