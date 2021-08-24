import requests
from bs4 import BeautifulSoup
import re

BaseURL = "https://www.blocket.se/annonser/hela_sverige?q="
ImageURL="https://www.blocket.se"
SearchWord="motorcykel"
Prefix = "&page="

Products = []

class Produkt:
    def __init__(self, name, price, imageURL):
        self.name = name
        self.price = price
        self.ImageURL = imageURL


def get_all_products(webpage):
    elements = webpage.find_all("article", class_="geRkWZ")

    for x in elements:
        name = x.find("div", class_="leTJeS").text
        price = x.find("div", class_="jVOeSj").text
        price = remove_all_charachters(price)

        url = x.find("a", class_="evOAPG")["href"]
        url = ImageURL + url

        Products.append(Produkt(name, price, url))

        save_text_to_file(name,price,url)


def parse_site(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    return soup


def remove_all_charachters(text):
    return re.sub("[^0-9]", "", text)


def get_total_pages(webpage):
    pages = webpage.find_all("a", class_="dMZGCO")
    total_page_numbers = []
    for page in pages:
        page_number = (page.getText())
        total_page_numbers.append(page_number)
    return total_page_numbers[-3]

def save_text_to_file(name, price, url):

    f.write("Name: "+ name + "Pris: " + price + " url: " + url + "\n")


f = open(SearchWord + ".txt", "w")

def main():

    webpage = parse_site(BaseURL+SearchWord)

    total_number_of_pages = int(get_total_pages(webpage))
    print("Number of pages: " + str(total_number_of_pages))

    for page in range(total_number_of_pages):
        full_url = BaseURL+SearchWord+Prefix+str(page+1)
        print(full_url)

        webpage = parse_site(full_url)
        get_all_products(webpage)

    # for idx, product in enumerate(Products):
    #     print(idx)
    #     print(product.name)
    #     print(product.price)
    #     print(product.ImageURL)
    #     print()
    f.close()


    print()
    print("Total products found: " + str(len(Products)))
    print()



main()
