#!/usr/bin/env python
import time
from time import gmtime, strftime
import random

from crawler.crawler import Crawler
from file_saver.file_saver import FileSaver

EARLIEST = 1993
LATEST = 2016

Q1 = 1
Q4 = 4

BASE_MASTER_PATH = '/local/wfearn/Documents/NLPLab/lab_scripts/reg-con-proc/EdgarWebCrawler/edgar_data/master_indices/{}/QTR{}/master.txt'

URL = 4
DATE = 3
COMPANY = 1

def contains_8k(line):
    line = line.split('|')

    for word in line:
        if word == '8-K':
            return True

    return False

def main():

    c = Crawler()
    fs = FileSaver()


    for i in range(EARLIEST, LATEST + 1):
        for j in range(Q1, Q4 + 1):
            print ("\nStarting on year %s, quarter %s\n" % (str(i), str(j)))

            if i == 2016 and j == 4:
                pass

            else:
                f = open(BASE_MASTER_PATH.format(i, j), 'r')

                for line in f:
                    if contains_8k(line):
                        line = line.split('|')

                        doc = c.get_8k_form(line[URL])

                        wait = random.randint(1, 30)
                        print('Waiting %s seconds' % (str(wait)))
                        time.sleep(int(wait))
                        print('Current time is %s' % strftime('%Y-%m-%d %H:%M:%S', gmtime()))

                        if isinstance(line[DATE], str) and isinstance(line[COMPANY], str):

                            form_date = line[DATE]

                            string_array = line[COMPANY].split('/')

                            form_company = ""

                            for idx in range(len(string_array)):
                                form_company += string_array[idx]

                        else:

                            form_date = line[DATE].decode('utf-8', 'ignore')
                            form_company = line[COMPANY].decode('utf-8', 'ignore')

                        print('Found form from company %s on date of %s' % (form_company, form_date))

                        fs.save_8k_file(i, j, doc, form_date, form_company)


if __name__ == '__main__':
    main()
