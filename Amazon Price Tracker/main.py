from os import getenv
from dotenv import find_dotenv, load_dotenv
from requests import get
from bs4 import BeautifulSoup
import smtplib

dotenv_path = find_dotenv()
load_dotenv(dotenv_path)

## Environment Variables => Amazon.com
USER_AGENT = getenv("USER_AGENT")
ACCEPT_LANGUAGE = getenv("ACCEPT_LANGUAGE")
URL = getenv("URL")

## Environment Variables => SMTP
TO_EMAIL = getenv("TO_EMAIL")
FROM_EMAIL = getenv("FROM_EMAIL")
PASSWORD = getenv("PASSWORD")
SMTP_SEVER = getenv("SMTP_SEVER")
