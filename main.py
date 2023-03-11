import requests
from bs4 import BeautifulSoup

from bible_list import *

bible_page = requests.get("https://www.bskorea.or.kr/bible/korbibReadpage.php?version=GAE&book=gen&chap=1&sec=1&cVersion=&fontSize=15px&fontWeight=normal")
bible_page_text = bible_page.text

soup = BeautifulSoup(bible_page.text, 'html.parser')

option_tags = soup.select(".searchList li:nth-of-type(2) > ul > li:nth-of-type(2) select option")

print(bible_page_text)
# print(option_tags)