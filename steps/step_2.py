import json

from scraper.google import GoogleScraper
from utility.processing import *


class Step2:
    def __init__(self, openai):
        self.openai = openai
        self.output_file_path = "data/processed_scraped_data.json"

    def check_existing_data(self):
        try:
            scraped_data = json.load(open(self.output_file_path, "r"))
            return scraped_data
        except:
            return None

    def execute(self, keywords):
        scraped_data = self.check_existing_data()

        if scraped_data:
            return scraped_data

        keywords_list = []
        keywords_list.extend(keywords["google"]["search_phrases"])

        keywords_list.extend(["site:twitter.com " + keywords for keywords in keywords["twitter"]["search_phrases"]])
        keywords_list.extend(["site:reddit.com " + keywords for keywords in keywords["reddit"]["search_phrases"]])
        keywords_list.extend(
            ["site:news.ycombinator.com " + keywords for keywords in keywords["hacker_news"]["search_phrases"]])

        g_scraper = GoogleScraper()
        scraped_data = g_scraper.get_data(keywords_list)

        for key in scraped_data.keys():
            scraped_data[key] = [process_info(info) for info in scraped_data[key]]

        with open(self.output_file_path, "w") as f:
            json.dump(scraped_data, f, indent=2)
