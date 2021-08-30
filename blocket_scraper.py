from managers import page_manager, file_manager
import statistics

search_url = "https://www.blocket.se/annonser/hela_sverige/fordon/motorcyklar?cg=1140&f=c"

search_word = "test"

def main():

    price_list = []

    saved_products = file_manager.load_products_from_file(search_word)



    page_manager.get_all_products(search_word, saved_products,search_url)

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