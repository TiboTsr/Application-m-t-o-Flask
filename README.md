# Application Météo

Cette application web, développée en utilisant Flask, permet d'afficher les données météorologiques actuelles et les prévisions pour une ville spécifique en se basant sur l'API OpenWeatherMap.

## Installation

1. Installez les modules nécessaires (ceux déjà présents dans la bibliothèque standard de Python ne nécessitent pas d'installation supplémentaire):
   - Flask
   - datetime * 
   - request *
   - pytz
   - dotenv *
   - os * 
   - sys *

2. Obtenez votre clé API OpenWeatherMap :
    - Inscrivez-vous sur [OpenWeatherMap](https://openweathermap.com) pour obtenir une clé API gratuite.

3. Modifiez le fichier clé_api.env pour y ajouter votre clé API OpenWeatherMap
    ```bash
    API_KEY=VotreCleAPIOpenWeatherMap
    ```

## Utilisation 

1. Exécutez le fichier Main.py 
    ```bash
    python Main.py
    ```

2. Ou exécutez directement le fichier Application_météo.exe pour lancer le serveur directement.

3. Accédez à l'application dans votre navigateur en visitant http://localhost:8080/.

4. Entrez le nom d'une ville dans le formulaire et appuyez sur "Obtenir la météo".

## Fonctionnalités 

- Affiche les données météorologiques actuelles, incluant la température, la météo, l'humidité, la vitesse du vent, etc.

- Fournit des prévisions météorologiques pour les prochains jours.

## Structure du projet

- app.py: Fichier principal contenant le code Flask pour l'application.

- Prevision_meteo.py: Module contenant les fonctions pour obtenir les données météorologiques à partir de l'API OpenWeatherMap.

- templates/: Dossier contenant les modèles HTML pour l'interface utilisateur.

- static/: Dossier contenant les fichiers CSS pour la mise en page et le logo des pages.
