from os import path, makedirs
from sys import exit
import json

DATA_DIR = "data"
SOURCE_FILE = "sources.txt"

JSON_EX = {
    "links": {
        "_link": "www.test.ts",
        "_elements": ["h2", ".test", "#test"],
    }
}

def get_sources_links():
    try:
        f = open(path.join(DATA_DIR, SOURCE_FILE), "r")
        sources = json.loads(f.read())
        f.close()
        return sources
    except FileNotFoundError:
        makedirs(path.join(DATA_DIR))
        f = open(path.join(DATA_DIR, SOURCE_FILE), "w")
        jsstr = json.dumps(JSON_EX, indent=4)
        f.write(jsstr)
        f.close()
        print(f"create {DATA_DIR} folder with {SOURCE_FILE} inside")
        print("add links with elements to scrap")
        exit()
