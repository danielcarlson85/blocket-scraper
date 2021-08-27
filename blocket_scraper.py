from managers import page_manager, file_manager
import statistics

searchURL = "https://www.blocket.se/annonser/hela_sverige?q=yamaha"


def main():
    full_blocket_base_webpage = page_manager.get_web_page(searchURL)
    search_word = page_manager.get_search_word(full_blocket_base_webpage)

    file_manager.check_if_file_exist_and_delete(search_word)

    total_number_of_pages = page_manager.get_total_pages(full_blocket_base_webpage)

    if not total_number_of_pages:
        print("No products found")
        return

    print("Number of pages: " + str(total_number_of_pages))

    price_list = []

    for page in range(total_number_of_pages):
        full_url = file_manager.get_full_page_url(searchURL, page)
        print(full_url)
        webpage = page_manager.get_web_page(full_url)
        page_manager.get_all_products(webpage, search_word)

    for price in page_manager.Products:
        price_list.append(int(price.price))

    price_sum = 0
    for page in page_manager.Products:
        price_sum += int(page.price)

    lowest_price = min(price_list)
    middle_price = int(price_sum / len(page_manager.Products))
    median_price = statistics.median(price_list)
    highest_price = max(price_list)

    print("Lowest price: " + str(lowest_price))
    print("Middle price: " + str(middle_price))
    print("Median price: " + str(median_price))
    print("Highest price: " + str(highest_price))

    print("Total products found with prices: " + str(len(page_manager.Products)))
    print()


main()
