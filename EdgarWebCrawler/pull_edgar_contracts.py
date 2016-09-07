#!/usr/bin/env python
from crawler.crawler import Crawler
from file_saver.file_saver import FileSaver

def main():

    c = Crawler()

    indices = c.get_master_indices()

    fs = FileSaver()
    fs.save_files(indices)

if __name__ == '__main__':
    main()
