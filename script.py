import os

import requests
from typing import List
from datetime import date
from dotenv import load_dotenv

load_dotenv()


# Post class to store data for each post that is retrieved
class Story:
    def __init__(self, id, score, title, url):
        self.id = id
        self.title = title
        self.url = url
        self.score = score

    def __repr__(self):
        return f"Story(id={self.id}, title={self.title}, url={self.url}), score={self.score}"


# Make post requests to an API
def make_get_request(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raises an HTTPError for bad responses (4xx, 5xx)
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
        return None


stories = []  # Create an empty array to store posts
max_stories = 20  # The number of stories to retrieve
story_ids = make_get_request(
    "https://hacker-news.firebaseio.com/v0/beststories.json?print=pretty")  # Get a list of post ids


# Make the content for the email, from a list of posts
def make_email(list_of_stories: List[Story]) -> str:
    story_html = ""
    for s in list_of_stories:
        story_html += f'<ol><li><p><a href="https://news.ycombinator.com/item?id={s.id}">{s.title}</a></p></li></ol>'
    return story_html


# Make a broadcast using a 3rd party service (ConvertKit)
# The content that is pass to the API is created through the make_email function which returns a string
def make_broadcast():
    url = "https://api.convertkit.com/v3/broadcasts"
    headers = {
        "Content-Type": "application/json"
    }
    data = {
        "api_secret": os.getenv('API_SECRET'),
        "subject": f"Hacker News Top Posts - {date.today()}",
        "content": f"{make_email(stories)}"
    }
    try:
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()  # This will raise an HTTPError for bad responses (4xx, 5xx)
        print(response.status_code)
        print(response.json())
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")


# For each post id, make another request to get the individual post data, append this data into the posts array.
# After retrieving all the post data, a broadcast can then be made.
if story_ids:
    for id in story_ids[:max_stories]:
        story = make_get_request(f"https://hacker-news.firebaseio.com/v0/item/{id}.json?print=pretty")
        if story:
            stories.append(Story(id=story['id'], title=story['title'], url=story['url'], score=story['score']))
        else:
            print(f"Failed to retrieve post with id {id}")
    make_broadcast()
else:
    print("No valid post IDs retrieved.")
