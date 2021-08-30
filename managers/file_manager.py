import os.path
from constants.constants import prefix
from models import product
import json



def save_text_to_file(product, filename):
    
    #jsonString = product.toJSON

    f = open("results\\" + filename + ".txt", "a", encoding="utf-8")
    f.writelines(product.name + "," + product.price + "," + product.url + "," + product.location + "," + product.date + "," + "\n")


def check_if_file_exist_and_delete(filename):
    if os.path.isfile(filename + ".txt"):
        os.remove(filename + ".txt")


def load_products_from_file(filename):

    products = []

    if os.path.isfile("results\\"+ filename + ".txt"):

        fh = open("results\\" + filename + ".txt").readlines()
        for line in fh:
            row = line.split(',')
            name = row[0]
            price = row[1]
            url = row[2]
            location = row[3]
            date = row[4]
            store = row[5]

            products.append(product.Product(name, price, url, location, date, store))

    return products