# Workout Tracker

This is a simple Python script that tracks workouts using the Nutritionix API and logs them to a Google Sheets document using the Sheety API.

## Setup

### Environment Variables

Before running the script, ensure you have set the necessary environment variables in a `.env` file. The required variables are:

- `WORKOUTS_APPLICATION_ID`: The application ID for accessing the Nutritionix API.
- `WORKOUTS_API_KEY`: The API key for accessing the Nutritionix API.
- `SHEETY_API_TOKEN`: The API token for accessing the Sheety API.
- `SHEETY_API_URL`: The URL endpoint for the Sheety API.
- `WEIGHT_KG`: Your weight in kilograms.
- `HEIGHT_CM`: Your height in centimeters.
- `AGE`: Your age.

## Installation

Install the required Python packages using pip:

```
pip install -r requirements.txt
```

## Usage

- Run the script and follow the prompts to input your workout details.

```        
python workout_tracker.py
```

## Adding Workouts :
- The script prompts you to enter the exercises you did. It then sends this information to the Nutritionix API to retrieve details about the exercises, including the calories burned.

## Logging Workouts:
- After retrieving workout details from the Nutritionix API, the script logs them to a Google Sheets document using the Sheety API. Each workout entry includes the date, time, exercise name, duration, and calories burned.

## Contributing : 
- Contributions are welcome! If you have suggestions for improving this script or adding new features, feel free to open an issue or submit a pull request.