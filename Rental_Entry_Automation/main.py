from automate_google_forms import AutomateGoogleForms
from zillow_scraper import ZillowScraper

zillow_scraper = ZillowScraper()
automate_google_forms = AutomateGoogleForms(zillow_scraper)
