import os
import json

import openai
from dotenv import load_dotenv

from google.keywords_search import KeywordsSearch

load_dotenv("data/.env")

openai.organization = os.getenv("OPENAI_ORG_ID")
openai.api_key = os.getenv("OPENAI_API_KEY")

# Step 1

keyword_search = KeywordsSearch(openai)
keywords = keyword_search.execute()

print(keywords)
# Step 2

# scraper = TwitterScraper(openai)
#
# keywords = json.load(open("data/conversations/keywords.json", "r"))
# search_phrases, hashtags, people = keywords["search_phrases"], keywords["hashtags"], keywords["people"]
#
# scraper.scrape(search_phrases, hashtags, people)
