from executors.model import ModelExecutor


class SummariseText:
    def __init__(self, openai, goal):
        self.openai = openai
        self.context = f"""
        You are a summarise content AI. 
        For each of the raw text given to you that has been scraped from a website, you need to summarise the text 
        without losing any information which can be used in the final goal.
        
        Goal:\n
        {goal}
        
        REMEMBER - Your response should only contain the summarised text.
        """

        self.executor = ModelExecutor(openai, self.context)

    def execute(self, task):
        response = self.executor.execute(task)

        return response.content()
