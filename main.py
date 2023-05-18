import os
import json

import openai
from dotenv import load_dotenv

from google.keywords_search import KeywordsSearch
from scraper.google import GoogleScraper

from pprint import pprint
from utility.processing import *

from executors.model import ModelExecutor
from utility.recursive_summarisation import RecursivelySummariseText

load_dotenv("data/.env")

openai.organization = os.getenv("OPENAI_ORG_ID")
openai.api_key = os.getenv("OPENAI_API_KEY")

# Step 1

# keyword_search = KeywordsSearch(openai)
# keywords = keyword_search.execute()

# Step 2

# keywords_data = json.load(open("data/conversations/google/keywords.json", "r"))
#
# # Prepare keywords list
# keywords_list = []
# keywords_list.extend(keywords_data["google"]["search_phrases"])
#
# keywords_list.extend(["site:twitter.com " + keywords for keywords in keywords_data["twitter"]["search_phrases"]])
# keywords_list.extend(["site:reddit.com " + keywords for keywords in keywords_data["reddit"]["search_phrases"]])
# keywords_list.extend(["site:news.ycombinator.com " + keywords for keywords in keywords_data["hacker news"]["search_phrases"]])
#
# # Scrape data
# g_scraper = GoogleScraper()
# g_scraper.get_data(keywords_list)


# Post Step 2 - Process scraped data

scraped_data = json.load(open("data/scraped_data/all_scraped_data.json", "r"))

for key in scraped_data.keys():
    res = scraped_data[key]
    scraped_data[key] = [process_info(info) for info in scraped_data[key]]

# Step 3 - Final Inference

system = \
    """
    You are a market research AI. Your job is to help us with market research of the below idea:
    
    We are trying to develop a protocol which does the following to help people distinguish if an image is genuine or ai generated
    
    Tracking if the image was algorithmically generated or taken by user on a camera:
    For this an attested camera sensor is used which cryptographically signs an image to prove that the image was indeed taken from a camera
    
    Tracking the edits on the image:
    For this we will track every edit made on the image and save it in the metadata.
    
    Verification:
    Any user, when given the image can test if the image was taken by a camera and also verify what edits were made on it
    
    We are going to give you raw data obtained from different web pages relating to the idea. Your job is to analyse and understand that information to 
    tell us about market fit, our competitors, existing technologies we can leverage and what is going on in this space. The output should be in markdown format. 
    """

goal = \
    """
    This information will be utilised to asses the below idea:
    
    We are trying to develop a protocol which does the following to help people distinguish if an image is genuine or ai generated
    
    Tracking if the image was algorithmically generated or taken by user on a camera:
    For this an attested camera sensor is used which cryptographically signs an image to prove that the image was indeed taken from a camera
    
    Tracking the edits on the image:
    For this we will track every edit made on the image and save it in the metadata.
     
    This information will finally be utilised to assess the idea on following parameter:
    
    Market fit, competitors, existing technologies we can leverage and what is going on in this space.
    """

# Step 3 - Summarise data using GPT 3.5

summarised_data = {}
model = RecursivelySummariseText(openai, goal)

for key in scraped_data:
    for idx, info in enumerate(scraped_data[key]):
        message = f"Information about {key} - {idx}/{len(scraped_data[key])}\n" + info
        summary = model.summarise(message)
        summarised_data[key] = summarised_data.get(key, []) + [summary]

    print(f"[Completed] Key: {key}")

with open("data/summary/summary.json", "w") as f:
    json.dump(summarised_data, f)


# Step 4 - Inference

# inference_model = ModelExecutor(openai, system)
# messages = []

# response = inference_model.execute_all(messages)
# message = response.content()
#
# with open("data/responses/research.md", "w") as f:
#     f.write(message)
