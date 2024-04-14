import os
from dotenv import load_dotenv, find_dotenv
import requests
from twilio.rest import Client

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

will_rain: bool = False
client = Client(ACCOUNT_SID, AUTH_TOKEN)

for hour_data in data["list"]:
    weather_code = hour_data["weather"][0]["id"]

    if weather_code < 700:
        will_rain = True

if will_rain:
    message = client.messages.create(
        from_=TWILIO_PHONENUMBER,
        to=MY_PHONENUMBER,
        body="Rain Expected, Don't Forget to Bring Umbella 🌧☔",
    )

print(message.status)
