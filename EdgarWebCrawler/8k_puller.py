#!/usr/bin/env python
import time
from time import gmtime, strftime
import random

import sys

from crawler.crawler import Crawler
from file_saver.file_saver import FileSaver
from master_index.master_index import MasterIndex

Q1 = 1
Q4 = 4

BASE_MASTER_PATH = '/net/perplexity/wfearn/Documents/NLPLab/lab_scripts/reg-con-proc/EdgarWebCrawler/edgar_data/master_indices/{}/QTR{}/master.txt'

COMPANY = 1

MASTER_URL_POS = 1
MASTER_COMPANY_POS = 2
MASTER_DATE_POS = 0

def start_8k_puller(year, quarter, index, crawler, saver):

        for j in range(quarter, Q4 + 1):
            quarter = j

            print ('\nStarting on year %s, quarter %s, index %s \n' % (str(year), str(j), str(index)))

            if year == 2016 and j == 4:
                pass

            else:

                try:

                    f = open(BASE_MASTER_PATH.format(year, j), 'r')

                    m = MasterIndex(f)

                    for index in m.get_8ks_from_index(index):
                        print("Now on index %s" % (str(index)))

                        doc = crawler.get_8k_form(index[MASTER_URL_POS])

                        wait = random.randint(1, 15)
                        time.sleep(int(wait))
                        print('Current time is %s' % strftime('%Y-%m-%d %H:%M:%S', gmtime()))

                        #Some URLs have '/' character that needs to be removed in
                        #order to save the file properly
                        if isinstance(index[MASTER_DATE_POS], str) and isinstance(index[MASTER_COMPANY_POS], str):

                            form_date = index[MASTER_DATE_POS]

                            string_array = index[MASTER_COMPANY_POS].split('/')

                            form_company = ""

                            for idx in range(len(string_array)):
                                form_company += string_array[idx]

                        else:

                            form_date = index[MASTER_DATE_POS].decode('utf-8', 'ignore')
                            form_company = index[MASTER_COMPANY_POS].decode('utf-8', 'ignore')

                        print ('Found form from company %s on date of %s' % (form_company, form_date))

                        saver.save_8k_file(year, j, doc, form_date, form_company)

                except:

                    print ('Exception, waiting 20 minutes')

                    timeout_time = 1200
                    time.sleep(timeout_time)

                    i = m.get_current_index()

                    return (year, quarter, i)

        return None



def main():

    c = Crawler()
    fs = FileSaver()

    year = sys.argv[1]

    quarter = sys.argv[2]

    index = sys.argv[3]

    result = (year, quarter, index)

    while result != None:

        result = start_8k_puller(result[0], int(result[1]), int(result[2]), c, fs)


if __name__ == '__main__':
    main()
