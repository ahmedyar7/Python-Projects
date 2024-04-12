# ISS Overhead Notification System

This Python script is designed to notify the user via email when the International Space Station (ISS) is overhead their provided location during nighttime.

## Requirements

- Python 3.x
- `requests` library (for making HTTP requests)
- `smtplib` library (for sending emails)
- Access to a Gmail account for sending emails

## Setup

1. **Install Dependencies**: Make sure you have Python installed on your system. You can install the required libraries using pip:

    ```
    pip install requests
    ```

2. **Configuration**: Before running the script, make sure to configure the following variables at the beginning of the script:

    - `YOUR_EMAIL_SMTP_PROTOCOL`: SMTP protocol for your email service provider.
    - `YOUR_EMAIL`: Your email address.
    - `YOUR_PASSWORD`: Your email account password (make sure to keep it secure).
    - Inorder to use password use app password [App Password Tutorial](https://www.youtube.com/watch?v=hXiPshHn9Pw){:target="_blank"}

    - `YOUR_LAT` and `YOUR_LONG`: Your latitude and longitude coordinates. These are used to determine if the ISS is overhead.
    - Inorder to get your location latitude and longitude [Latitude & Longitude](https://latlong.net){:target="_blank"}

3. **Run the Script**: Execute the script in your terminal:

    ```
    python iss_notification.py
    ```

## Functionality

### `iss_overhead()`

This function checks if the ISS is currently passing overhead the provided latitude and longitude coordinates. It does so by making a request to the Open Notify API's `iss-now` endpoint, which provides the current location of the ISS. The function then compares the ISS's coordinates with the provided coordinates, allowing a tolerance of +/- 5 degrees.

### `is_night()`

This function checks if it is currently nighttime at the provided location. It utilizes the Sunrise-Sunset API to fetch the sunrise and sunset times for the given coordinates. Then, it compares the current hour with these times to determine if it is nighttime.

### Notification Loop

The main loop of the script runs indefinitely, checking every hour if both `iss_overhead()` and `is_night()` functions return `True`. If both conditions are met, an email notification is sent using the provided SMTP server and email credentials.

## Note

- Ensure that your email provider allows access via SMTP and that "Less Secure App Access" is enabled for your account.
- The script uses a sleep time of 60 minutes between checks to avoid unnecessary API requests.
