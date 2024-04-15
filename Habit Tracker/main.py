import requests
from os import getenv
from dotenv import find_dotenv, load_dotenv

dotenv_path = find_dotenv()
load_dotenv(dotenv_path)

TOKEN = getenv("TOKEN")
USERNAME = getenv("USER_NAME")


# TODO: Make the user endpoint and user parameter on the habit trackers
api_endpoint = "https://pixe.la/v1/users"

user_data = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}


response = requests.post(url=f"{api_endpoint}", json=user_data)
print(response.raise_for_status)
