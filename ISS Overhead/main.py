import requests
import smtplib
from datetime import datetime

# TODO : Compare the sunrise and sunset timing with the current time with the
# TODO : Make a function that compaire and the return true of false accordingly


MY_LAT = 30.179840
MY_LONG = 66.974976

api_parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}


def is_night():
    """Checks the sun rise and set timing with the current time(hours) and return boolean value"""

    time_now = datetime.now().hour

    response = requests.get(
        url="https://api.sunrise-sunset.org/json", params=api_parameters
    )
    response.raise_for_status()
    data = response.json()

    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    # Condition that check wether its night or not:
    if time_now >= sunset and time_now <= sunrise:
        return True


# print(sunrise)
# print(sunset)
