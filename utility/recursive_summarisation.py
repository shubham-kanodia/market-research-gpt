from executors.model import ModelExecutor
from utility.processing import get_token_count_gpt3_5


class Splitter:
    def __init__(self, original_text):
        self.text = original_text
        self.whitespace_split = original_text.split(" ")

        self.given_chunks = 0
        self.last_idx = 0

    def get_chunk(self, existing_content=""):
        if self.last_idx == len(self.whitespace_split):
            return None

        current_chunk = ""
        current_token_len = get_token_count_gpt3_5(existing_content)

        for idx, word in enumerate(self.whitespace_split[self.last_idx:]):
            word_token_len = get_token_count_gpt3_5(word)

            if current_token_len + word_token_len <= 3000:
                current_chunk += " " + word
                current_token_len += word_token_len
            else:
                self.given_chunks += 1
                self.last_idx = idx

                return current_chunk

        self.last_idx = len(self.whitespace_split)
        return current_chunk


class RecursivelySummariseText:
    def __init__(self, openai, goal, model_name="gpt-3.5-turbo"):
        self.openai = openai
        self.context = f"""
        You are a content summarising AI. 
        For each of the raw text given to you that has been scraped from a website, you need to summarise the text 
        without losing any information which can be used in the final goal. Along with the new text we might also give
         you previously summarised text so that you can summarise the complete information for the final goal

        Goal:\n
        {goal}        

        REMEMBER - Your response should only contain the summarised text.
        """

        self.executor = ModelExecutor(openai, self.context, model_name=model_name)

    def _execute(self, task):
        response = self.executor.execute_without_memory(task)

        return response.content()

    def _split_text(self, text):
        chunks = []

        whitespace_split = text.split()

        current_piece = ""
        current_token_len = 0

        for word in whitespace_split:
            word_token_len = get_token_count_gpt3_5(word)

            if current_token_len + word_token_len < 4000:
                current_piece += " " + word
                current_token_len += word_token_len

            else:
                chunks.append(current_piece)

                current_piece = f"Text continued from last message:\n {word}"
                current_token_len = get_token_count_gpt3_5(current_piece)

        if len(current_piece) > 50:
            chunks.append(current_piece)

        return chunks

    def summarise(self, text):

        if get_token_count_gpt3_5(text) < 3000:
            return self._execute(text)

        if get_token_count_gpt3_5(text) > 30000:
            return ""

        else:
            splitter = Splitter(text)

            prev_summary = ""
            for idx in range(10):
                chunk = splitter.get_chunk(prev_summary)

                if not chunk:
                    break

                if not prev_summary:
                    message = f"Raw data:\n {chunk}"

                else:
                    message = f"Previously summarised text:\n {prev_summary} \n\n Raw data to add to summary:\n {chunk}"

                response = self._execute(message)
                prev_summary = response

            return prev_summary
