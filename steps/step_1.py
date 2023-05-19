import json
from google.keywords_search import KeywordsSearch


class Step1:
    def __init__(self, openai):
        self.openai = openai
        self.file_path = "data/keywords.json"

    def check_existing_data(self):
        try:
            keywords_data = json.load(open(self.file_path, "r"))
            return keywords_data
        except:
            return None

    def execute(self):
        existing_data = self.check_existing_data()

        if existing_data:
            return existing_data
        else:
            keyword_search = KeywordsSearch(self.openai)
            keywords = keyword_search.execute()

            json.dump(keywords, open(self.file_path, "w"), indent=2)
            return keywords
