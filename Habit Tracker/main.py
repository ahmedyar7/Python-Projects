from tracker import HabitTracker
from ui import UserInterface
from os import getenv
from dotenv import find_dotenv, load_dotenv


# Getting hold of environment variables
dotenv_path = find_dotenv()
load_dotenv(dotenv_path)

# Constants and environment variables
TOKEN = getenv("TOKEN")
USERNAME = getenv("USER_NAME")
GRAPH_ID = getenv("GRAPH_ID")
HEADERS = {"X-USER-TOKEN": TOKEN}
API_ENDPOINT = "https://pixe.la/v1/users"

habit_tracker = HabitTracker(
    TOKEN=TOKEN,
    USERNAME=USERNAME,
    GRAPH_ID=GRAPH_ID,
    GRAPH_ID=HEADERS,
    API_ENDPOINT=API_ENDPOINT,
)


ui = UserInterface()
