import time
import requests
from bs4 import BeautifulSoup
import os

from bible_list import szGAEBook

bible_title_chapter_list = szGAEBook
#
# for i in bible_title_chapter_list:
#     os.makedirs('/Users/tj/PycharmProjects/bible_crawler/bible_text/{}'.format(i[0]))
#     for j in range(2,len(i)):
#         url = "https://www.bskorea.or.kr/bible/korbibReadpage.php?version=GAE&book={}&chap={}&sec=1&cVersion=&fontSize=15px&fontWeight=normal".format(i[1],i[j])
#         # url = "https://www.bskorea.or.kr/bible/korbibReadpage.php?version=GAE&book={}&chap={}&sec=1&cVersion=&fontSize=15px&fontWeight=normal".format(bible_title_chapter_list[0][1],bible_title_chapter_list[0][i])
#         bible_page = requests.get(url)
#         bible_page_text = bible_page.text
#
#         soup = BeautifulSoup(bible_page.text, 'html.parser')
#         texts_only = soup.select("#tdBible1 > span")
#         str_texts_only = str(texts_only)
#         new_soup = BeautifulSoup(str_texts_only, 'html.parser')
#
#         for font in new_soup['size']:
#             font.decompose()
#         for div in new_soup("div"):
#             div.decompose()
#
#         file_path = '/Users/tj/PycharmProjects/bible_crawler/bible_text/{}/{}{}.text'
#         with open(file_path.format(i[0], i[0], i[j]), 'w') as fp:
#             fp.write(new_soup.text)
#
#         time.sleep(3)

url = "https://www.bskorea.or.kr/bible/korbibReadpage.php?version=GAE&book={}&chap={}&sec=1&cVersion=&fontSize=15px&fontWeight=normal".format(bible_title_chapter_list[0][1],bible_title_chapter_list[0][5])
bible_page = requests.get(url)
bible_page_text = bible_page.text

soup = BeautifulSoup(bible_page.text, 'html.parser')
texts_only = soup.select("#tdBible1 > span")
str_texts_only = str(texts_only)
new_soup = BeautifulSoup(str_texts_only, 'html.parser')

for font in new_soup('font'):
    print(font)

for div in new_soup("div"):
    print(div)
    div.decompose()