import re


def remove_all_characters(text):
    return re.sub("[^0-9]", "", text)


def remove_last_character(text):
    last_character = text[len(text) - 1]
    if last_character == " ":
        size = len(text)
        text = text[:size - 1]

    return text
