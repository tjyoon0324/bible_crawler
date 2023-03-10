import requests

bible_page = requests.get("https://www.bskorea.or.kr/bible/korbibReadpage.php?version=GAE&book=gen&chap=60&sec=1&cVersion=&fontSize=15px&fontWeight=normal").text

print(bible_page)