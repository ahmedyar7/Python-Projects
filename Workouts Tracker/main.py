from dotenv import find_dotenv, load_dotenv
from os import getenv
import requests
from datetime import datetime as dt

dotenv_path = find_dotenv()
load_dotenv(dotenv_path)

# Environment Variables -> Natural Workouts
WORKOUTS_APPLICATION_ID = getenv("WORKOUTS_APPLICATION_ID")
WORKOUTS_API_KEY = getenv("WORKOUTS_API_KEY")

# Environment Variables -> SHEETY
SHEETY_API_TOKEN = getenv("SHEETY_API_TOKEN")
SHEETY_API_URL = getenv("SHEETY_API_URL")

# print(SHEETY_API_URL)
# print(SHEETY_API_TOKEN)

# Environment Variable -> Personal
WEIGHT_KG = getenv("WEIGHT_KG")
HEIGHT_CM = getenv("HEIGHT_CM")
AGE = getenv("AGE")


# CONSTANTS:
WORKOUT_URL = "https://trackapi.nutritionix.com/v2/natural/exercise"


def add_workout(text):
    """This function will add the workouts"""

    headers = {
        "x-app-id": WORKOUTS_APPLICATION_ID,
        "x-app-key": WORKOUTS_API_KEY,
        "x-remote-user-id": "0",
    }
    body = {
        "query": "I ran 1 mile",
        "weight_kg": WEIGHT_KG,
        "height_cm": HEIGHT_CM,
        "age": AGE,
    }

    response = requests.post(url=WORKOUT_URL, json=body, headers=headers)
    return response.json()["exercises"]
    # return workout


print(add_workout(text="I ran 3 miles"))

# data_dict = {
#     "tag_id": 317,
#     "user_input": "ran",
#     "duration_min": 10.01,
#     "met": 9.8,
#     "nf_calories": 114.45,
#     "photo": {
#         "highres": "https://d2xdmhkmkbyw75.cloudfront.net/exercise/317_highres.jpg",
#         "thumb": "https://d2xdmhkmkbyw75.cloudfront.net/exercise/317_thumb.jpg",
#         "is_user_uploaded": False,
#     },
#     "compendium_code": 12050,
#     "name": "running",
#     "description": "None",
#     "benefits": "None",
# }

# TODO: Add the worout in the google sheet by using the shetty:


def add_entry(entry):

    body = {
        "workout": {
            "date": dt.now().strftime("%Y-%m-%d"),
            "time": dt.now().strftime("%I-%M-%p"),
            "exercise": entry["user_input"].capitalize(),
            "duration": f"{entry['duration_min']} min",
            "calories": f"{entry['nf_calories']} kcal",
        }
    }
    print(body)

    headers = {"Authorization": f"Bearer {SHEETY_API_TOKEN}"}
    response = requests.post(url=SHEETY_API_URL, json=body, headers=headers)
    response.raise_for_status()
    print(response.content)


# add_entry(entry=data_dict)
