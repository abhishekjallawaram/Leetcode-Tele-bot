import requests
import json

# Endpoint URL
url = "https://leetcode.com/graphql"

# Headers for the request
headers = {"Content-Type": "application/json"}

# GraphQL query payload
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

# Sending the POST request to the GraphQL endpoint
response = requests.post(url, json=query, headers=headers)

# Parsing the response
data = response.json()

# Extracting the question details
question = data["data"]["activeDailyCodingChallengeQuestion"]["question"]
title = question["title"]
difficulty = question["difficulty"]
tags = [tag["name"] for tag in question["topicTags"]]
link = "https://leetcode.com" + data["data"]["activeDailyCodingChallengeQuestion"]["link"]

# Displaying the question details
print(f"Title: {title}")
print(f"Difficulty: {difficulty}")
print(f"Tags: {', '.join(tags)}")
print(f"Link: {link}")
