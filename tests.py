import unittest
from unittest.mock import MagicMock
from Prevision_meteo import get_weather_data, get_forecast_data, search_cities, timestamp_to_datetime


class YourModuleTests(unittest.TestCase):
    def setUp(self):
        self.api_key = '...'  # Remplacez par votre véritable clé API openweathermap ici

    def test_get_weather_data(self):
        city_query = 'Paris'
        weather_data = get_weather_data(self.api_key, city_query)
        self.assertIsNotNone(weather_data)

    def test_get_forecast_data(self):
        latitude = 48.8566
        longitude = 2.3522
        forecast_data = get_forecast_data(self.api_key, latitude, longitude)
        self.assertIsNotNone(forecast_data)
        # Ajoutez d'autres assertions en fonction des résultats attendus

    def test_search_cities(self):
        query = 'Paris'
        city_data = search_cities(self.api_key, query)
        self.assertIsNotNone(city_data)
        # Ajoutez d'autres assertions en fonction des résultats attendus

    def test_timestamp_to_datetime(self):
        timestamp = 1643155200  # Exemple de timestamp (2022-01-26 00:00:00 UTC)
        result = timestamp_to_datetime(timestamp)
        self.assertEqual(result, '2022-01-26 01:00:00')  # En supposant un décalage horaire de +1 (Europe/Paris)

if __name__ == '__main__':
    unittest.main()
