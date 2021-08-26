def save_text_to_file(name, price, url, filename):
    f = open(filename + ".csv", "a", encoding="utf-8")
    f.write(name + "," + price + "," + url + "\n")