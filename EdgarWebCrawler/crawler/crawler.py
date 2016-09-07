import time

import random

import urllib.request

URL_TEMPLATE = 'ftp://ftp.sec.gov/edgar/full-index/{}/QTR{}/master.idx'
BASE_8K_URL = 'ftp://ftp.sec.gov/{}'
EARLIEST = 1993
LATEST = 2016
Q1 = 1
Q4 = 4

class Crawler:
    def __init__(self):
        self.master_indices = {}

    def get_master_indices(self):
        for i in range(1994, 1995 + 1):
            for j in range(Q1, Q4 + 1):
                if i == 2016 and j == 4:
                    pass

                else:
                    path = URL_TEMPLATE.format(i, j)
                    print ('Opening new path: %s' % (path))


                    url = urllib.request.urlopen(path)
                    doc = url.read()

                    self.master_indices[path] = doc

                    wait = random.randint(10, 30)
                    print ('Waiting %s seconds' % (str(wait)))

                    time.sleep(int(wait))

        return self.master_indices

    def get_8k_form(self, url):

        print ('\nPulling document from URL %s' % (BASE_8K_URL.format(url)))

        result = urllib.request.urlopen(BASE_8K_URL.format(url))
        doc = result.read()

        return doc
