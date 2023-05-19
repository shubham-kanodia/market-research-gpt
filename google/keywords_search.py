import json
from executors.model import ModelExecutor
from prompts import *


class KeywordsSearch:
    def __init__(self, openai):
        self.openai = openai
        self.context = KEYWORD_SEARCH_CONTEXT

        self.executor = ModelExecutor(openai, self.context)

    def execute(self):
        response = self.executor.execute(
            KEYWORD_SEARCH_PROMPT
        )

        keywords = json.loads(response.content())
        return keywords
