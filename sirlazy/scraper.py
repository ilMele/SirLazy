import threading, json
from bs4 import BeautifulSoup
import requests

def core(data):
    threadlist = []
    for site in data:
        t = threading.Thread(target=start, args=(site,))
        t.start()
        threadlist.append(t)

    for t in threadlist:
        t.join()
    

def start(site):
    res = requests.get(site["link"])
    if res.status_code != 200:
        print(f"{res.status_code} from {site['link']}")
        return
    
    data = list()
    soup = BeautifulSoup(res.content, "html.parser")
    items = soup.find_all(site["item"]["tag"], class_= str(site["item"]["id"]).replace(".", ""))
    
    for i in items:
        title = i.find(site["title"]["tag"], class_=str(site["title"]["id"]).replace(".", "")).text
        link = i.find("a", href=True)["href"]
        data.append({
            title: title,
            link: link
        })

    print(json.dumps(data, indent=4))

