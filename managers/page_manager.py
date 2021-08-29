import requests
from bs4 import BeautifulSoup
from constants.constants import base_url
from models import product
from managers import file_manager, string_manager

Products = []


def get_web_page(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    return soup


def get_search_word(web_page):
    try:
        search_word=web_page.find_all("h1", class_="bnGrQe")[0].text.split("\"")[1]
        return search_word
    except:
        return "product"


def get_all_products(web_page, search_word):
    all_products = web_page.find_all("article", class_="geRkWZ")


    # TODO add variables to product object
    for x in all_products:
        name = x.find("div", class_="leTJeS").text
        name = string_manager.remove_last_character(name)
        price = x.find("div", class_="jVOeSj").text
        price = string_manager.remove_all_characters(price)
        
        url = x.find("a", class_="evOAPG")["href"]
        url = base_url + url

        date = x.find("p", class_="gEFkeH").text
        butik = x.find("span", class_="hpfPc").text

        typeandlocation = x.find("p", class_="lbavoU").text
        location = string_manager.get_location_from_string(typeandlocation)
        type = string_manager.get_type_from_string(typeandlocation)
        
        year_model =  x.find("li", class_="kAfCZF").text
        
        if price:
            Products.append(product.Product(name, price, url))
            file_manager.save_text_to_file(name, price, url, search_word)

    Products.sort(key=lambda x: x.price)


def get_total_pages(web_page):
    pages = web_page.find_all("a", class_="dMZGCO")

    if not len(pages) or len(pages) == 1:
            return 1

    total_page_numbers = []
    for page in pages:
        page_number = (page.getText())
        total_page_numbers.append(page_number)
    return int(total_page_numbers[-3])
