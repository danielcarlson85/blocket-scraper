import os.path
from constants.constants import prefix
from models import product



def save_text_to_file(name, price, url, filename):
    f = open(filename + ".txt", "a", encoding="utf-8")
    f.write(name + "," + price + "," + url + "\n")


def check_if_file_exist_and_delete(search_word):
    if os.path.isfile(search_word + ".txt"):
        os.remove(search_word + ".txt")


def get_full_page_url(search_url, page):
    return search_url + prefix + str(page + 1)


def load_products_from_file():
    products = []
    fh = open('product.txt').readlines()
    for line in fh:
        row = line.split(',')
        name = row[0]
        price = row[1]
        url = row[2]

        products.append(product.Product(name, price, url))

    return products