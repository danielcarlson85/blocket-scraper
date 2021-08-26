import os.path
from managers import page_manager
import statistics
import constants

searchURL = "https://www.blocket.se/annonser/hela_sverige?q=yamaha%204335"

def check_if_file_exist_and_delete(search_word):
    if os.path.isfile(search_word + ".txt"):
        os.remove(search_word + ".txt")


def get_full_page_url(page):
    return searchURL + constants.prefix + str(page + 1)


def main():

    parsed_web_page = page_manager.get_web_page(searchURL)
    search_word = page_manager.get_search_word(parsed_web_page)

    check_if_file_exist_and_delete(search_word)

    total_number_of_pages = page_manager.get_total_pages(parsed_web_page)

    if not total_number_of_pages:
        print("No products found")
        return

    print("Number of pages: " + str(total_number_of_pages))

    price_list = []

    for page in range(total_number_of_pages):
        full_url = get_full_page_url(page)
        print(full_url)
        webpage = page_manager.get_web_page(full_url)
        page_manager.get_all_products(webpage, search_word)

    for price in page_manager.Products:
        price_list.append(int(price.price))

    sum = 0
    for page in page_manager.Products:
        sum += int(page.price)

    lowest_price = min(price_list)
    middle_price = int(sum/len(page_manager.Products))
    median_price = statistics.median(price_list)
    highest_price = max(price_list)

    print("Lowest price: " + str(lowest_price))
    print("Middle price: " + str(middle_price))
    print("Median price: " + str(median_price))
    print("Highest price: " + str(highest_price))

    print("Total products found with prices: " + str(len(page_manager.Products)))
    print()


main()
