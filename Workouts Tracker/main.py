from dotenv import find_dotenv, load_dotenv
from os import getenv
import requests

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


def add_workout():
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
    workout = response.json()["exercises"]
    return workout
