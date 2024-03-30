from telebot import TeleBot
import datetime
import pytz
from .leetcode import next_contest_start, get_weekly_time_left, get_bi_weekly_time_left, format_timedelta, leetcode_timezone, is_contest_ongoing, fetch_daily_challenge

def setup_commands(bot: TeleBot):
    @bot.message_handler(commands=["start"])
    def send_welcome(message):
        reply = "Thank you for using the LeetCode Contest Bot! 🎉 To discover more about what I can do, type /commands. I'm here to help you track contest times, keep up with the schedules, and more. Let's ace those challenges together! ✨"
        bot.send_message(message.chat.id, reply)

    @bot.message_handler(commands=["weeklytime"])
    def weekly_time_left(message):
        weekly_response = get_weekly_time_left()
        response = f"Weekly Contest: {weekly_response}\n\nThank you for using the LeetCode Contest Bot! 🎉 To discover more about what I can do, type /commands. I'm here to help you track contest times, keep up with the schedules, and more. Let's ace those challenges together! ✨"
        bot.send_message(message.chat.id, response)

    @bot.message_handler(commands=["biweeklytime"])
    def bi_weekly_time_left(message):
        bi_weekly_response = get_bi_weekly_time_left()
        response = f"Bi-Weekly Contest: {bi_weekly_response}\n\nThank you for using the LeetCode Contest Bot! 🎉 To discover more about what I can do, type /commands. I'm here to help you track contest times, keep up with the schedules, and more. Let's ace those challenges together! ✨"
        bot.send_message(message.chat.id, response)
        
    @bot.message_handler(commands=["commands"])
    def list_commands(message):
        commands_list = """
        Available Commands:
        /commands - Show all commands
        /weeklytime - Show time left until the next Weekly Contest
        /biweeklytime - Show time left until the next Bi-Weekly Contest
        /timeleft - Show time left for ongoing contests or until the next contest starts
        /QOTD - Get the Question of the Day (QOTD) from LeetCode
            """
        bot.send_message(message.chat.id, commands_list.strip())
        
    @bot.message_handler(commands=["timeleft"])
    def time_left(message):
        now = datetime.datetime.now(leetcode_timezone)
        contest_times = next_contest_start()
        responses = []

        def format_time_until_start(contest_name, start_time):
            # Calculate the time difference between now and the contest start time
            time_diff = start_time - now
            if time_diff.total_seconds() > 0:
                end_time = start_time + datetime.timedelta(minutes=90)
                # If the contest hasn't started yet, format the time left until it starts
                return f"{contest_name} Contest: Starts in {format_timedelta(time_diff)}."
            else:
                # If the contest has already started or ended, calculate when it ended
                end_time = start_time + datetime.timedelta(minutes=90)
                if now < end_time:
                    # Contest is ongoing, calculate time until it ends
                    return f"{contest_name} Contest: Ends in {format_timedelta(end_time - now)}."
                else:
                    # Contest has ended
                    return f"{contest_name} Contest has already ended."

        # Generate the time until start message for both weekly and bi-weekly contests
        weekly_msg = format_time_until_start("Weekly", contest_times["weekly"])
        responses.append(weekly_msg)
        
        # For bi-weekly, first check if it's scheduled for this week
        if "bi_weekly" in contest_times and contest_times["bi_weekly"]:
            bi_weekly_msg = format_time_until_start("Bi-Weekly", contest_times["bi_weekly"])
            responses.append(bi_weekly_msg)
        else:
            responses.append("Bi-Weekly Contest: No contest is scheduled for this week.")

        # Combine all responses and send the message
        response = "\n\n".join(responses)
        bot.send_message(message.chat.id, response)
        
    @bot.message_handler(commands=["QOTD"])
    def daily_question(message):
        challenge = fetch_daily_challenge()
        if challenge:
            response = f"Title: {challenge['title']}\nDifficulty: {challenge['difficulty']}\nTags: {challenge['tags']}\nLink: {challenge['link']}"
        else:
            response = "Sorry, I couldn't fetch the daily challenge at the moment. Please try again later."

        bot.send_message(message.chat.id, response)


        
        
def format_timedelta(td):
    days, remainder = divmod(td.total_seconds(), 86400)
    hours, remainder = divmod(remainder, 3600)
    minutes, seconds = divmod(remainder, 60)
    return f"{int(days)} days, {int(hours)} hours, {int(minutes)} minutes, {int(seconds)} seconds."
