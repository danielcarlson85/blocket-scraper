from pagegetter import *
import os.path

baseURL = "https://www.blocket.se/annonser/hela_sverige?q="
imageURL= "https://www.blocket.se"
search_word= "bil"
prefix = "&page="

def check_if_file_exist():
    if os.path.isfile(search_word + ".txt"):
        os.remove(search_word + ".txt")


def get_full_url(page):
    return baseURL + search_word + prefix + str(page + 1)


def main():

    check_if_file_exist()

    site = baseURL + search_word
    parsed_web_page = parsesite(site)

    total_number_of_pages = int(get_total_pages(parsed_web_page))

    print("Number of pages: " + str(total_number_of_pages))

    for page in range(total_number_of_pages):
        full_url = get_full_url(page)
        print(full_url)

        webpage = parsesite(full_url)
        get_all_products(webpage, search_word, imageURL)

    print()
    print("Total products found: " + str(len(Products)))
    print()


main()