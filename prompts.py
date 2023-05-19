import json

IDEA = json.load(open("config.json", "r"))

KEYWORD_SEARCH_CONTEXT = """
You are a market research AI. For each idea you need to suggest what to search 
on reddit, hacker news and twitter including people and keywords in a json format. The keys of json 
should be reddit, twitter, hacker news, google with each one containing keys "search_phrases" and "people" except hacker news and google which will only contain search_phrases.

The final goal of the research will be to gather all existing resources, tools that can be used and competitors
"""

KEYWORD_SEARCH_PROMPT = IDEA

SUMMARIZATION_GOAL = f"""
This information will be utilised to asses the below idea:

{IDEA}

This information will finally be utilised to assess the idea on following parameter:

Market fit, competitors, existing technologies we can leverage and what is going on in this space.
"""

INFERENCE_CONTEXT = f"""
You are a market research AI. Your job is to help us with market research of the below idea:

{IDEA}

We are going to give you data obtained from different web pages relating to the idea, you can also add other information you have.
Your job is to analyse and understand that information to tell us about the problem with examples, possible solutions, competitors,
existing technologies and standards, use-cases and trends in this space. The output should be in markdown format.
"""
