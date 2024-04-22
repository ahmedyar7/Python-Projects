from os import getenv
from dotenv import find_dotenv, load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

load_dotenv(dotenv_path=find_dotenv())


# Environment Variables => Twitter
TWITTER_EMAIL = getenv("TWITTER_EMAIL")
TWITTER_USERNAME = getenv("TWITTER_USERNAME")
TWITTER_PASSWORD = getenv("TWITTER_PASSWORD")
