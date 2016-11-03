#Charles Dellebovi
#Pratt LIS-664-01: Fall 2016
#Programming for Cultural Heritage: Weekly Challenge 8 - BKM GitHub
#List of Exhibitions Held at the Brooklyn Museum with Available Photographs and Didactics.

from bs4 import BeautifulSoup

import requests, json

all_exhibitions = []
current_page = 0

while current_page <= 14:

    url = "https://www.brooklynmuseum.org/opencollection/search?hasImages=on&require_didactic=on&x=12&y=11&type=exhibitions&limit=12&offset=" + str(current_page*12)

    print("Downloading Page" + url)
    exhibitions_page = requests.get(url)
    page_html = exhibitions_page.text

    soup = BeautifulSoup(page_html, "html.parser")

    exhibition_info = soup.find_all("span", attrs = {"class": "item-title"})

    for an_exhibition in exhibition_info:

            if an_exhibition not in all_exhibitions:

                all_exhibitions.append(an_exhibition.text)
 
    current_page = current_page + 1
    print("Page", current_page, "of 15 Complete")
 
with open('CDellebovi_WeeklyChallenge8_BKM_GitHub.json', 'w') as f:
    f.write(json.dumps(sorted(set(all_exhibitions)),indent=4))
