#!/usr/bin/env python

import requests
import sys
import re

class WebCrawler:

    def __init__(self):
        if sys.argv[1].startswith("http://") or sys.argv[1].startswith("https://"):
            self.url = sys.argv[1]
        else:
            self.url = "https://" + sys.argv[1]

    def request_resource(self):
        r = requests.get(self.url)
        urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', r.text)
        return urls

def main():
    
    crawl = WebCrawler()
    new_data = crawl.request_resource()
    
    if new_data is not None:
        for url in new_data:
            print(url)

if __name__ == '__main__':
    main()

