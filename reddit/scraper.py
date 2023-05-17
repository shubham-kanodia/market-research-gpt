from utility.code_generator import CodeGenerator

import os

import praw


class RedditScraper:
    def __init__(self, openai):
        self.openai = openai
        self.code_generator_model = CodeGenerator(openai)

    def scrape(self, search_phrases, subreddits, users):
        # Create a Reddit instance
        REDDIT_API_SECRET = os.getenv("REDDIT_API_SECRET")
        REDDIT_CLIENT_ID = os.getenv("REDDIT_CLIENT_ID")

        reddit = praw.Reddit(client_id='REDDIT_CLIENT_ID',
                             client_secret='REDDIT_API_SECRET',
                             user_agent='YOUR_USER_AGENT')

        # Scrape subreddit(s)
        for subreddit_name in subreddits:
            subreddit = reddit.subreddit(subreddit_name)
            print(f'Scraping subreddit: {subreddit_name}')
            for submission in subreddit.new(limit=10):  # Set the number of posts to retrieve
                # Filter posts based on keywords
                if any(keyword in submission.title for keyword in search_phrases):
                    print(f'Title: {submission.title}')
                    print(f'URL: {submission.url}')

        for username in users:
            user = reddit.redditor(username)
            print(f'Scraping user: {username}')
            for submission in user.submissions.new(limit=10):
                if any(keyword in submission.title for keyword in search_phrases):
                    print(f'Title: {submission.title}')
                    print(f'URL: {submission.url}')
