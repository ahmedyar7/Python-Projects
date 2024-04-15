# Tesla News Alert

This Python script fetches the latest news articles related to a specific company (in this case, Tesla) from the News API and sends the information via SMS using Twilio. 

## Setup

Before running the script, make sure you have the following:

1. **News API Key**: Obtain your API key from [News API](https://newsapi.org/) by signing up for an account.

2. **Twilio Account**: Sign up for a Twilio account to get your Account SID, Auth Token, and a Twilio phone number.

3. **Environment Variables**: Create a `.env` file in the same directory as the script and add the following variables:

    ```plaintext
    API_KEY=your_news_api_key
    ACCOUNT_SID=your_twilio_account_sid
    AUTH_TOKEN=your_twilio_auth_token
    TWILIO_PHONENUMBER=your_twilio_phone_number
    MY_PHONENUMBER=your_phone_number
    ```

4. **Python Environment**: Make sure you have Python installed on your system. Install required packages using pip:

    ```
    pip install requests twilio-python python-dotenv
    ```

## Usage

1. **Run the Script**: Execute the Python script `news_alert.py`. It will fetch the latest news articles related to the specified company (here, Tesla) and send the information via SMS.

2. **SMS Notification**: You will receive an SMS containing the details of the latest news article, including the source, author, title, and description.

## Script Explanation

- The script starts by importing necessary modules including `os`, `dotenv`, `requests`, and `twilio`.
- It loads environment variables from a `.env` file using `dotenv`.
- Environment variables include API keys, Twilio credentials, and phone numbers.
- The script constructs parameters for the News API query, specifying the API key and the company name to search for.
- It makes a GET request to the News API endpoint with the constructed parameters.
- The script retrieves the JSON response and extracts the relevant article data.
- It selects the first article from the response and constructs a message containing information about the article.
- Using Twilio's Python client, it sends an SMS message containing the article details to the specified phone number.
- Finally, it prints the status of the sent message.

## Customization

- Modify the `COMPANY_NAME` variable to search for news related to a different company.
- Customize the message format in the `MESSAGE` variable to include additional information if needed.

## Limitations

- The script fetches only one news article per run. You may need to modify the script to fetch multiple articles or schedule it to run periodically for continuous updates.

