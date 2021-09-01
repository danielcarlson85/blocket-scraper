import logging
import azure.functions as func
from blocket_scraper import blocket_scraper as scraper
import statistics
from datetime import datetime


def main(req: func.HttpRequest) -> func.HttpResponse:

    logging.info('Python HTTP trigger function processed a request.')
    
    found_products, price_list = scraper.start()
    
    price_sum = 0
    for page in found_products:
        price_sum += int(page.price)

    lowest_price = min(price_list)
    middle_price = int(price_sum / len(found_products))
    median_price = statistics.median(price_list)
    highest_price = max(price_list)

    logging.info("Lowest price: " + str(lowest_price) + " " + found_products[0].url)
    logging.info("Middle price: " + str(middle_price))
    logging.info("Median price: " + str(median_price))
    logging.info("Highest price: " + str(highest_price) + " " + found_products[len(found_products)-1].url)

    logging.info("Total products with prices: " + str(len(found_products)))
    logging.info("To see all results open file in /results folder")

    results = ""
    
    date_and_time = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    for x in found_products:
        results += x.name + "," + x.price + "," + x.url + "," + x.location + "," + x.store + "," + x.date + "\n"

    results += "\n" + "Database is now updated" + ": " + date_and_time
    results += "\n" 

    results += "\n" + "Lowest price: " + str(lowest_price) + " " + found_products[0].url
    results += "\n" + "Middle price: " + str(middle_price)
    results += "\n" + "Median price: " + str(median_price)
    results += "\n" + "Highest price: " + str(highest_price) + " " + found_products[len(found_products)-1].url
    results += "\n" 

    results += "\n" + "Total products with prices: " + str(len(found_products))
    results += "\n" + "To see all results open file in /results folder"


    return func.HttpResponse(results, status_code= 200)
