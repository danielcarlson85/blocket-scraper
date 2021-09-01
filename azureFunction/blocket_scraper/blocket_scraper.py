from blocket_scraper.managers import page_manager, file_manager


#search_url = "https://www.blocket.se/annonser/hela_sverige/fordon/motorcyklar?cg=1140&f=c"
#search_url = "https://www.blocket.se/annonser/hela_sverige/fordon/motorcyklar/ovrigt?cg=1148&plo=1&q=motorcykel"
#search_url = "https://www.blocket.se/annonser/hela_sverige"
#search_url = "https://www.blocket.se/annonser/hela_sverige/for_hemmet?cg=2000"
#search_url = "https://www.blocket.se/annonser/hela_sverige/fordon/motorcyklar/custom?cg=1142&q=yamaha%20virago%201100"
search_url = "https://www.blocket.se/annonser/hela_sverige/fordon/motorcyklar/scooter?cg=1144&q=yamaha"

def start():

    price_list = []
    full_blocket_base_webpage = page_manager.get_web_page(search_url)
    filename = page_manager.get_search_word(full_blocket_base_webpage, search_url)
    saved_products = file_manager.load_products_from_file(filename)
    found_products = page_manager.get_all_products(saved_products, full_blocket_base_webpage, search_url, filename)

    for price in found_products:
        price_list.append(int(price.price))

    found_products.sort(key=lambda x: x.price)

    return found_products, price_list