class Response:
    def __init__(self, response):
        self.response = response

    def content(self):
        choice = self.response["choices"][0]
        message = choice["message"]["content"]
        return message
    