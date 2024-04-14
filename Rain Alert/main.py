import os
from dotenv import load_dotenv, find_dotenv
import requests

dotenv_path = find_dotenv()
load_dotenv(dotenv_path)

API_KEY = os.getenv("API_KEY")
LONGITUDE = os.getenv("LONGITUDE")
LATITUDE = os.getenv("LATITUDE")

ACCOUNT_SID = os.getenv("ACCOUNT_SID")
AUTH_TOKEN = os.getenv("AUTH_TOKEN")
TWILIO_PHONENUMBER = os.getenv("TWILIO_PHONENUMBER")
MY_PHONENUMBER = os.getenv("MY_PHONENUMBER")

API_PARAMETERS = {
    "lat": LATITUDE,
    "lon": LONGITUDE,
    "appid": API_KEY,
    "cnt": 4,
}

response = requests.get(
    url="https://api.openweathermap.org/data/2.5/forecast", params=API_PARAMETERS
)
data = response.json()


for hour_data in data["list"]:
    print(hour_data["weather"][0]["id"])
