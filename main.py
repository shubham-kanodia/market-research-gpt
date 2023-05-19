import os

import openai
from dotenv import load_dotenv

from steps.step_1 import Step1
from steps.step_2 import Step2
from steps.step_3 import Step3
from steps.step_4 import Step4

load_dotenv("data/.env")

openai.organization = os.getenv("OPENAI_ORG_ID")
openai.api_key = os.getenv("OPENAI_API_KEY")

# Step 1 - Generation of keywords

step1 = Step1(openai)
keywords = step1.execute()

# Step 2 - Prepare keywords list, scrape data, process scraped data

step2 = Step2(openai)
scraped_data = step2.execute(keywords)

# Step 3 - Summarization of data

step3 = Step3(openai)
summarised_data = step3.execute(scraped_data)

# Step 4 - Inference

step4 = Step4(openai)
step4.execute(summarised_data)

print("The result is in data/research.md file")
