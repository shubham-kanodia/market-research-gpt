import tiktoken

encoding_3_5 = tiktoken.encoding_for_model("gpt-3.5-turbo")
encoding_4 = tiktoken.encoding_for_model("gpt-4-32k")


def process_info(info):
    str_en = info.encode("ascii", "ignore")
    str_de = str_en.decode()

    return str_de


def get_token_count_gpt3_5(text):
    return len(encoding_3_5.encode(text))


def split_text(text):
    chunks = []

    whitespace_split = text.split()

    current_piece = ""
    current_token_len = 0

    for word in whitespace_split:
        word_token_len = get_token_count_gpt3_5(word)

        if current_token_len + word_token_len < 8000:
            current_piece += " " + word
            current_token_len += word_token_len

        else:
            chunks.append(current_piece)

            current_piece = f"Text continued from last message:\n {word}"
            current_token_len = get_token_count_gpt3_5(current_piece)

    if len(current_piece) > 50:
        chunks.append(current_piece)

    return chunks
