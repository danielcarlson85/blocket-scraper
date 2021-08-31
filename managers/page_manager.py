import requests
from bs4 import BeautifulSoup
from constants.constants import base_url, prefix
from models import product
from managers import file_manager, string_manager

Products = []


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



def get_all_products(saved_products, full_blocket_base_webpage, search_url, filename):
    
    
    total_number_of_pages = get_total_pages(full_blocket_base_webpage)
    print("Number of pages: " + str(total_number_of_pages))


    for page in range(total_number_of_pages):
        full_url = get_full_page_url(search_url, page)
        print(full_url)
        web_page = get_web_page(full_url)
    
        all_products = web_page.find_all("article", class_="geRkWZ")


        # TODO add variables to product object
        for x in all_products:
            name = x.find("div", class_="leTJeS").text
            name = string_manager.remove_last_character(name)
            name = string_manager.remove_special_characters(name)

            price = x.find("div", class_="jVOeSj").text
            price = string_manager.remove_all_characters(price)
        
            url = x.find("a", class_="evOAPG")["href"]
            url = base_url + url

            date = x.find("p", class_="gEFkeH").text

            try:
                store = x.find("span", class_="hpfPc").text
            except:
                store = ""

            typeandlocation = x.find("p", class_="lbavoU").text
            location = string_manager.get_location_from_string(typeandlocation)
            type = string_manager.get_type_from_string(typeandlocation)
        
            year_model =  x.find("li", class_="kAfCZF").text
        
       

            if len(saved_products) != 0:

                saved_produts_url = saved_products[len(saved_products)-1].url.split("\n")[0]
                if saved_produts_url == url:
                    print(url + " exist in db")
            else:
                if price:

                    new_product = product.Product(name, price, url, location, date, store)
                    Products.append(new_product)

                    file_manager.save_text_to_file(new_product, filename)

                    Products.sort(key=lambda x: x.price)