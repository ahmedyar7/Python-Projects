from tracker import HabitTracker

from os import getenv
from dotenv import find_dotenv, load_dotenv


# Getting hold of environment variables
dotenv_path = find_dotenv()
load_dotenv(dotenv_path)

# Constants and environment variables
TOKEN = getenv("TOKEN")
USERNAME = getenv("USER_NAME")
GRAPH_ID = getenv("GRAPH_ID")
HEADERS = {
    "X-USER-TOKEN": TOKEN,
}
API_ENDPOINT = "https://pixe.la/v1/users"
hbt = HabitTracker(TOKEN, USERNAME, GRAPH_ID, HEADERS, API_ENDPOINT)

# hbt.create_graph()
# print(type(hbt.todays_date()))
# hbt.todays_date()
# hbt.create_pixel()

# update_pixel_amount = input("Enter Amount of pixel you want to update: ")
# hbt.update_pixel(amount=update_pixel_amount)
hbt.delete_pixel()
