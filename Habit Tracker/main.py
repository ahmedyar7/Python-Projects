import requests
from os import getenv
from dotenv import find_dotenv, load_dotenv
from datetime import datetime as dt

dotenv_path = find_dotenv()
load_dotenv(dotenv_path)

TOKEN = getenv("TOKEN")
USERNAME = getenv("USER_NAME")
GRAPH_ID = getenv("GRAPH_ID")


api_endpoint = "https://pixe.la/v1/users"

user_data = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}


# response = requests.post(url=f"{api_endpoint}", json=user_data)
# print(response.raise_for_status)

HEADERS = {
    "X-USER-TOKEN": TOKEN,
}

graph_endpoint_data = {
    "X-USER-TOKEN": TOKEN,
    "id": GRAPH_ID,
    "name": "Reading",
    "unit": "commit",
    "type": "int",
    "color": "ajisai",
}

graph_endpoint = f"{api_endpoint}/{USERNAME}/graphs"

# response = requests.post(url=graph_endpoint, json=graph_endpoint_data, headers=HEADERS)
# print(response.text)

# TODO : Make a pixel to the graph


now_time = dt.now()
today = now_time.strftime(format="%Y%m%d")

pixel_endpoint_data = {
    "date": today,
    "quantity": "5",
}

pixel_endpoint = f"{api_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
response = requests.post(url=pixel_endpoint, json=pixel_endpoint_data, headers=HEADERS)
