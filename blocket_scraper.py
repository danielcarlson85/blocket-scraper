import os.path
from managers import page_manager


baseURL = "https://www.blocket.se/annonser/hela_sverige?q="
imageURL= "https://www.blocket.se"
search_word= "bil"
prefix = "&page="


def check_if_file_exist_and_delete():
    if os.path.isfile(search_word + ".txt"):
        os.remove(search_word + ".txt")


def get_full_page_url(page):
    return baseURL + search_word + prefix + str(page + 1)


def get_full_web_page_url():
    return baseURL + search_word


def main():

    check_if_file_exist_and_delete()
    web_page_url = get_full_web_page_url()
    parsed_web_page = page_manager.get_web_page(web_page_url)
    total_number_of_pages = page_manager.get_total_pages(parsed_web_page)

    print("Number of pages: " + str(total_number_of_pages))

    for page in range(total_number_of_pages):
        full_url = get_full_page_url(page)
        print(full_url)
        webpage = page_manager.get_web_page(full_url)
        page_manager.get_all_products(webpage, search_word, imageURL)

    print()
    print("Total products found: " + str(len(page_manager.Products)))
    print()


main()
