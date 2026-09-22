import requests  # type: ignore
import locale
from datetime import datetime

# Définit la locale pour l'affichage de la date au bon format
locale.setlocale(locale.LC_TIME, "fr_FR.UTF-8")

print("Informations sur l'ISS")

# Consomme l'api pour les coordonnées
location_request = requests.get('http://api.open-notify.org/iss-now.json')

#Récupère le json
location_data = location_request.json()

#Convertit l'epoch en date lisible
timestamp = location_data["timestamp"]
date = datetime.fromtimestamp(timestamp)

# Récupère les coordonnées
longitude = location_data["iss_position"]["longitude"]
latitude = location_data["iss_position"]["latitude"]

# Consomme l'api pour l'équipage
crew_request = requests.get('http://api.open-notify.org/astros.json')
crew_data = crew_request.json()


print(f'Le {date.strftime("%A %d %B %Y à %H:%M:%S")}, l\'ISS se trouve à une longitude de {longitude} et une latitude '
      f'de {latitude}')


print(f'Il y a {crew_data["number"]} personnes dans l\'espace' )
for people in crew_data["people"]:
    print(f' Equipage : {people["craft"]}, Nom : {people["name"]}')

