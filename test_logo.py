#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 20 15:08:39 2018

@author: buckz
"""

try:
    from urlparse import urljoin
except ImportError:
    from urllib.parse import urljoin

import requests
import os
from bs4 import BeautifulSoup

#filev4 = 'dfv4.xls'
#df = pd.read_excel(filev4)

def extract_values(colname):
    a = []
    for i in df[colname]:
        if str(i) != 'nan': 
            a.append(i)
        else:
            pass
    return a

#pageweb = extract_values('PageWeb')



class Scraper:
    def __init__(self):
        self.visited = set()
        self.session = requests.Session()
        self.session.headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.109 Safari/537.36"}

        requests.packages.urllib3.disable_warnings()  # turn off SSL warnings

    def visit_url(self, url, level):
        print(url)
        #if url in self.visited:
        #    return

        #self.visited.add(url)

        content = self.session.get(url, verify=False).content
        soup = BeautifulSoup(content, "lxml")

        for img in soup.select("img[src]"):
            image_url = img["src"]
            if not image_url.startswith(("data:image", "javascript")):
                self.download_image(urljoin(url, image_url))

        if level > 0:
            for link in soup.select("a[href]"):
                self.visit_url(urljoin(url, link["href"]), level - 1)

    def download_image(self, image_url):
        local_filename = image_url.split('/')[-1].split("?")[0]

        r = self.session.get(image_url, stream=True, verify=False)
        with open(local_filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=1024):
                f.write(chunk)

if __name__ == '__main__':
    scraper = Scraper()
    scraper.visit_url("https://logo.clearbit.com/http://www.agrosupdijon.fr/", 1)

    #for lien in pageweb:
     #   path = '/home/buckz/Data/img'
      #  lien2 = str(lien).replace('/', '_')
       # os.mkdir(path+'/' + lien2)
        #os.chdir(path+'/' + lien2)
        #os.chdir(path)