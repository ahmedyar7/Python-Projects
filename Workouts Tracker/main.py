from dotenv import find_dotenv, load_dotenv
from os import getenv

# TODO : Get hold of the requried credentials for the workouts API and Sheety api

dotenv_path = find_dotenv()
load_dotenv(dotenv_path)

# Environment Variables -> Natural Workouts
WORKOUTS_APPLICATION_ID = getenv("WORKOUTS_APPLICATION_ID")
WORKOUTS_API_KEY = getenv("WORKOUTS_API_KEY")

# Environment Variables -> SHEETY
SHEETY_API_TOKEN = getenv("SHEETY_API_TOKEN")
SHEETY_API_URL = getenv("SHEETY_API_URL")
