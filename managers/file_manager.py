import os.path
from constants.constants import prefix


def save_text_to_file(name, price, url, filename):
    f = open(filename + ".txt", "a", encoding="utf-8")
    f.write(name + "," + price + "," + url + "\n")


def check_if_file_exist_and_delete(search_word):
    if os.path.isfile(search_word + ".txt"):
        os.remove(search_word + ".txt")


def get_full_page_url(search_url, page):
    return search_url + prefix + str(page + 1)
