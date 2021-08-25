import os.path
from managers import page_manager
import statistics

baseURL = "https://www.blocket.se/annonser/hela_sverige/fordon/bilar?cg=1020&ps=2&q=volvo%20v70%20d5&sort=price"
imageURL= "https://www.blocket.se"
search_word= ""
prefix = "&page="


def check_if_file_exist_and_delete():
    if os.path.isfile(search_word + ".txt"):
        os.remove(search_word + ".txt")


def get_full_page_url(page):
    return baseURL + search_word + prefix + str(page + 1)


def get_full_web_page_url():
    return baseURL + search_word

def clear_list_from_empty_price(prodList):

    for idx, prod in enumerate(prodList):
        if not prod.price:
            del prodList[idx]
    return prodList

def main():

    check_if_file_exist_and_delete()
    web_page_url = get_full_web_page_url()
    parsed_web_page = page_manager.get_web_page(web_page_url)
    total_number_of_pages = page_manager.get_total_pages(parsed_web_page)

    print("Number of pages: " + str(total_number_of_pages))

    priceList = []

    for page in range(total_number_of_pages):
        full_url = get_full_page_url(page)
        print(full_url)
        webpage = page_manager.get_web_page(full_url)
        page_manager.get_all_products(webpage, search_word, imageURL)

    for price in page_manager.Products:
        priceList.append(int(price.price))

    sum = 0
    for page in page_manager.Products:
        sum += int(page.price)

    lowest_price = min(priceList)
    middle_price = int(sum/len(page_manager.Products))
    median_price=statistics.median(priceList)
    highest_price= max(priceList)

    print("Lowest price: " + str(lowest_price))
    print("Middle price: "+ str(middle_price))
    print("Median price: " + str(median_price))
    print("Highest price: " + str(highest_price))

    print("Total products found: " + str(len(page_manager.Products)))
    print()


main()
