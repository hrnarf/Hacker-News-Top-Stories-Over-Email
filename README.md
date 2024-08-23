# Hacker News top stories, over email!
If you're like me and often find yourself spending hours browsing Hacker News, this script might be just what you need. 

It’s designed to fetch the top stories (limited to a specified number) from Hacker News. After getting each top story, it uses ConvertKit to send an email with the content of the stories. 

ConvertKit is an email service which has a free tier, this is all you'd need to make this script work.

Here is an example of the email you'd expect to recieve:

<img width="853" alt="Screenshot 2024-08-23 at 21 08 39" src="https://github.com/user-attachments/assets/d4a89b41-35b6-414b-b15a-aa83ab1358e1">


## How It's Made:

**Tech used:** Python

A pure Python script that uses the official Hacker News API to fetch the top stories, and then uses ConvertKit, a free email service, to send these stories in a neatly formatted email. 

The project was designed with simplicity in mind, using only essential third-party APIs to achieve the functionality.

This runs locally on my machine using a cron job.
