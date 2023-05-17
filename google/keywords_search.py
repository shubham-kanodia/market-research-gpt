import json
from executors.model import ModelExecutor


class KeywordsSearch:
    def __init__(self, openai):
        self.openai = openai
        self.context = """
        You are a market research AI. For each idea you need to suggest what to search 
        on reddit, hacker news and twitter including people and keywords in a json format. The keys of json 
        should be reddit, twitter, hacker news, google with each one containing keys "search_phrases" and "people" except hacker news and google which will only contain search_phrases.
        
        The final goal of the research will be to gather all existing resources, tools that can be used and competitors
        """

        self.executor = ModelExecutor(openai, self.context)

    def execute(self):
        response = self.executor.execute(
            """We are trying to develop a protocol which does the following to help people distinguish if an image is genuine or ai generated

            Tracking if the image was algorithmically generated or taken by user on a camera:
            For this an attested camera sensor is used which cryptographically signs an image to prove that the image was indeed taken from a camera

            Tracking the edits on the image:
            For this we will track every edit made on the image and save it in the metadata.

            Verification:
            Any user, when given the image can test if the image was taken by a camera and also verify what edits were made on it 

            """
        )

        keywords = json.loads(response.content())

        json.dump(keywords, open("data/conversations/google/keywords.json", "w"), indent=2)

        return keywords
