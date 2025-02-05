#!/usr/bin/env python

import re

class StringProcess:
    def __init__(self):

        #Finds all strings that begin with a section number, beginning with
        #Section, or simply a number.
        self.section_match = re.compile(r'((?:\A\Section\s\d+\.[\d]+)|(?:\A[\d]+\.[\d]+\s))',
                flags=re.IGNORECASE)

        #Finds all strings that start with IN WITNESS WHEREOF, signifying end
        #of an acquisition agreement.
        self.end_match = re.compile(r'(\W*?IN\W*?WITNESS\W*?WHEREOF)', flags=re.M)

        #Finds all strings that begin with "Agreement and Plan of Merger" which
        #signifies the beginning of an acquisition agreement contract
        self.beginning_match = re.compile(r"""((?:\A\W*?Agreement\W*?and\W*?Plan\W*?of\W*?Merger)|
                                                (?:\A\W*?Acquisition\W*?Agreement)|
                                                (?:\A\W*?Plan\W*?of\W*?Reorganization)|
                                                (?:\A\W*?Stock\W*?Purchase\W*?Agreement)|
                                                (?:\A\W*?Transaction\W*?Agreement))""", flags=re.I)

    def matches_section(self, string):
        match = self.section_match.match(string)

        if match != None:
            return True
        else:
            return False

    def get_section_match(self, string):

        if self.matches_section(string):

            match = self.section_match.match(string)

            return match.group(0)
        else:
            raise Exception("InvalidInput: %s" % string)

    def matches_end(self, string):
        #match = self.end_match.match(string)
        match = self.end_match.search(string)

        if match != None:
            return True

        else:
            return False

    def get_end_match(self, string):
        if self.matches_end(string):
            match = self.end_match.match(string)

            return match.group(0)
        else:
            raise Exception("InvalidInput: %s" % string)

    def matches_beginning(self, string):
        match = self.beginning_match.match(string)

        if match != None:
            return True

        else:
            return False

    def get_beginning_match(self, string):
        if self.matches_beginning(string):
            match = self.beginning_match.match(string)

            return match.group(0)
        else:
            raise Exception("InvalidInput: %s" % string)
