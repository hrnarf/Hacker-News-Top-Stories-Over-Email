# Hacker News top stories, over email!
If you're like me and often find yourself spending hours browsing [Hacker News](http://hacker.news), this script might be just what you need. 

It’s designed to fetch the top stories from Hacker News. After getting each top story, it uses ConvertKit to send generate and send email with the title + link of each story. 

The email which is created in ConvertKit is called a Broadcast, this broadcast can be automatically scheduled to send using parameters over the ConvertKit API, meaning you'd never need to login to your ConvertKit account once everything is setup.

[ConvertKit API](https://developers.convertkit.com/#create-a-broadcast) | [Hacker News API](https://github.com/HackerNews/API?tab=readme-ov-file)

P.S ConvertKit has a free tier, which is all you require!

Here is an example of the email you'd expect to recieve:

<img width="853" alt="Screenshot" src="https://github.com/user-attachments/assets/d4a89b41-35b6-414b-b15a-aa83ab1358e1">

## How It's Made:

**Tech used:** Python

A pure Python script that uses the Hacker News API to fetch the top stories, and then uses ConvertKit, a free email service, to send these stories in a neatly formatted email. 

The project was designed with simplicity in mind, using only essential third-party APIs to achieve the functionality.

This runs locally on my machine using a cron job.
