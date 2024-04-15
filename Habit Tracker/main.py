import requests
from os import getenv
from dotenv import find_dotenv, load_dotenv
from datetime import datetime as dt

# Getting hold of environment variables
dotenv_path = find_dotenv()
load_dotenv(dotenv_path)

# Constants and environment variables
TOKEN = getenv("TOKEN")
USERNAME = getenv("USER_NAME")
GRAPH_ID = getenv("GRAPH_ID")
HEADERS = {
    "X-USER-TOKEN": TOKEN,
}
API_ENDPOINT = "https://pixe.la/v1/users"


def create_user():

    user_data = {
        "token": TOKEN,
        "username": USERNAME,
        "agreeTermsOfService": "yes",
        "notMinor": "yes",
    }

    response = requests.post(url=f"{API_ENDPOINT}", json=user_data)
    return response


def create_graph():
    """This function would create the graph"""

    graph_endpoint_data = {
        "X-USER-TOKEN": TOKEN,
        "id": GRAPH_ID,
        "name": "Reading",
        "unit": "commit",
        "type": "int",
        "color": "ajisai",
    }

    graph_endpoint = f"{API_ENDPOINT}/{USERNAME}/graphs"

    response = requests.post(
        url=graph_endpoint, json=graph_endpoint_data, headers=HEADERS
    )
    return response


def todays_date() -> str:
    now_time = dt.now()
    today = now_time.strftime(format="%Y%m%d")
    return today


def create_pixel():

    pixel_endpoint_data = {
        "date": todays_date(),
        "quantity": "5",
    }

    pixel_endpoint = f"{API_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}"
    response = requests.post(
        url=pixel_endpoint, json=pixel_endpoint_data, headers=HEADERS
    )
    return response


def update_pixel(amount):
    """This will update the graph based upon provided amount"""

    update_pixel_data = {
        "quantity": "22",
    }

    update_pixel_endpoint = (
        f"{API_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}/{todays_date()}"
    )

    response = requests.put(
        url=update_pixel_endpoint, json=update_pixel_data, headers=HEADERS
    )


def delete_pixel():
    """This will delete the pixel from the Graph"""

    delete_pixel_endpoint = (
        f"{API_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}/{todays_date()}"
    )
    response = requests.delete(url=delete_pixel_endpoint, headers=HEADERS)
    return response
