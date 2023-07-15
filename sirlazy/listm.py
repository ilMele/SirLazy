from os import path, makedirs
from sys import exit
import json

DATA_DIR = "data"
SOURCE_FILE = "sources.txt"

JSON_EX = {
    "test": [
        {
            "link": "https://j-pop.it/it/catalog/category/view/id/696/s/fumetti/?product_list_dir=desc&product_list_order=position",
            "item": {
                "tag": "div",
                "id": ".product-item-info"
            },
            "title": {
                "tag": "a",
                "id": ".product-item-link"
            },
            "asdf": {
                "tag": "a",
                "id": ".product-item-link"
            }
        }
    ]
}

class Listm:
    def __init__(self):
        self.data = dict()
        self.get_lists()

    def get_lists(self):
        try:
            f = open(path.join(DATA_DIR, SOURCE_FILE), "r")
            data = json.loads(f.read())
            f.close()
            self.data = data
        except FileNotFoundError:
            makedirs(path.join(DATA_DIR))
            f = open(path.join(DATA_DIR, SOURCE_FILE), "w")
            jsstr = json.dumps(JSON_EX, indent=4)
            f.write(jsstr)
            f.close()
            print(f"create {DATA_DIR} folder with {SOURCE_FILE} inside")
            print("add links with elements to scrap")
            exit()

    def show_all(self):
        for name in self.data.keys():
            print(name)

    def show(self, name):
        if self.data.get(name) is None:
            print(f"Wrong list name: {name}")
            return
        
        for e in self.data[name]:
            print(e["link"])

    def get(self, name):
        if self.data.get(name) is None:
            print(f"Wrong list name: {name}")
            return

        return self.data.get(name)
