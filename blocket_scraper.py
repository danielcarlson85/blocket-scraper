from managers import page_manager, file_manager
import statistics
import time, os

#search_url = "https://www.blocket.se/annonser/hela_sverige/fordon/motorcyklar?cg=1140&f=c"

#search_url = "https://www.blocket.se/annonser/hela_sverige/fordon/motorcyklar/ovrigt?cg=1148&plo=1&q=motorcykel"

search_url = "https://www.blocket.se/annonser/hela_sverige"


#search_url = "https://www.blocket.se/annonser/hela_sverige/for_hemmet?cg=2000"

def main():

    while True:
    
        price_list = []

        full_blocket_base_webpage = page_manager.get_web_page(search_url)
        filename = page_manager.get_search_word(full_blocket_base_webpage, search_url)
        saved_products = file_manager.load_products_from_file(filename)
        found_products = page_manager.get_all_products(saved_products, full_blocket_base_webpage, search_url, filename)

        for price in found_products:
            price_list.append(int(price.price))

        price_sum = 0
        for page in found_products:
            price_sum += int(page.price)

        lowest_price = min(price_list)
        middle_price = int(price_sum / len(found_products))
        median_price = statistics.median(price_list)
        highest_price = max(price_list)

        print("Lowest price: " + str(lowest_price))
        print("Middle price: " + str(middle_price))
        print("Median price: " + str(median_price))
        print("Highest price: " + str(highest_price))

        print("Total products found with prices: " + str(len(found_products)))
        time.sleep(2)
        os.system('cls')

main()
