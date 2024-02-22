# Importation des modules nécessaires
from flask import Flask, render_template, request
from Prevision_meteo import get_weather_data, get_forecast_data, timestamp_to_datetime
from dotenv import load_dotenv
import os
import sys

# Initialisation de l'application Flask
app = Flask(__name__)
app.static_folder = 'static'
app.template_folder = 'templates'

# Chargement de la clé API depuis la variable d'environnement
api_key = os.getenv('API_KEY')

# Ajout d'un filtre Jinja pour convertir le timestamp en datetime
app.jinja_env.filters['timestamp_to_datetime'] = timestamp_to_datetime

# Définition d'une fonction pour obtenir le chemin des ressources en fonction de l'environnement
# Pour convertir le fichier python en excutable
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except AttributeError:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

# Changement du répertoire de travail vers le répertoire du script
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Chargement des variables d'environnement depuis un fichier .env
load_dotenv(dotenv_path='clé_api.env')

# Définition de la route racine, rendant la page d'accueil
@app.route('/')
def index():
    return render_template('accueil.html')

# Définition de la route /weather pour gérer les données météorologiques
@app.route('/weather', methods=['GET', 'POST'])
def weather():
    # Récupération de la ville depuis le formulaire en cas de soumission avec la méthode POST
    city_query = request.form.get('city') if request.method == 'POST' else None

    if city_query:
        # Récupération des données météorologiques actuelles en utilisant la clé API et la requête de la ville
        weather_data = get_weather_data(api_key, city_query, lang='fr', units='metric')


        # Récupération des données de prévisions en utilisant la clé API et les coordonnées des données météorologiques actuelles
        forecast_data = get_forecast_data(api_key, weather_data['coord']['lat'], weather_data['coord']['lon'], lang='fr', units='metric')

        # Rendu du modèle météo avec les données obtenues
        return render_template('weather.html', city=city_query, weather_data=weather_data, forecast_data=forecast_data)
    else:
        # Rendu du modèle météo avec un message d'erreur si aucune ville n'est trouvée
        return render_template('weather.html', city=city_query, error_message="Aucune ville trouvée")

# Exécution de l'application Flask si ce script est exécuté directement
if __name__ == '__main__':
    app.run(debug=True, port=8080)
