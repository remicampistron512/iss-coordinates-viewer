import requests  # type: ignore
import locale
from datetime import datetime

locale.setlocale(locale.LC_TIME, "fr_FR.UTF-8")


print("Informations sur l'ISS")

location_request = requests.get('http://api.open-notify.org/iss-now.json')
location_data = location_request.json()

timestamp = location_data["timestamp"]
date = datetime.fromtimestamp(timestamp)

longitude = location_data["iss_position"]["longitude"]
latitude = location_data["iss_position"]["latitude"]


print(f'Le {date.strftime("%A %d %B %Y à %H:%M:%S")}, l\'ISS se trouve à une longitude de {longitude} et une latitude '
      f'de {latitude}')


crew_request = requests.get('http://api.open-notify.org/astros.json')
print(crew_request.json())

