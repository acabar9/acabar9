import urllib
from bs4 import BeautifulSoup

htmltext = urllib.urlopen("http://www.mju.ac.kr/mbs/mjukr/jsp/board/list.jsp?boardId=10487&id=mjukr_060101000000").read()

soup = BeautifulSoup(htmltext, from_encoding="utf-8")

authors =[]

for tag in soup.select("td"):
	td = tag.findNextSibling('td').findNextSibling('td')
	authors.append(td.get_text())

for author in authors:
	print author