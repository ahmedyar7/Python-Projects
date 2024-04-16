import requests
from datetime import datetime as dt
import webbrowser


class HabitTracker:

    def __init__(self, TOKEN, USERNAME, GRAPH_ID, HEADERS, API_ENDPOINT):

        # Consturctor Constants:
        self.TOKEN = TOKEN
        self.USERNAME = USERNAME
        self.GRAPH_ID = GRAPH_ID
        self.HEADERS = HEADERS
        self.API_ENDPOINT = API_ENDPOINT

        # Constructor Function:
        self.create_user()
        self.create_graph()
        self.todays_date()

    def create_user(self):

        self.user_data = {
            "token": self.TOKEN,
            "username": self.USERNAME,
            "agreeTermsOfService": "yes",
            "notMinor": "yes",
        }

        self.response = requests.post(url=f"{self.API_ENDPOINT}", json=self.user_data)

    def create_graph(self):
        """This function would create the graph"""

        graph_endpoint_data = {
            "X-USER-TOKEN": self.TOKEN,
            "id": self.GRAPH_ID,
            "name": "Reading",
            "unit": "commit",
            "type": "int",
            "color": "ajisai",
        }

        self.graph_endpoint = f"{self.API_ENDPOINT}/{self.USERNAME}/graphs"

        self.response = requests.post(
            url=self.graph_endpoint,
            json=graph_endpoint_data,
            headers=self.HEADERS,
        )

    def todays_date(self) -> str:
        """This function would return the current date"""

        now_time = dt.now()
        today = str(now_time.strftime(format="%Y%m%d"))
        return today

    def create_pixel(self):
        "This function would create pixel onto graph"

        pixel_endpoint_data = {
            "date": self.todays_date(),
            "quantity": "5",
        }

        pixel_endpoint = f"{self.API_ENDPOINT}/{self.USERNAME}/graphs/{self.GRAPH_ID}"
        self.response = requests.post(
            url=pixel_endpoint,
            json=pixel_endpoint_data,
            headers=self.HEADERS,
        )

    def update_pixel(self, amount):
        """This will update the graph based upon provided amount"""

        self.update_pixel_data = {
            "quantity": amount,
        }

        update_pixel_endpoint = f"{self.API_ENDPOINT}/{self.USERNAME}/graphs/{self.GRAPH_ID}/{self.todays_date()}"

        self.response = requests.put(
            url=update_pixel_endpoint,
            json=self.update_pixel_data,
            headers=self.HEADERS,
        )

    def delete_pixel(self):
        """This will delete the pixel from the Graph"""

        self.delete_pixel_endpoint = f"{self.API_ENDPOINT}/{self.USERNAME}/graphs/{self.GRAPH_ID}/{self.todays_date()}"
        self.response = requests.delete(
            url=self.delete_pixel_endpoint,
            headers=self.HEADERS,
        )
