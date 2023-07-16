import threading, time, requests
from datetime import datetime
from bs4 import BeautifulSoup

# my module
import constants as cs

THREAD_TIME = 10

def start():
    star_t = threading.Thread(target=starcomics)
    star_t.start()

    star_t.join()
        
    
def starcomics():
    starcomics_latest(cs.STARCOMICS_DATA["link"])
    time.sleep(THREAD_TIME)

def starcomics_latest(link):
    thismonth = int(datetime.now().strftime("%m"))

    res = requests.get(link)
    if res.status_code != 200:
        print(f"code: {res.status_code} from {cs.STARCOMICS_DATA['link']}")
        return
    
    soup = BeautifulSoup(res.content, "html.parser")

    items = soup.find_all(cs.STARCOMICS_DATA["item"]["tag"], class_= cs.STARCOMICS_DATA["item"]["class"])

    for i in items:
        title = i.find(cs.STARCOMICS_DATA["title"]["tag"], class_=cs.STARCOMICS_DATA["title"]["class"]).text
        title = str(title).strip()

        img_link = i.find("img")["src"]
        img_link = cs.STARCOMICS_DATA["home"] + img_link

        date = i.find(cs.STARCOMICS_DATA["date"]["tag"], class_=cs.STARCOMICS_DATA["date"]["class"]).text
        date = datetime.strptime(str(date),'%d/%m/%Y')
        month = int(date.strftime("%m"))
        if month != thismonth:
            return
        
        date = date.strftime("%d/%m/%Y")
        link = i.find("a", href=True)["href"]
        link = cs.STARCOMICS_DATA["home"] + link

        
        print(title)
        print(img_link)
        print(date)
        print(link)
        print()

    nextpage = soup.find(cs.STARCOMICS_DATA["nextpage"]["tag"], title=cs.STARCOMICS_DATA["nextpage"]["title"], href=True)
    nextpage = nextpage["href"]

    starcomics_latest(cs.STARCOMICS_DATA["home"] + nextpage)

