# LeetCode Contest Reminder Bot 🚀

Welcome to the **LeetCode Contest Reminder Bot**, a dedicated Telegram bot crafted to ensure competitive programmers never miss out on their next big challenge. Whether it's a Weekly or Bi-Weekly contest, or if you're just looking to tackle the Question of the Day (QOTD), this bot has got you covered. With timely reminders and direct links to daily challenges, sharpening your coding skills has never been more convenient.

## 🌟 Features

- **Contest Timing Notifications**: Get ahead with precise reminders for LeetCode's Weekly and Bi-Weekly contests. Know exactly how much time you have until the next intellectual showdown.
- **Daily Coding Challenge**: Dive into LeetCode's Question of the Day (QOTD) directly from your Telegram chat. Details include title, difficulty, tags, and a direct problem link.
- **Commands at Your Fingertips**: A comprehensive list of commands ensures you seamlessly make the most out of your bot experience.

## 🛠 Getting Started

### Prerequisites

Before you embark on this journey, make sure you're equipped with:

- Python (version 3.6 or later)
- A Telegram account
- A token for your Telegram bot, obtainable via [BotFather](https://t.me/botfather)

### Installation Steps

1. **Clone the Repository**

    Kick things off by cloning this repository to your local machine. Open your terminal and run:

    ```bash
    git clone https://github.com/yourusername/leetcode-reminder-bot.git
    cd leetcode-reminder-bot
    ```

2. **Prepare Your Python Environment**

    For a smooth sailing development experience, set up a virtual environment:

    ```bash
    python3 -m venv env
    source env/bin/activate
    ```

3. **Install Dependencies**

    Navigate through the high seas of development with all the necessary packages:

    ```bash
    pip install -r requirements.txt
    ```

4. **Bot Token Configuration**

    Keep your bot's heart beating with its unique token. Create a `.env` file in the root directory and insert:

    ```plaintext
    API_KEY=your_bot_token_here
    ```

### 🚀 Launching the Bot

With the wind in your sails, it's time to launch:

```bash
python main.py
```

You are now ready to interact with your bot on Telegram and explore the vast ocean of coding challenges.

## 📜 Bot Commands

| Command       | Description                                                |
|---------------|------------------------------------------------------------|
| `/start`      | A hearty welcome and bot instructions.                     |
| `/commands`   | Lists all the available commands for easy navigation.      |
| `/weeklytime` | Countdown to the next Weekly Contest.                      |
| `/biweeklytime` | Countdown to the next Bi-Weekly Contest.                |
| `/timeleft`   | Time left for ongoing contests or until the next contest embarks. |
| `/QOTD`       | Fetch the Question of the Day from LeetCode.               |

## 🛠 Development Insights

Dive deeper into the workings of this bot, built with the `python-telegram-bot` library and powered by `pytz` for timezone accuracy. Contest times and the daily challenge are fetched with grace, ensuring you're always in the loop.

### Important Files

- `commands.py`: The heart of the bot, handling all your Telegram commands.
- `leetcode.py`: The brain, calculates contest times and fetches the daily challenge.

## 🤝 Contributing

Set sail with us! Contributions are the winds that propel this project forward. Feel free to fork the project, make your changes, and submit a pull request with your treasures.

## 📜 License

This project is proudly licensed under the MIT License. For more details, see the LICENSE file.

Sail forth, brave coder, and may the winds of code always be at your back!


## Interact With Your Bot on Telegram

1. **Start the bot:** Send the `/start` command to your bot on Telegram.
2. **Check contest reminders:** Use the custom commands you've implemented (like `/timeleft`) to interact with your bot and receive reminders about LeetCode contests.

## Deploy Your Bot (Optional)

Consider deploying your bot to a cloud platform like Heroku or a VPS to keep it running 24/7.

1. **Choose a deployment platform:** Research platforms like Heroku, AWS, or DigitalOcean for deploying your bot.
2. **Follow the platform-specific deployment guide:** Each platform has its method for deploying applications, so follow the instructions carefully.


## Additional Resources

- [Telegram Bot API](https://core.telegram.org/bots/api)
- [python-telegram-bot Documentation](https://python-telegram-bot.readthedocs.io/)
- [Heroku Deployment Guide](https://devcenter.heroku.com/articles/getting-started-with-python)
