from datetime import datetime
import requests
import pytz

def get_weather_data(api_key, city_query, units='metric', lang='fr'):
    """
    Obtient les données météorologiques actuelles pour une ville spécifiée.

    Arguments:
        api_key (str): Clé API pour l'accès à l'API OpenWeatherMap.
        city_query (str): Nom de la ville pour laquelle obtenir les données météorologiques.
        units (str): Unités de mesure pour la température. Par défaut, 'metric' pour Celsius.
        lang (str): Langue des données météorologiques. Par défaut, 'fr' pour le français.

    Renvois:
        dict ou None: Les données météorologiques actuelles au format JSON si la requête réussit, sinon None.
    """
    city_search_data = search_cities(api_key, city_query)
    
    if city_search_data:
        latitude = city_search_data[0]['lat']
        longitude = city_search_data[0]['lon']

        base_url = "https://api.openweathermap.org/data/2.5/weather"
        params = {
            "lat": latitude,
            "lon": longitude,
            "appid": api_key,
            "lang": lang,
            "units": units
        }

        response = requests.get(base_url, params=params)

        if response.status_code == 200:
            weather_data = response.json()
            return weather_data
        else:
            print(f"Error: {response.status_code}")
            return None
    else:
        print("Aucune ville trouvée.")
        return None

def get_forecast_data(api_key, latitude, longitude, units='metric', lang='fr'):
    """
    Obtient les données de prévision météorologique pour une localisation spécifiée.

    Arguments:
        api_key (str): Clé API pour l'accès à l'API OpenWeatherMap.
        latitude (float): Latitude de la localisation.
        longitude (float): Longitude de la localisation.
        units (str): Unités de mesure pour la température. Par défaut, 'metric' pour Celsius.
        lang (str): Langue des données de prévision. Par défaut, 'fr' pour le français.

    Renvois:
        dict ou None: Les données de prévision météorologique au format JSON si la requête réussit, sinon None.
    """
    base_url = "https://api.openweathermap.org/data/2.5/forecast"
    params = {
        "lat": latitude,
        "lon": longitude,
        "appid": api_key,
        "lang": lang,
        "units": units
    }

    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        forecast_data = response.json()

        filtered_forecast = []
        for forecast in forecast_data['list']:
            forecast_time = datetime.utcfromtimestamp(forecast['dt'])
            if forecast_time.hour == 12: #12 pour obtenir les prévisions de 13h vu qu'il y a décalage
                filtered_forecast.append(forecast)

        forecast_data['list'] = filtered_forecast

        return forecast_data
    else:
        print(f"Error: {response.status_code}")
        return None

def search_cities(api_key, query, limit=5):
    """
    Recherche les villes correspondant à une requête.

    Arguments:
        api_key (str): Clé API pour l'accès à l'API OpenWeatherMap.
        query (str): Terme de recherche pour les villes.
        limit (int): Limite du nombre de résultats. Par défaut, 5.

    Renvois:
        list ou None: Liste des données des villes au format JSON si la requête réussit, sinon None.
    """
    base_url = "http://api.openweathermap.org/geo/1.0/direct"
    params = {
        "q": query,
        "limit": limit,
        "appid": api_key
    }

    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        city_data = response.json()
        return city_data
    else:
        print(f"Error: {response.status_code}")
        return None

def timestamp_to_datetime(timestamp, timezone='Europe/Paris'):
    """
    Convertit un timestamp Unix en objet datetime avec un fuseau horaire spécifié.

    Arguments:
        timestamp (int): Timestamp Unix à convertir.
        timezone (str): Fuseau horaire. Par défaut, 'Europe/Paris'.

    Renvois:
        str: Représentation formatée de l'objet datetime en chaîne de caractères.
    """
    utc_time = datetime.utcfromtimestamp(timestamp)
    paris_timezone = pytz.timezone(timezone)
    local_time = utc_time.replace(tzinfo=pytz.utc).astimezone(paris_timezone)
    return local_time.strftime('%Y-%m-%d %H:%M:%S')
