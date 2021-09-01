import json

class Product:
    def __init__(self, name, price, url, location, date, store, year):
        self.name = name
        self.price = price
        self.url = url
        self.location = location
        self.date = date
        self.store = store
        self.year = year

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4)