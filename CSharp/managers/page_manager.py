import requests
from bs4 import BeautifulSoup
from constants.constants import base_url, prefix
from models import product
from managers import file_manager, string_manager

def get_web_page(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    return soup

def get_full_page_url(search_url, page):
    return search_url + prefix + str(page + 1)

def get_search_word(web_page, full_url):

    try:
        search_word=web_page.find_all("h1", class_="bnGrQe")[0].text.split("\"")[1]
        return search_word
    except:
        urls = full_url.split("?")[0].split("/")
        search_word = urls[len(urls)-1]

    return search_word

    
def get_total_pages(web_page):

    pages = web_page.find_all("a", class_="dMZGCO")

    if not len(pages) or len(pages) == 1:
            return 1

    total_page_numbers = []
    for page in pages:
        page_number = (page.getText())
        total_page_numbers.append(page_number)
    return int(total_page_numbers[-3])


def get_product_name(product):
    name = product.find("div", class_="leTJeS").text
    name = string_manager.remove_last_character(name)
    name = string_manager.remove_special_characters(name)
    return name


def get_product_price(product):
            price = product.find("div", class_="jVOeSj").text
            price = string_manager.remove_all_characters(price)
            return price


def get_product_url(product):
    url = product.find("a", class_="evOAPG")["href"]
    url = base_url + url
    return url


def get_product_date(product):
    date = product.find("p", class_="gEFkeH").text
    return date


def get_product_store_type(product):
    try:
        store = product.find("span", class_="hpfPc").text
    except:
        store = "Private"
    return store


def get_product_location(product):
    typeandlocation = product.find("p", class_="lbavoU").text
    location = string_manager.get_location_from_string(typeandlocation)
    return location


def get_product_type(product):
    typeandlocation = product.find("p", class_="lbavoU").text
    type = string_manager.get_type_from_string(typeandlocation)
    return type


def get_product_year_model(product):
    try:
        year_model =  product.find("li", class_="kAfCZF").text
    except:
        year_model = ""

    return year_model


def check_if_product_exist_in_list(saved_products, url):
    for product in reversed(saved_products):
        if product.url == url:
            return True

    return False


def save_to_file(date, filename, location, name, price, products, store, url, year):
    if price:
        new_product = product.Product(name, price, url, location, date, store, year)
        products.append(new_product)
        file_manager.save_text_to_file(new_product, filename)
        products.sort(key=lambda x: x.price)

def get_all_products(saved_products, full_blocket_base_webpage, search_url, filename):
    total_number_of_pages = get_total_pages(full_blocket_base_webpage)
    
    products = []
    is_product_in_list = False

    for page in range(total_number_of_pages):
        full_url = get_full_page_url(search_url, page)
        web_page = get_web_page(full_url)

        all_products = web_page.find_all("article", class_="geRkWZ")

        for found_product in all_products:
            name = get_product_name(found_product)
            price = get_product_price(found_product)
            url = get_product_url(found_product)
            date = get_product_date(found_product)
            store = get_product_store_type(found_product)
            location = get_product_location(found_product)
            type = get_product_type(found_product)
            year = get_product_year_model(found_product)

            if len(saved_products) != 0:
                is_product_in_list = check_if_product_exist_in_list(saved_products, url)
                if not is_product_in_list:
                       save_to_file(date, filename, location, name, price, products, store, url, year)
                else:
                    #print("Database is up to date")
                    return saved_products
            else:
                save_to_file(date, filename, location, name, price, products, store, url, year)

    return products