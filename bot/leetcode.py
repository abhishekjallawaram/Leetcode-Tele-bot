import datetime
import pytz
import requests
import json

# Define EDT Time Zone
leetcode_timezone = pytz.timezone("America/New_York")

def next_contest_start():
    today = datetime.datetime.now(leetcode_timezone)
    next_contest_date = today + datetime.timedelta((5 - today.weekday()) % 7)  # Next Saturday
    
    # Scheduled times for contests
    bi_weekly_start_time = next_contest_date.replace(hour=10, minute=30, second=0, microsecond=0)  # 10:30 AM
    weekly_start_time = next_contest_date.replace(hour=22, minute=30, second=0, microsecond=0)  # 10:30 PM
    
    # Adjust for next week if the current time is past this week's weekly contest time
    if datetime.datetime.now(leetcode_timezone) >= weekly_start_time:
        next_contest_date += datetime.timedelta(weeks=1)
        bi_weekly_start_time = next_contest_date.replace(hour=10, minute=30, second=0, microsecond=0)
        weekly_start_time = next_contest_date.replace(hour=22, minute=30, second=0, microsecond=0)
    
    # Assume bi-weekly contests occur every other week starting from a known date
    # Replace with the actual start date of the bi-weekly contest series
    bi_weekly_reference_date = datetime.datetime(2023, 1, 1, tzinfo=leetcode_timezone)  # Example reference date
    weeks_since_reference = (today - bi_weekly_reference_date).days // 7
    
    bi_weekly_this_week = weeks_since_reference % 2 == 0
    
    # Return times for both contests if bi-weekly is this week, else return only weekly
    return {
        "bi_weekly": bi_weekly_start_time if bi_weekly_this_week else None,
        "weekly": weekly_start_time
    }

def get_contest_time_left(start_time):
    if not start_time:
        return "No contest is scheduled."
    now = datetime.datetime.now(leetcode_timezone)
    time_difference = start_time - now
    if time_difference.total_seconds() > 0:
        days, seconds = time_difference.days, time_difference.seconds
        hours, remainder = divmod(seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        return f"Starts in {days} days, {hours} hours, {minutes} minutes, {seconds} seconds."
    else:
        return "The contest has already started or no contest is scheduled."

def get_weekly_time_left():
    contest_times = next_contest_start()
    if "weekly" in contest_times:
        return get_contest_time_left(contest_times["weekly"])
    else:
        return "No weekly contest is scheduled."

def get_bi_weekly_time_left():
    contest_times = next_contest_start()
    if "bi_weekly" in contest_times:
        return get_contest_time_left(contest_times["bi_weekly"])
    else:
        return "No bi-weekly contest is scheduled."
    
def is_contest_ongoing(contest_start_time):
    now = datetime.datetime.now(leetcode_timezone)
    contest_end_time = contest_start_time + datetime.timedelta(minutes=90)
    if contest_start_time <= now < contest_end_time:
        # Contest is ongoing; calculate time left until it ends
        return True, contest_end_time - now
    return False, None

def format_timedelta(td):
    days, remainder = divmod(td.total_seconds(), 86400)
    hours, remainder = divmod(remainder, 3600)
    minutes, seconds = divmod(remainder, 60)
    return f"{int(days)} days, {int(hours)} hours, {int(minutes)} minutes, {int(seconds)} seconds."

def fetch_daily_challenge():
    url = "https://leetcode.com/graphql"
    headers = {"Content-Type": "application/json"}
    query = {
        "query": """
        query questionOfToday {
          activeDailyCodingChallengeQuestion {
            date
            userStatus
            link
            question {
              title
              titleSlug
              difficulty
              topicTags {
                name
                slug
              }
            }
          }
        }
        """
    }

    try:
        response = requests.post(url, json=query, headers=headers)
        data = response.json()
        question = data["data"]["activeDailyCodingChallengeQuestion"]["question"]
        title = question["title"]
        difficulty = question["difficulty"]
        tags = [tag["name"] for tag in question["topicTags"]]
        link = "https://leetcode.com" + data["data"]["activeDailyCodingChallengeQuestion"]["link"]

        return {
            "title": title,
            "difficulty": difficulty,
            "tags": ', '.join(tags),
            "link": link
        }
    except Exception as e:
        print(f"Error fetching daily challenge: {e}")
        return None




