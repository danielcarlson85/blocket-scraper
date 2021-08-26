import sys

def save_text_to_file(name, price, url, filename):
    try:
        f = open(filename + ".csv", "a", encoding="utf-8")
        f.write(name + "," + price + "," + url + "\n")
    except:
        print("Cannot open file, check if it is already opend")
        sys.exit()
