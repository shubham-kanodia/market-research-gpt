from responses.response import Response


class ModelExecutor:
    def __init__(self, openai, system, model_name="gpt-4-32k-0314"):
        self.model_name = model_name
        self.system = system
        self.openai = openai
        self.messages = [{"role": "system", "content": self.system}]

    def execute(self, message):
        self.messages.append({"role": "user", "content": message})

        resp = self.openai.ChatCompletion.create(
            model=self.model_name,
            messages=self.messages
        )

        wrapped_response = Response(resp)
        response_content = wrapped_response.content()

        self.messages.append({"role": "assistant", "content": response_content})
        return wrapped_response

    def execute_all(self, messages):
        for message in messages:
            self.messages.append({"role": "user", "content": message})

        resp = self.openai.ChatCompletion.create(
            model=self.model_name,
            messages=self.messages
        )

        wrapped_response = Response(resp)
        response_content = wrapped_response.content()

        self.messages.append({"role": "assistant", "content": response_content})
        return wrapped_response

    def execute_without_memory(self, message):
        messages = self.messages + [{"role": "user", "content": message}]

        resp = self.openai.ChatCompletion.create(
            model=self.model_name,
            messages=messages
        )

        wrapped_response = Response(resp)
        return wrapped_response
