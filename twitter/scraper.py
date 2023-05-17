from executors.model import ModelExecutor
from utility.code_generator import CodeGenerator

import os

import tweepy


class TwitterScraper:
    def __init__(self, openai):
        self.openai = openai
        self.code_generator_model = CodeGenerator(openai)

    def generate_code(self, search_phrases, hashtags, people):
        code = self.code_generator_model.execute(
            f"""Generate code to search and get content of tweets on twitter that contain given search phrases,
             hashtags and people
             
             Search Phrases:
             {",".join(search_phrases)}
             
             Hashtags:
             {",".join(hashtags)}
             
             People:
             {",".join(people)}
            """
        )

        return code

    def scrape(self, search_phrases, hashtags, people, count=5):
        TWITTER_API_KEY = os.getenv("TWITTER_API_KEY")
        TWITTER_API_SECRET = os.getenv("TWITTER_API_SECRET")
        TWITTER_ACCESS_TOKEN = os.getenv("TWITTER_ACCESS_TOKEN")
        TWITTER_ACCESS_SECRET = os.getenv("TWITTER_ACCESS_SECRET")

        auth = tweepy.OAuthHandler(TWITTER_API_KEY, TWITTER_API_SECRET)
        auth.set_access_token(TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_SECRET)

        api = tweepy.API(auth)

        query = ' OR '.join(search_phrases + hashtags + people)
        tweets = [status._json for status in
                  tweepy.Cursor(api.search_tweets, q=query, count=count, tweet_mode='extended').items()]

        full_tweets = [tweet['full_text'] for tweet in tweets]

        return full_tweets
