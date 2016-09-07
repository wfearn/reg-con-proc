#!/usr/bin/env python
from bs4 import BeautifulSoup
from bs4.element import NavigableString
from bs4.element import Tag

class Parser:
    def __init__(self, html_file):
        self.soup = BeautifulSoup(open(html_file), "lxml")

    def text_gen(self):
        for item in self.soup.recursiveChildGenerator():
            if item.string != None:

                s = item.string.encode("utf-8", "ignore")

                #Many contracts have lines that are simply one whitespace character, hope to modify to include empty lines
                if s != " ":
                    yield item.string.encode("utf-8", "ignore")
