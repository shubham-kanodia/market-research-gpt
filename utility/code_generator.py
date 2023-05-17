from executors.model import ModelExecutor


class CodeGenerator:
    def __init__(self, openai):
        self.openai = openai
        self.context = """
        You are a code generator AI. For each of the task mentioned, you need to generate python code for it.
        Your response should contain only the code and nothing else
        """

        self.executor = ModelExecutor(openai, self.context)

    def execute(self, task):
        response = self.executor.execute(task)

        return response.content()
