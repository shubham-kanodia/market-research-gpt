from utility.processing import *

from executors.model import ModelExecutor
from prompts import INFERENCE_CONTEXT


class Step4:
    def __init__(self, openai):
        self.openai = openai
        self.output_file_path = "data/research.md"

    def execute(self, summarised_data):
        inference_model = ModelExecutor(self.openai, INFERENCE_CONTEXT)
        prompt = ""

        for key in summarised_data:
            if key.startswith("site:twitter.com"):
                continue

            for idx in summarised_data[key]:
                if get_token_count_gpt3_5(prompt + summarised_data[key][idx]) > 7500:
                    break
                else:
                    prompt += "\n" + summarised_data[key][idx]

        response = inference_model.execute(prompt)
        message = response.content()

        with open(self.output_file_path, "w") as f:
            f.write(message)
