# TwittetBot

TwitterNetBot is a Python script that automates tweeting internet speed test results to your Twitter account.

## Overview

This script utilizes Selenium, a powerful tool for automating web browser interaction, to perform the following tasks:
- Conduct an internet speed test using Speedtest.net.
- Log in to a Twitter account.
- Compose a tweet containing the internet speed test results and desired speed thresholds.

## Prerequisites

Before using TwitterNetBot, ensure you have the following:
- Python installed on your system.
- Chrome web browser installed.
- Twitter developer account to access API keys.
- `.env` file containing Twitter credentials (`TWITTER_EMAIL`, `TWITTER_USERNAME`, `TWITTER_PASSWORD`).

## Installation

1. ### Clone this repository:

```bash
git clone https://github.com/ahmedyar7/Python-Projects.git
```

2. ### Install the required Python packages:
```
pip install -r requirements.txt
```

3. ### Create a .env file in the root directory and add your Twitter credentials:
```
TWITTER_EMAIL=your_twitter_email
TWITTER_USERNAME=your_twitter_username
TWITTER_PASSWORD=your_twitter_password

```
## Usage:

1. Run the script:
```
python main.py
```
2. The script will perform the following steps:
Conduct an internet speed test.
Log in to your Twitter account.

3. Compose a tweet with the internet speed test results.
Check your Twitter account to verify the tweet.

## Note:
Contributions are welcomed