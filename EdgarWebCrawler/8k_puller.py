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

def start_8k_puller(year, index, crawler, saver):

        for j in range(Q1, Q4 + 1):
            print ('\nStarting on year %s, quarter %s\n' % (str(year), str(j)))

            if year == 2016 and j == 4:
                pass

            else:

                try:

                    f = open(BASE_MASTER_PATH.format(year, j), 'r')

                    m = MasterIndex(f)

                    for index in m.get_8ks_from_index(index):

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

                    print ('Exception, waiting 10 minutes')

                    timeout_time = 600
                    time.sleep(timeout_time)

                    i = m.get_current_index()

                    start_8k_puller(year, i, crawler, saver)



def main():

    c = Crawler()
    fs = FileSaver()

    year = sys.argv[1]

    start_8k_puller(year, 0, c, fs)


#    for j in range(Q1, Q4 + 1):
#        print ("\nStarting on year %s, quarter %s\n" % (str(i), str(j)))
#
#        if year == 2016 and j == 4:
#            pass
#
#        else:
#            f = open(BASE_MASTER_PATH.format(year, j), 'r')
#
#            for line in f:
#                if contains_8k(line):
#                    line = line.split('|')
#
#                    doc = c.get_8k_form(line[URL])
#
#                    wait = random.randint(1, 30)
#                    print('Waiting %s seconds' % (str(wait)))
#                    time.sleep(int(wait))
#                    print('Current time is %s' % strftime('%Y-%m-%d %H:%M:%S', gmtime()))
#
#                    if isinstance(line[DATE], str) and isinstance(line[COMPANY], str):
#
#                        form_date = line[DATE]
#
#                        string_array = line[COMPANY].split('/')
#
#                        form_company = ""
#
#                        for idx in range(len(string_array)):
#                            form_company += string_array[idx]
#
#                    else:
#
#                        form_date = line[DATE].decode('utf-8', 'ignore')
#                        form_company = line[COMPANY].decode('utf-8', 'ignore')
#
#                    print('Found form from company %s on date of %s' % (form_company, form_date))
#
#                    fs.save_8k_file(i, j, doc, form_date, form_company)
#

if __name__ == '__main__':
    main()
