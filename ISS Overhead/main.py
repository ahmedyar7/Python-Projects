import requests
import smtplib
from datetime import datetime

# TODO : Make a function that return boolean value called iss_overhead()
# TODO: Then after getting hold of the lat and long of the ISS data compare it with the my own lat and long with margin of 5 degrees
# TODO: After compairsinon then give or return true or false


MY_LAT = 30.179840
MY_LONG = 66.974976


def iss_overhead():
    """This function would return true or false based upon wether the ISS align with the provied latitude and longitude"""

    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    if (MY_LAT + 5 <= iss_latitude or MY_LAT - 5 <= iss_latitude) or (
        MY_LONG + 5 <= iss_longitude or MY_LONG - 5 <= iss_longitude
    ):
        return True


# def is_night():
#     """Checks the sun rise and set timing with the current time(hours) and return boolean value"""

#     api_parameters = {
#         "lat": MY_LAT,
#         "lng": MY_LONG,
#         "formatted": 0,
#     }

#     time_now = datetime.now().hour

#     response = requests.get(
#         url="https://api.sunrise-sunset.org/json", params=api_parameters
#     )
#     response.raise_for_status()
#     data = response.json()

#     sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
#     sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

#     # Condition that check wether its night or not:
#     if time_now >= sunset and time_now <= sunrise:
#         return True
