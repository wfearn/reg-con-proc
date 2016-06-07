#! /usr/bin/env python3

from bs4 import BeautifulSoup
import urllib

EXHIBIT_REGEX = "(^Ex[a-z]*.{1}2\.1)"


class web_crawler():

    def __init__(self):
        pass
    
    def set_base_url(self, url):
        self.url = url

    def get_base_url(self):
        return self.url

    def access_base_url(self):

        return urllib.request.urlopen(self.url).read()

    def access_url_append(self, append):

        new_url = "%s%s" % (self.url, append)
        return urllib.request.urlopen(new_url).read()

    def pull_url_append_links(self, append):

        page_links = []

        soup = BeautifulSoup(self.access_url_append(append), 'html.parser')

        for link in soup.find_all('a'):
            page_links.append(link.get('href'))

        return page_links
#TODO: Combine testpy and webcrawler functions to pull html links, search them
# exhibit 2.1 files and pull them, IMPORTANT: Don't forget to use time.sleep()
# function between all link access points
