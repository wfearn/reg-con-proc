#!/usr/bin/env python

from file.file import File
from file.file_manager import FileManager
from htmlparse.parser import Parser
from regex.string_process import StringProcess

import collections
import time

TEST_PATH = "/local/wfearn/Documents/NLPLab/lab_scripts/reg-con-proc/test_code/test_data/"

DATA_PATH = "/local/wfearn/Documents/NLPLab/lab_scripts/WebCrawler/data_dump/"
TEST_OUTPUT = "/local/wfearn/Documents/NLPLab/lab_scripts/reg-con-proc/test_code/test_output/"
FILE_EXT = "txt"

def main():

    time_begin = time.time()

    fm = FileManager(DATA_PATH, FILE_EXT, TEST_OUTPUT)

    file_dictionary = []
    file_dictionary.append([])

    index = 0

    beginning_found = False
    end_found = False

    sp = StringProcess()

    number_of_contracts = 0

    for f in fm.file_gen():
        print "\nProcessing file %s" % f
        p = Parser(f)

        for string in p.text_gen():
            beginning_match = sp.matches_beginning(string)

            if beginning_match or beginning_found:
                if beginning_found == False:

                    print "\nBeginning found, %s" % string
                    beginning_found = True
                    end_found = False

                file_dictionary[index].append(string)


            if sp.matches_end(string) and beginning_found:
                print "\nEnd found %s" % string

                print "\nWhole contract found"
                number_of_contracts += 1
                file_dictionary.append([])
                index += 1

                beginning_found = False
                end_found = True

        if beginning_found == False and end_found == True:

            end_found = False

        elif beginning_found == True and end_found == False:
            print "\nCorrecting error in file_dictionary"

            del file_dictionary[index]
            file_dictionary.append([])

            beginning_found = False

    del file_dictionary[index]

    failures = len(file_dictionary) - number_of_contracts

    fm.save_contract_files(file_dictionary)

    time_end = time.time()

    t = float(time_end - time_begin)

    hours = int(t / 3600)
    minutes = int(t / 60) % 60
    seconds = t % 60

    print "\nDone, saving files, number of contracts found is %s" % number_of_contracts
    print "Number of failures is %s" % failures

    print "Total time: %s hours, %s minutes, and %s seconds" % (hours, minutes, seconds)

if __name__ == "__main__":
    main()
