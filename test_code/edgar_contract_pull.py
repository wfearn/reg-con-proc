import requests
from bs4 import BeautifulSoup
import os
import time
import random

url = "https://www.sec.gov/cgi-bin/srch-edgar?text=FORM-TYPE%3D8-K&start=1&count=80&first=1994&last=2016" 
OUTPUT_FILE_PATH = "/local/wfearn/Documents/NLPLab/lab_scripts/WebCrawler/data_dump/{}"
BASE_URL = "https://www.sec.gov{}"
PAGE_COUNT = 50
start = 0 
ONE_MINUTE = 60
TWO_MINUTES = 120
NEXT_PAGE = "[NEXT]"

while start < PAGE_COUNT:


    rand = random.randint(ONE_MINUTE, TWO_MINUTES) 
    
    print "opening {}".format(url)

    html = requests.get(url)

    time.sleep(rand)

    soup = BeautifulSoup(html.text, "lxml")

    for link in soup.find_all('a'):
        href = link.get('href')

        filename = os.path.split(href)[1]

        new_file_path = OUTPUT_FILE_PATH.format(filename)

        if href.endswith('.txt'):
            print "Getting {} from {}".format(href, filename)

            with open(new_file_path, 'wb') as new_file:
                new_file.write(requests.get(BASE_URL.format(href)).content)
                time.sleep(rand)

        elif str(link.string) == NEXT_PAGE:
            url = BASE_URL.format(href)

    start += 1
