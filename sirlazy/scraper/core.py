import threading

import scraper
from .storing import load_new_comics, comics_omparison
from .constants import *

def start():
    star_t = threading.Thread(target=starcomics)
    star_t.start()

    planet_t = threading.Thread(target=planetmanga)
    planet_t.start()

    star_t.join()
    planet_t.join()
        

def show_news(data):
    for d in data:
        print(d["name"])
        print(d["editor"])
        print(d["link"])
        print()

def check_load(data):
    
    newdata = comics_omparison(data)
    if len(newdata) > 0:
        show_news(newdata)
        load_new_comics(newdata)
    
def starcomics():
    data = scraper.starcomics_releases(STARCOMICS_DATA["link"])
    check_load(data)

def planetmanga():
    data = scraper.planetmanga_this_week()
    newdata = scraper.planetmanga_next_releases(PLANETMANGA_DATA["link"])
    data.extend(newdata)
    check_load(data)
