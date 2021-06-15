from dotenv import dotenv_values
import requests

config = dotenv_values(".env")
API_KEY = config['API_KEY']

# curl -X GET "https://sensores.grafcan.es/api/v1.0/datastreams/" -H "accept: application/json"

url = "https://sensores.grafcan.es/api/v1.0/datastreams/"
headers = {
    "accept": "application/json",
    "Authorization": "Api-Key " + API_KEY
}

r = requests.get(url, headers=headers)
