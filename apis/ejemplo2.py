import requests

# Ejemplo avanzado: consumo de la API gratuita "OpenWeatherMap" (https://open-meteo.com)
# Esta API devuelve el clima actual por coordenadas (no requiere API key)

def consultar_clima(lat, lon):
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": lat,
        "longitude": lon,
        "current_weather": True
    }
    respuesta = requests.get(url, params=params)
    datos = respuesta.json()  # Diccionario con los datos del clima
    return datos

if __name__ == "__main__":
    print("Consulta de clima actual por coordenadas")
    lat = float(input("Ingrese la latitud: "))
    lon = float(input("Ingrese la longitud: "))
    resultado = consultar_clima(lat, lon)
    print("\nDatos recibidos de la API:")
    print(resultado)
    # Mostrar datos principales de clima si existen
    clima = resultado.get("current_weather", {})
    if clima:
        print(f"\nTemperatura: {clima.get('temperature', 'N/A')}°C")
        print(f"Viento: {clima.get('windspeed', 'N/A')} km/h")
        print(f"Dirección del viento: {clima.get('winddirection', 'N/A')}°")
        print(f"Condición: {clima.get('weathercode', 'N/A')}")
    else:
        print("No se encontraron datos de clima para esas coordenadas.")
