# Zillow Scraper and Google Forms Automator

This project consists of two main components:

1. **Zillow Scraper**: This Python script (zillow_scraper.py) scrapes rental property information from a Zillow clone website and extracts rental addresses, prices, and links.
2. **Google Forms Automator:**: This Python script (automate_google_forms.py) automates the filling of a Google Form with the rental property information obtained from the Zillow scraper.

## Zillow Scraper:
The Zillow Scraper is responsible for retrieving rental property data from the Zillow clone website. It uses Beautiful Soup for web scraping and Requests for making HTTP requests to fetch the webpage content.

### Usage:
1. Install the required dependencies using pip:
```
pip install beautifulsoup4 requests
```
2. Run the script:
```
zillow_scraper.py
```
3. The script will fetch rental property information such as addresses, prices, and links from the Zillow clone website.

## Google Forms Automater:
The Google Forms Automator fills out a Google Form with the rental property information obtained from the Zillow scraper. It uses Selenium WebDriver to interact with the Google Form and fill in the required fields.

### Usage:
1. Install the required dependencies using pip:
```
pip install selenium
```
2. Download and install the appropriate WebDriver for your browser (e.g., ChromeDriver for Google Chrome).
3. Run the Scripts:
```
python automate_google_forms.py
```
4. The script will automatically fill out the Google Form with the rental property information.

## Run:
- To run the full program 
```
python main.py
```

## Requirments:
- Python 3.x
- Beautiful Soup 4
- Requests
- Selenium

### Contributions:
- Contribution are welcomed.