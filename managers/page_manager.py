import requests
from bs4 import BeautifulSoup
from Models import product
from managers import file_manager, string_manager

Products = []

def get_web_page(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    return soup


def get_all_products(web_page, search_word, imageURL):

    all_products = web_page.find_all("article", class_="geRkWZ")

    for x in all_products:
        name = x.find("div", class_="leTJeS").text
        price = x.find("div", class_="jVOeSj").text
        price = string_manager.remove_all_charachters(price)

        url = x.find("a", class_="evOAPG")["href"]
        url = imageURL + url

        Products.append(product.Product(name, price, url))
        file_manager.save_text_to_file(name, price, url, search_word)


def get_total_pages(web_page):
    pages = web_page.find_all("a", class_="dMZGCO")
    if len(pages) == 1:
        return 1

    total_page_numbers = []
    for page in pages:
        page_number = (page.getText())
        total_page_numbers.append(page_number)
    return int(total_page_numbers[-3])

