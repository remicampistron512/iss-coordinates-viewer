import requests  # type: ignore

print("Informations sur l'ISS")

location_request = requests.get('http://api.open-notify.org/iss-now.json')
print(location_request.json())

crew_request = requests.get('http://api.open-notify.org/astros.json')
print(crew_request.json())