import re


def remove_all_characters(text):
    return re.sub("[^0-9]", "", text)


def remove_last_character(text):
    last_character = text[len(text) - 1]
    if last_character == " ":
        size = len(text)
        text = text[:size - 1]

    return 

def remove_special_characters(text):
    return text.replace(",","")

    return text

def get_location_from_string(text):
    text = text.split("\xa0·\xa0")
    return text[1]

def get_type_from_string(text):
    text = text.split("\xa0·\xa0")
    return text[0]
