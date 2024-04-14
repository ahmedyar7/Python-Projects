# Rain Alert 

This Python script utilizes the OpenWeatherMap API and Twilio to send an SMS notification if rain is expected in a specified location. It fetches weather forecast data for the given coordinates and checks if any of the forecasted weather conditions indicate rain. If rain is predicted, it sends an SMS message using Twilio to remind the user to bring an umbrella.

## Prerequisites

Before running the script, ensure you have the following:

- Python installed on your system (version 3.x)
- An OpenWeatherMap API key. You can sign up for free and get your API key from [OpenWeatherMap](https://openweathermap.org/api).
- A Twilio account. You can sign up for free and get your Account SID, Auth Token, and a Twilio phone number from [Twilio](https://www.twilio.com/try-twilio).
- Coordinates (latitude and longitude) of the location you want to check for rain. You can find coordinates for your location using tools like Google Maps.

## Setup

1. Clone or download the repository to your local machine.
2. Install the required Python packages by running:
3. Create a `.env` file in the project directory and add the following variables:
API_KEY=your_openweathermap_api_key
LONGITUDE = longitude_of_your_location
LATITUDE = latitude_of_your_location
ACCOUNT_SID = your_twilio_account_sid
AUTH_TOKEN = your_twilio_auth_token
TWILIO_PHONENUMBER = your_twilio_phone_number
MY_PHONENUMBER = your_phone_number_to_receive_sms

Replace `your_openweathermap_api_key`, `longitude_of_your_location`, `latitude_of_your_location`, `your_twilio_account_sid`, `your_twilio_auth_token`, `your_twilio_phone_number`, and `your_phone_number_to_receive_sms` with your actual values.

## Usage

Run the script `weather_sms_notifier.py` using Python:


The script will fetch the weather forecast for the specified location and send an SMS notification if rain is expected. You will receive the SMS on the phone number specified in the `.env` file.

## Customization

- You can modify the `cnt` parameter in the `API_PARAMETERS` dictionary to adjust the number of forecasted hours to check for rain.
- Customize the SMS message in the `body` parameter of the `client.messages.create()` method to suit your preferences.

## Notes

- This script is for demonstration purposes and may require modifications for use in production environments.
- Ensure you comply with the terms of service of both OpenWeatherMap and Twilio when using their services.
- Handle exceptions and errors gracefully in a production environment to improve reliability.

## Automate The Script:
- By using [PythonAnywhere](https://www.pythonanywhere.com/)