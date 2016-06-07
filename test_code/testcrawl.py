from bs4 import BeautifulSoup


TEST_FILE_PATH = "/aml/home/wfearn/Downloads/WebCrawlerHTMLTestDocs/Search_Historical_SEC_Edgar_Archives.html"


soup = BeautifulSoup(open(TEST_FILE_PATH), "html.parser")
between_headers = False

for link in soup.find_all('a'):
    print("Checking link with string %s" % link.string)
    if between_headers:
        print("Between next headers, printing html links")
        if str(link.string) == "[html]":
            print(link.string)
            print(link.get("href"))
    if str(link.string) == "[NEXT]":
        print("link string matches next, changing boolean")
        if between_headers:
            between_headers = False 
        else:
            between_headers = True 
