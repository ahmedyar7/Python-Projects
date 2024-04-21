from os import getenv
from dotenv import find_dotenv, load_dotenv
from requests import get

load_dotenv(dotenv_path=find_dotenv())
API_KEY = getenv("API_KEY")
HEADER = {
    "apikey": API_KEY,
}


currency_codes = [
    "USD",
    "EUR",
    "GBP",
    "JPY",
    "CAD",
    "AUD",
    "CHF",
    "CNY",
    "SEK",
    "NZD",
    "MXN",
    "SGD",
    "HKD",
    "NOK",
    "KRW",
    "TRY",
    "RUB",
    "INR",
    "BRL",
    "ZAR",
]
converted_to_currency = ",".join(currency_codes)


def currency_converter(base):
    parameters = {
        "base_currency": f"{base}",
        "currencies": f"{converted_to_currency}",
    }

    API_ENDPOINT = "https://api.freecurrencyapi.com/v1/latest"
    response = get(url=API_ENDPOINT, params=parameters, headers=HEADER)

    data = response.json()["data"]

    del data["USD"]
    for key, value in data.items():
        print(f"{key}:{value}")


while True:

    base = input("Enter the currency: Or press q to quit ").upper()

    if base == "Q":
        print("Thank You For using")
        break
    elif base == "":
        print("Invalid Input")
        continue

    currency_converter(base=base)
