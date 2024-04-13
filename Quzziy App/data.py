import requests

api_paramters = {
    "amount": 10,
    "type": "boolean",
}

response = requests.get(url="https://opentdb.com/api.php", params=api_paramters)

data = response.json()
question_data = data["results"]
