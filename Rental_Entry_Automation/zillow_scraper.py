from bs4 import BeautifulSoup
from requests import get


class ZillowScraper:

    def __init__(self) -> None:
        self.response = get(url="https://appbrewery.github.io/Zillow-Clone/")
        self.data = self.response.text

        # Beautifull Soup Setup:
        self.soup = BeautifulSoup(markup=self.data, features="html.parser")

        # Rental Addresses;
        self.all_address = self.soup.find_all(name="address")
        self.rental_address = []
        for address in self.all_address:
            r_address = address.text
            self.rental_address.append(r_address.replace(" | ", "").strip())

        # Rental Prices;
        self.all_prices = self.soup.find_all(
            name="span", class_="PropertyCardWrapper__StyledPriceLine"
        )
        self.rental_prices = []
        for prices in self.all_prices:
            r_prices = prices.text
            self.rental_prices.append(
                r_prices.replace("+", "").replace("/mo", "").replace("1 bd", "")
            )

        # Rental Address Links
        self.all_links = self.soup.select(selector=".StyledPropertyCardDataWrapper a")
        self.rental_links = []
        for links in self.all_links:
            href = links["href"]
            self.rental_links.append(href)


scraper = ZillowScraper()
