#!/usr/bin/env python
from bs4 import BeautifulSoup
from bs4.element import NavigableString

class Parser:
    def __init__(self, html_file):
        self.soup = BeautifulSoup(open(html_file), "lxml")

    def text_gen(self):
        for item in self.soup.recursiveChildGenerator():
            if type(item) == NavigableString:
                yield item.string.encode("utf-8", "ignore")
