def save_text_to_file(name, price, url, filename):
    f = open(filename + ".txt", "a", encoding="utf-8")
    f.write("Name: "+ name + "Pris: " + price + " url: " + url + "\n")