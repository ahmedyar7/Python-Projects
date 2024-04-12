import requests
import smtplib
from datetime import datetime
import time

YOUR_EMAIL_SMTP_PROTOCOL = "smtp.gmail.com"
YOUR_EMAIL = "youraddress@email.com"
YOUR_PASSWORD = "your password "

YOUR_LAT = 000000
YOUR_LONG = 000000


def iss_overhead():
    """This function would return true or false based upon wether the ISS align with the provied latitude and longitude"""

    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    # Condition to check wether ISS is over your head or not
    if (YOUR_LAT + 5 <= iss_latitude or YOUR_LAT - 5 <= iss_latitude) or (
        YOUR_LONG + 5 <= iss_longitude or YOUR_LONG - 5 <= iss_longitude
    ):
        return True


def is_night():
    """Checks the sun rise and set timing with the current time(hours) and return boolean value"""

    api_parameters = {
        "lat": YOUR_LAT,
        "lng": YOUR_LONG,
        "formatted": 0,
    }

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


SUBJECT = "ISS Is overhead Loop Up. "
MESSAGE = ""
MINS = 60  # in seconds

while True:
    time.sleep(MINS)
    if iss_overhead() and is_night():
        with smtplib.SMTP(YOUR_EMAIL_SMTP_PROTOCOL) as connection:
            connection.starttls()
            connection.login(YOUR_EMAIL, YOUR_PASSWORD)

            connection.sendmail(
                to_addrs=YOUR_EMAIL,
                from_addr=YOUR_EMAIL,
                msg=f"Subject:{SUBJECT}\n\n{MESSAGE}",
            )
