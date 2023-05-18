import os
import json

import openai
from dotenv import load_dotenv

from google.keywords_search import KeywordsSearch
from scraper.google import GoogleScraper

from pprint import pprint


load_dotenv("data/.env")

openai.organization = os.getenv("OPENAI_ORG_ID")
openai.api_key = os.getenv("OPENAI_API_KEY")

# Step 1

# keyword_search = KeywordsSearch(openai)
# keywords = keyword_search.execute()

# Step 2

keywords_data = json.load(open("data/conversations/google/keywords.json", "r"))

# Prepare keywords list
keywords_list = []
keywords_list.extend(keywords_data["google"]["search_phrases"])

keywords_list.extend(["site:twitter.com " + keywords for keywords in keywords_data["twitter"]["search_phrases"]])
keywords_list.extend(["site:reddit.com " + keywords for keywords in keywords_data["reddit"]["search_phrases"]])
keywords_list.extend(["site:news.ycombinator.com " + keywords for keywords in keywords_data["hacker news"]["search_phrases"]])

# Scrape data
g_scraper = GoogleScraper()
g_scraper.get_data(keywords_list)
