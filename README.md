# Hacker News Top Stories, Over Email. 📧
> A script to send Hacker News Top stories, to yourself, through email, via a free third party email service.

If you're like me and often find yourself spending hours browsing [Hacker News](http://hacker.news), this script might be just what you need. 

It’s designed to fetch the top stories from Hacker News. After getting each top story, it uses ConvertKit to generate and send an email with the title + link of each story. 

[ConvertKit API](https://developers.convertkit.com/#create-a-broadcast) | [Hacker News API](https://github.com/HackerNews/API?tab=readme-ov-file)

[ConvertKit](https://convertkit.com) has a free tier, which is all you require.

Here is an example of the email you'd expect to recieve:

<img width="853" alt="Screenshot" src="https://github.com/user-attachments/assets/d4a89b41-35b6-414b-b15a-aa83ab1358e1">

## How It's Made:

**Tech used:** Python

A pure Python script that uses the Hacker News API to fetch the top stories, and then uses the ConvertKit API to generate and send the email.
 
The email created in ConvertKit is referred to as a “Broadcast.” In the script, this broadcast is generated in “draft” mode. However, it can be configured via the API to be scheduled and automatically sent to your email on a daily basis, offering flexibility in how and when you receive the curated top stories from Hacker News.

I've set this script to run locally, using a cron job.
