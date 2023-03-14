import time
import requests
from bs4 import BeautifulSoup
import os

from bible_list import szGAEBook

bible_title_chapter_list = szGAEBook

for i in bible_title_chapter_list[0:40]:
    os.makedirs('/Users/tj/PycharmProjects/bible_crawler/bible_text/{}. {}'.format(i[0],i[1]))
    for j in range(3,len(i)):
        url = "https://www.bskorea.or.kr/bible/korbibReadpage.php?version=GAE&book={}&chap={}&sec=1&cVersion=&fontSize=15px&fontWeight=normal".format(i[2],i[j])
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

        #go through pre_result line by line_numb
        for line_numb in range(0,len(pre_result)):
            #go through chacter k in the line
            position = []
            for k in range(0,len(pre_result[line_numb])-2):
                if (pre_result[line_numb][k] == ',') and (pre_result[line_numb][k+2].isnumeric()):
                    position.append(k)
                    continue
            # print(position)

            temp_list = list(pre_result[line_numb])

            for p in range(0,len(position)):
                temp_list.pop(position[p])
                temp_list.insert(position[p], '\n')

            temp_string = ''.join(temp_list)
            splitted = temp_string.split('\n ')

            for split in splitted:
                result.append(split)

        # print(result)

        new_result = [i for i in result if not i.isascii()]
        # print(new_result)

        final_result = []
        for k in new_result:
            final_result.append(k.lstrip('[').rstrip(']'))
        # print(final_result)

        file_path = '/Users/tj/PycharmProjects/bible_crawler/bible_text/{}. {}/{}{}.text'
        with open(file_path.format(i[0], i[1], i[1], i[j]), 'w') as fp:
            fp.write('\n'.join(final_result))

        time.sleep(3)

