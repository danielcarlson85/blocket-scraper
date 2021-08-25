import requests
from bs4 import BeautifulSoup
from stringmanager import remove_all_charachters
from filemanager import *
from product import Product

BaseURL = "https://www.blocket.se/annonser/hela_sverige?q="
ImageURL="https://www.blocket.se"
SearchWord="bil"

Prefix = "&page="
Products = []

def get_all_products(webpage):
    elements = webpage.find_all("article", class_="geRkWZ")

    for x in elements:
        name = x.find("div", class_="leTJeS").text
        price = x.find("div", class_="jVOeSj").text
        price = remove_all_charachters(price)

        url = x.find("a", class_="evOAPG")["href"]
        url = ImageURL + url
        Products.append(Product(name, price, url))
        save_text_to_file(name,price,url, SearchWord)


def parse_site(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    return soup


def get_total_pages(webpage):
    pages = webpage.find_all("a", class_="dMZGCO")
    total_page_numbers = []
    for page in pages:
        page_number = (page.getText())
        total_page_numbers.append(page_number)
    return total_page_numbers[-3]


def main():

    webpage = parse_site(BaseURL+SearchWord)

    name = webpage.find("div", class_="icDoQT").text



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

    print()
    print("Total products found: " + str(len(Products)))
    print()



main()