# Monday Motivation Email Sender

This Python script is designed to send motivational quotes via email every Monday. It randomly selects a quote from a text file containing a list of quotes and sends it to a specified email address.

## Prerequisites

Before running the script, ensure you have the following:

- Python installed on your system
- An email account (e.g., Gmail) from which you want to send the motivational emails
- Generate an App Password if you're using Gmail, as regular passwords may not work due to security reasons

## You can setup your own app password by following through the tutorial below

[App Password Tutorial](https://www.youtube.com/watch?v=hXiPshHn9Pw)

## Setup

1. Clone or download the repository to your local machine.
2. Ensure you have a text file containing motivational quotes. By default, the script assumes the file is named `quotes.txt` and is located in a directory named `Monday Motivation`, but you can modify the `FILE_PATH` variable in the script if your file is located elsewhere or named differently.
3. Update the `MY_EMAIL` and `PASSWORD` variables in the script with your email address and App Password, respectively.
4. Make sure your email provider allows SMTP (Simple Mail Transfer Protocol) connections. Gmail, for example, requires you to enable "Less Secure Apps" or use App Passwords for SMTP connections.




## Usage

1. Open a terminal or command prompt.
2. Navigate to the directory containing the script.
3. Run the script by executing the following command:
4. The script will connect to your email server, select a random quote from the `quotes.txt` file, and send it to your specified email address.

## Customization

- You can modify the frequency of email sending by scheduling the script to run weekly using tools like cron jobs (Linux/Mac) or Task Scheduler (Windows).
- Customize the subject line and message content by modifying the `SUBJECT` and `MESSAGE` variables in the script to suit your preferences.

## Note

- Ensure the `quotes.txt` file contains quotes separated by newlines (\n).
- This script assumes you have Python installed and configured on your system.
- Make sure you keep your email credentials secure and do not share them with anyone.
- Test the script with a dummy email address before using it with your primary email account to ensure everything works as expected.


