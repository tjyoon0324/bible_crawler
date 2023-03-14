import time
import requests
from bs4 import BeautifulSoup
import os

from bible_list import szGAEBook

bible_title_chapter_list = szGAEBook

for i in bible_title_chapter_list:
    os.makedirs('/Users/tj/PycharmProjects/bible_crawler/bible_text/{}'.format(i[0]))
    for j in range(2,len(i)):
        url = "https://www.bskorea.or.kr/bible/korbibReadpage.php?version=GAE&book={}&chap={}&sec=1&cVersion=&fontSize=15px&fontWeight=normal".format(i[1],i[j])
        # url = "https://www.bskorea.or.kr/bible/korbibReadpage.php?version=GAE&book={}&chap={}&sec=1&cVersion=&fontSize=15px&fontWeight=normal".format(bible_title_chapter_list[0][1],bible_title_chapter_list[0][i])
        bible_page = requests.get(url)
        bible_page_text = bible_page.text

        soup = BeautifulSoup(bible_page.text, 'html.parser')
        texts_only = soup.select("#tdBible1 > span")
        str_texts_only = str(texts_only)
        new_soup = BeautifulSoup(str_texts_only, 'html.parser')

        for a in new_soup('a'):
            a.decompose()

        for div in new_soup("div"):
            div.decompose()

        pre_result = new_soup.text.replace('   ', '. ').replace('\n\n',' ').replace(' , ', '\n').split('\n')
        # print(pre_result)

        result = []

        for n in range(0,len(pre_result)):
            for k in range(0,len(pre_result[n])-2):
                if (pre_result[n][k] == ',') and (pre_result[n][k+2].isnumeric()):
                    temp_list = list(pre_result[n])
                    temp_list.pop(k)
                    temp_list.insert(k,'\n')
                    temp_string = ''.join(temp_list)
                    splitted = temp_string.split('\n ')
                    print(splitted)
                    result.append(splitted[0])
                    result.append(splitted[1])
                    continue
                else:
                    result.append(pre_result[n])
                    continue

        # print(result)

        new_result = [i for i in result if not i.isascii()]
        # print(new_result)

        final_result = []
        for k in new_result:
            # print(k)
            final_result.append(k.lstrip('[').rstrip(']'))
            # print(final_result)

        file_path = '/Users/tj/PycharmProjects/bible_crawler/bible_text/{}/{}{}.text'
        with open(file_path.format(i[0], i[0], i[j]), 'w') as fp:
            fp.write('\n'.join(final_result))

        time.sleep(3)

