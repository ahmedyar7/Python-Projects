# Amazon Price Tracker 📉🔎

## Introduction
This Python script tracks the price of a product on Amazon.com and sends an email notification if the price drops below a desired threshold. It utilizes web scraping with BeautifulSoup to extract the price from the Amazon page and sends an email using SMTP if the price falls below a specified amount.

## Requirements
- Python 3.x
- requests library
- BeautifulSoup library
- smtplib library
- dotenv library

## Setup
1. Clone the repository or download the script.
2. Install the required dependencies by running:
    ```bash
    pip install requests beautifulsoup4
    pip install python-dotenv
    ```
3. Create a `.env` file in the project directory and add the following environment variables:
    ```
    USER_AGENT="Your User Agent"
    ACCEPT_LANGUAGE="Your Accept Language"
    URL="URL of the Amazon product"
    TO_EMAIL="Recipient's email address"
    FROM_EMAIL="Your email address"
    PASSWORD="Your email password"
    SMTP_SEVER="SMTP server address"
    ```
    Replace the placeholder values with your actual information.

## Usage
1. Run the script using:
    ```bash
    python main.py
    ```
2. The script will fetch the price of the product from the specified Amazon URL.
3. If the price drops below the desired threshold, it will send an email notification to the recipient.

## Note
- Ensure that you enable "Less secure app access" for your email account if you're using Gmail as your SMTP server.
- Be cautious with storing sensitive information like passwords in your `.env` file. Keep it secure and don't share it publicly.
- Make sure to comply with Amazon's Terms of Service when scraping data from their website.

