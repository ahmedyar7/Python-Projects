from dotenv import find_dotenv, load_dotenv
from os import getenv
import requests
from datetime import datetime as dt


# * -------------------------------- ENVIRONMENT VARIABLES & CONSTANTS ----------------------------------------#
dotenv_path = find_dotenv()
load_dotenv(dotenv_path)

# Environment Variables -> Natural Workouts
WORKOUTS_APPLICATION_ID = getenv("WORKOUTS_APPLICATION_ID")
WORKOUTS_API_KEY = getenv("WORKOUTS_API_KEY")

# Environment Variables -> SHEETY
SHEETY_API_TOKEN = getenv("SHEETY_API_TOKEN")
SHEETY_API_URL = getenv("SHEETY_API_URL")


# Environment Variable -> Personal
WEIGHT_KG = getenv("WEIGHT_KG")
HEIGHT_CM = getenv("HEIGHT_CM")
AGE = getenv("AGE")

# CONSTANTS:
WORKOUT_URL = "https://trackapi.nutritionix.com/v2/natural/exercise"


# * ------------------- ADD WORKOUTS ------------------ #


while True:

    print("What exercies you did: ")
    my_workout = input(">> ")

    if my_workout == "":
        print("What exercies you did: ")
    else:
        break


def add_workout(text):
    """This function will add the workouts"""

    headers = {
        "x-app-id": WORKOUTS_APPLICATION_ID,
        "x-app-key": WORKOUTS_API_KEY,
        "x-remote-user-id": "0",
    }
    body = {
        "query": my_workout,
        "weight_kg": WEIGHT_KG,
        "height_cm": HEIGHT_CM,
        "age": AGE,
    }

    response = requests.post(url=WORKOUT_URL, json=body, headers=headers)
    workout = response.json()["exercises"]
    return workout


# * ------------------ ADD TO GOOGLE SHEETS ------------- #


def add_entry(entry):

    body = {
        "workout": {
            "date": dt.now().strftime("%Y-%m-%d"),
            "time": dt.now().strftime("%I-%M-%p"),
            "exercise": entry["user_input"],
            "duration": entry["duration_min"],
            "calories": entry["nf_calories"],
        }
    }

    HEADERS = {"Authorization": f"Bearer {SHEETY_API_TOKEN}"}

    response = requests.post(url=SHEETY_API_URL, json=body, headers=HEADERS)
    response.raise_for_status()


workout_list = add_workout(text=my_workout)

if workout_list is not None:
    for exercises in workout_list:
        add_entry(entry=exercises)
