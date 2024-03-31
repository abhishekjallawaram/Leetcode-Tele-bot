# Building a LeetCode Reminder Bot for Telegram: A Beginner's Guide

This guide is designed to walk beginners through the process of creating a LeetCode Reminder Bot for Telegram. By the end of this tutorial, you'll have a functioning bot that notifies users about upcoming LeetCode contests.

## Prerequisites

Before starting, ensure you have the following:
- Basic knowledge of Python programming.
- Python installed on your computer ([Download Python](https://www.python.org/downloads/)).
- A Telegram account.

## Step 1: Create Your Telegram Bot

1. **Start a chat with BotFather:** Search for [@BotFather](https://t.me/botfather) on Telegram and start a conversation.
2. **Create a new bot:** Send the `/newbot` command and follow the prompts to set up your bot. You'll need to choose a name and a username for your bot.
3. **Save your bot token:** After the setup, BotFather will give you an API token. Save it; you'll need this token to interact with the Telegram Bot API.

## Step 2: Set Up Your Project Environment

1. **Create a new directory for your project:** This will be your working directory.
2. **Open a terminal in your project directory.**
3. **Create a virtual environment:** Run `python -m venv env` to create a virtual environment named `env`. Then, activate it with `source env/bin/activate` on Unix/macOS or `.\env\Scripts\activate` on Windows.
4. **Create a `requirements.txt` file:** This file should list all the necessary Python packages:
    ```
    python-telegram-bot==13.7
    pytz==2021.1
    python-decouple==3.4
    ```
5. **Install dependencies:** Run `pip install -r requirements.txt` to install the required packages.

## Step 3: Write Your Bot's Code

1. **Create a `bot` directory and a `main.py` file:** Your project structure should now look like this:
    ```
    your-project/
    ├── bot/
    ├── .env
    ├── requirements.txt
    └── main.py
    ```
2. **Set up your `.env` file:** Inside this file, place your Telegram bot token like so:
    ```
    API_KEY=your_bot_token_here
    ```
3. **Implement your bot's logic:** Use the `python-telegram-bot` library to interact with the Telegram API, `pytz` for timezone management, and `python-decouple` for environment variable management.

## Step 4: Run Your Bot

1. **Execute `main.py`:** Run `python main.py` in your terminal. Your bot should now be live and responding to commands on Telegram.

## Step 5: Interact With Your Bot on Telegram

1. **Start the bot:** Send the `/start` command to your bot on Telegram.
2. **Check contest reminders:** Use the custom commands you've implemented (like `/timeleft`) to interact with your bot and receive reminders about LeetCode contests.

## Step 6: Deploy Your Bot (Optional)

Consider deploying your bot to a cloud platform like Heroku or a VPS to keep it running 24/7.

1. **Choose a deployment platform:** Research platforms like Heroku, AWS, or DigitalOcean for deploying your bot.
2. **Follow the platform-specific deployment guide:** Each platform has its own method for deploying applications, so follow the instructions carefully.

## Conclusion

Congratulations! You've built and deployed your own LeetCode Reminder Bot for Telegram. This project is a great starting point for diving deeper into bot development and exploring more advanced features.

## Additional Resources

- [Telegram Bot API](https://core.telegram.org/bots/api)
- [python-telegram-bot Documentation](https://python-telegram-bot.readthedocs.io/)
- [Heroku Deployment Guide](https://devcenter.heroku.com/articles/getting-started-with-python)
