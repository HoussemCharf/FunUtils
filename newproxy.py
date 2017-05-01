
# Importing needed libs
import httplib
# importing beautiful soup for parsing html tags
from bs4 import BeautifulSoup as BS
# setting up the connecting using get request
conn = httplib.HTTPSConnection("www.sslproxies.org")
conn.request("GET", "/")
# getting the response and storing it in data
response = conn.getresponse()
data = response.read()
# applying beautifulsoup for parsing
soup = BS(data,"html.parser")
# parsing the table for the needed infos
table = soup.find('tbody')
rows = table.findAll('tr')
for tr in rows:
	cols = tr.findAll('td')
	# parsing and storing data in each row
	IP_Address,Port,Code_Country,Country,Type_proxy,Google,https,LastCheck = [c.text for c in cols]
	# displaying string along with needed infos
	print IP_Address+" "+Port+" "+Country+" "+Type_proxy
