import json

from utility.recursive_summarisation import RecursivelySummariseText
from prompts import *


class Step3:
    def __init__(self, openai):
        self.openai = openai
        self.output_file_path = "data/summary.json"

    def check_existing_data(self):
        try:
            summarised_data = json.load(open(self.output_file_path, "r"))
            return summarised_data
        except Exception as exp:
            return {}

    def execute(self, scraped_data):
        summarised_data = self.check_existing_data()

        done_set = set()
        for key in summarised_data:
            for idx in summarised_data[key]:
                done_set.add(f"{key} - {idx}")

        model = RecursivelySummariseText(self.openai, SUMMARIZATION_GOAL)

        for key in scraped_data:
            for idx, info in enumerate(scraped_data[key]):
                if f"{key} - {idx}" in done_set:
                    continue

                message = f"Information about {key} - {idx}/{len(scraped_data[key])}\n" + info
                summary = model.summarise(message)

                if key in summarised_data:
                    summarised_data[key][idx] = summary
                else:
                    summarised_data[key] = {idx: summary}

                with open(self.output_file_path, "w") as f:
                    json.dump(summarised_data, f, indent=2)

                print(f"[Completed] Key / Index: {key} / {idx}")

        return summarised_data
