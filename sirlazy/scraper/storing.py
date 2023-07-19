from pymongo import MongoClient
from threading import Lock

lock = Lock()

client = MongoClient()

db = client["sirlazy"]

comic_cols = db["comic"]

def load_new_comics(data):
    with lock:
        comic_cols.insert_many(data)

def comics_omparison(newdata):
    docs = []
    with lock:
        docs = list(comic_cols.find({"editor": newdata[0]["editor"]}).sort("date", 1))
        news = []

    for n in newdata:
        add = True
        for d in docs:
            if compare_comic_dict(n, d):
                add = False
                break
        if add:
            news.append(n)

    return news

def compare_comic_dict(a, b):
    for k in dict(a).keys():
        if a[k] != b[k]:
            return False
        
    return True