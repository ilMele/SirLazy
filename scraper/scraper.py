from bs4 import BeautifulSoup
import requests

def start(data):
    for site in data:
        res = requests.get(site["link"])
        if res.status_code != 200:
            print("status code is not 200")
            return
        soup = BeautifulSoup(res.content, "html.parser")
        items = soup.find_all(class_= str(site["item"]).replace(".", ""))
        
        for i in items:
            print(i.find(class_=str(site["title"]).replace(".", "")).text)
            print(i.find("a", href=True)["href"])