import re

def remove_all_charachters(text):
    return re.sub("[^0-9]", "", text)