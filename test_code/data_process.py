from bs4 import BeautifulSoup
from bs4 import UnicodeDammit
from ctypes import cdll
import re
import os, glob
import collections


NEWFILE = "/local/wfearn/Documents/NLPLab/lab_scripts/WebCrawler/usable_data/{}_{}.txt"
FILEHEADER = '''number: {}
title: {}
author_name: Grant
month: Febuary
president_name: Grant
year: 2016
day: 25

'''

acquisition_agreement_counter = 0

counter = 1

section_match = re.compile(r'((?:\A\Section\s\d+\.[\d]+)|(?:\A[\d]+\.[\d]+\s))',
        flags=re.IGNORECASE)

end_match = re.compile(r'(\bIN\b\s\bWITNESS\b\s\bWHEREOF\b)')
beginning_of_agreement = re.compile(r'((?:\AAgreement\sand\sPlan\sof\sMerger))')

def html_file_gen():
    os.chdir("/local/wfearn/Documents/NLPLab/lab_scripts/WebCrawler/data_dump/")
    for file in glob.glob("*.txt"):
        yield(file)

def write_dictionary_to_file(section_dictionary, filename):

   #print("Now writing documents to file...\n")

   fileshorthand = os.path.splitext(filename)[0] 
   global counter

   for key in section_dictionary:
       #print("opening key %s"%(key))

       new_file_name = NEWFILE.format(fileshorthand, key).replace("\s", "_")
       new_file = open(new_file_name, "w")

       new_header_title = "{} {}".format(fileshorthand, key).replace("_", " ")
       file_header = FILEHEADER.format(str(counter), new_header_title)

       counter += 1

       new_file.write(file_header)

       for value in section_dictionary[key]:
           #print("writing to file value %s"%(value))
           new_file.write(value)

def section_puller(filename):

    global acquisition_agreement_counter

    fileshorthand = os.path.splitext(filename)[0]

    #print("Pulling sections inside of document %s\n" % filename)

    counter = 1

    soup = BeautifulSoup(open(filename, errors="ignore"), "lxml")

    file_sections = collections.defaultdict(list) 
    current_section_title = ""

    in_acquisition_agreement = False

    for text in soup.find_all('p'):
        for string in text.strings:

            beginning = beginning_of_agreement.match(string)

            if beginning:
                #print("match found in %s" % string)
                acquisition_agreement_counter += 1

                print("Acquisition agreement #%s found" %(str(acquisition_agreement_counter)))

                in_acquisition_agreement = True

            if in_acquisition_agreement:

              #print("Inspecting string: %s\n"%(string))
              results = section_match.match(string)
              final = end_match.match(string)

              if final is None:
                    if results:
                        #print("match found in %s" % string)
                        current_section_title = results.group(1)
                        #print("Match! %s"%current_section_title)
                        file_sections[current_section_title].append(string)

                    elif current_section_title != "":

                        file_sections[current_section_title].append(string)
              else:
                   #print("End found, %s"%string)
                   in_acquisition_agreement = False
                   current_section_title = ""

    write_dictionary_to_file(file_sections, filename)


for file in html_file_gen():
    #print("Starting section puller...\n")
    section_puller(file)

#section_puller("/local/wfearn/Documents/NLPLab/lab_scripts/WebCrawler/data_dump/0001019056-14-000764.txt")
