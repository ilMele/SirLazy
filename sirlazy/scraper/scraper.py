import requests, time
from datetime import datetime
from bs4 import BeautifulSoup

# my module
from .constants import *

def starcomics_releases(link):
    data = []

    res = requests.get(link)
    if res.status_code != 200:
        print(f"code: {res.status_code} from {STARCOMICS_DATA['link']}")
        return
    
    soup = BeautifulSoup(res.content, "html.parser")
    
    items = soup.find_all(STARCOMICS_DATA["item"]["tag"], class_= STARCOMICS_DATA["item"]["class"])

    for i in items:
        name = i.find(STARCOMICS_DATA["name"]["tag"], class_=STARCOMICS_DATA["name"]["class"]).text
        name = str(name).strip()

        img_link = i.find("img")["src"]
        img_link = STARCOMICS_DATA["home"] + img_link

        date = i.find(STARCOMICS_DATA["date"]["tag"], class_=STARCOMICS_DATA["date"]["class"]).text
        date = datetime.strptime(str(date),"%d/%m/%Y")
        date = date.strftime("%Y-%m-%d")
        date = datetime.strptime(date, "%Y-%m-%d")

        link = i.find("a", href=True)["href"]
        link = STARCOMICS_DATA["home"] + link

        data.append({
            "name": name,
            "img_path": img_link,
            "date": date,
            "link": link,
            "editor": STARCOMICS_DATA["editor"]
        })

    nextpage = soup.find(STARCOMICS_DATA["nextpage"]["tag"], title=STARCOMICS_DATA["nextpage"]["title"], href=True)
    if nextpage is None:
        return []
    
    nextpage = nextpage["href"]

    time.sleep(1)
    nextdata = starcomics_releases(STARCOMICS_DATA["home"] + nextpage)
    
    data.extend(nextdata)
    return data

def planetmanga_this_week():
    data = []

    res = requests.get(PLANETMANGA_DATA["thisweek"])
    if res.status_code != 200:
        print(f"code: {res.status_code} from {PLANETMANGA_DATA['link']}")
        return
    soup = BeautifulSoup(res.content, "html.parser")
    items = soup.find_all(PLANETMANGA_DATA["item"]["tag"], class_= PLANETMANGA_DATA["item"]["class"])

    for i in items:
        name = i.find(PLANETMANGA_DATA["name"]["tag"], class_=PLANETMANGA_DATA["name"]["class"]).text
        name = str(name).strip()

        img_link = i.find("img")["src"]
        img_link = img_link

        date = i.find(PLANETMANGA_DATA["date"]["tag"], class_=PLANETMANGA_DATA["date"]["class"]).text
        date = date.strip()
        date = datetime.strptime(str(date),"%d/%m/%y")
        date = date.strftime("%Y-%m-%d")
        date = datetime.strptime(date, "%Y-%m-%d")

        link = i.find("a", href=True)["href"]
        link = link

        data.append({
            "name": name,
            "img_path": img_link,
            "date": date,
            "link": link,
            "editor": PLANETMANGA_DATA["editor"]
        })

    return data

def planetmanga_next_releases(link):
    data = []

    res = requests.get(link)
    if res.status_code != 200:
        print(f"code: {res.status_code} from {PLANETMANGA_DATA['link']}")
        return
    soup = BeautifulSoup(res.content, "html.parser")
    items = soup.find_all(PLANETMANGA_DATA["item"]["tag"], class_= PLANETMANGA_DATA["item"]["class"])

    for i in items:
        name = i.find(PLANETMANGA_DATA["name"]["tag"], class_=PLANETMANGA_DATA["name"]["class"]).text
        name = str(name).strip()

        img_link = i.find("img")["src"]
        img_link = img_link

        date = i.find(PLANETMANGA_DATA["date"]["tag"], class_=PLANETMANGA_DATA["date"]["class"]).text
        date = date.strip()
        date = datetime.strptime(str(date),"%d/%m/%y")
        date = date.strftime("%Y-%m-%d")
        date = datetime.strptime(date, "%Y-%m-%d")

        link = i.find("a", href=True)["href"]
        link = link

        data.append({
            "name": name,
            "img_path": img_link,
            "date": date,
            "link": link,
            "editor": PLANETMANGA_DATA["editor"]
        })

    nextpage = soup.find(PLANETMANGA_DATA["nextpage"]["tag"], title=PLANETMANGA_DATA["nextpage"]["title"], href=True)
    if nextpage is None:
        return []
    
    nextpage = nextpage["href"]

    time.sleep(1)
    nextdata = planetmanga_next_releases(nextpage)
    
    data.extend(nextdata)
    return data
