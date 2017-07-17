import urllib2, urllib
from bs4 import BeautifulSoup as BS
import base64

letters = raw_input()
#taking a whole word and seperating it with commas
letters = ",".join(list(letters))
#post data
mydata=[('letters', letters),('order','length'),('pos','beg'),('dic','1'),('table','dict')]
#Encoding
mydata=urllib.urlencode(mydata)
codedPath ='''aHR0cDovL3d3dy50aGV3b3JkZmluZGVyLmNvbS9zY3JhYmJsZS5waHA='''
path=base64.b64decode(codedPath)
req=urllib2.Request(path, mydata)
req.add_header("Content-type", "application/x-www-form-urlencoded")
page=urllib2.urlopen(req).read()
#title array
titles = ["h3","h6"]
# applying beautifulsoup for parsing
soup = BS(page,"html.parser")
# parsing the div with id
res = soup.find("div", { "id" : "displayresults" })
Con= res.contents[1].contents[1]
line=""
for child in Con.children:
	if (child.name in titles):
		print("------------")
		line = ""
	print child.string
