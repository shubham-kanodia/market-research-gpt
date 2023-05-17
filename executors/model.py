from responses.response import Response


class ModelExecutor:
    def __init__(self, openai, system, model_name="gpt-4"):
        self.model_name = model_name
        self.system = system
        self.openai = openai
        self.messages = [{"role": "system", "content": self.system}]

    def execute(self, message):
        self.messages.append({"role": "user", "content": message})

        resp = self.openai.ChatCompletion.create(
            model="gpt-4",
            messages=self.messages
        )

        wrapped_response = Response(resp)
        response_content = wrapped_response.content()

        self.messages.append({"role": "assistant", "content": response_content})
        return wrapped_response
