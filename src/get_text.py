#import bs4
import urllib.request
from bs4 import BeautifulSoup
import gzip
import logging

log = logging.getLogger("get_text.py")
log.setLevel(level=logging.INFO)


def from_wikipedia(article :str):
   wikipedia_url = 'https://de.wikipedia.org/wiki/'
   url = wikipedia_url+article
   return get_text(url)

def from_heute(id="100242707"):
   url = "https://www.heute.at/s/"+id
   log.debug(url)
   return get_text(url)

def get_text(url):
   hdr = { 
      'Accept-Encoding': 'gzip',
      'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)',
      'Accept': 'application/json',
      }


   req = urllib.request.Request(url, data=None, headers=hdr)

   ret = []

   with urllib.request.urlopen(req) as f:
      j = gzip.decompress(f.read()).decode('utf-8')
      log.debug(f"response: {f}: {dir(f)}")
      log.debug(f"response headers: {f.headers}")
      soup = BeautifulSoup(j, "html.parser")
      log.info(soup.title)
      ret = soup.find_all('p')
      for i, p in enumerate(ret):
         log.debug(f'{i} --- {p.text[:30]}')

   return ret