# BeautifulSoup and requests are required.
# pip install beautifulsoup4
# pip install requests

from bs4 import BeautifulSoup
import re

def get_soup_by_url(url, parser=None):
	import requests
	r = requests.get(url)
	html_doc = r.content
	return BeautifulSoup(html_doc, parser)

def get_soup_by_path(path, parser=None):
	if not isinstance(path, str):
		path = str(path)

	print('parser:', parser)

	with open(path) as f:
		data = f.read()
		return BeautifulSoup(data, parser)


# The html tag Reg-ex, instead of'<.*>'
html_tag_pattern =re.compile('<[^>]*>')


# ================ Online HTML ======================
# # url = "http://www.ielts-mentor.com/reading-sample/academic-reading/26-ielts-academic-reading-sample-1-population-viability-analysis"
# # Python doc PEP-0008
# url = 'https://www.python.org/dev/peps/pep-0008/'
# soup = get_soup_by_url(url)

# ================ Local  HTML ======================
# path = "/home/shawn/Dropbox/src/try_memo/2016/fenci/ielts_mentor.html"

path = "/Users/shawn/Dropbox/src/try_memo/2016/fenci/ielts_mentor.html"
soup = get_soup_by_path(path, 'lxml')

# soup = get_soup_by_path(path)


# ================ Doc manipulation =================
data = soup.find_all('p',{'align':'justify'})
l = [d.text for d in data]
print(l[:-1])




# print(soup.prettify())
# raw_data = soup.find_all('p', {'align': 'justify'})[:3]

# print(raw_data)
# for data in raw_data:
# 	print(data.index, data.text.strip())

# Alice example
# html_doc = """
# <html><head><title>The Dormouse's story</title></head>
# <body>
# <p class="title"><b>The Dormouse's story</b></p>

# <p class="story">Once upon a time there were three little sisters; and their names were
# <a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
# <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
# <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
# and they lived at the bottom of a well.</p>

# <p class="story">...</p>
# """
# soup = BeautifulSoup(html_doc)
# soup.head.getText()
# soup.head.get_text()