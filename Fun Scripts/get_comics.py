import sys
import requests
import os

n = int(sys.argv[1])
if len(sys.argv) < 3:
	comicsDirectory = os.getcwd() + "/"
else:
	comicsDirectory = sys.argv[2]
url = "https://xkcd.com/"

response = requests.get(url)
data = response.text
idx = data.find(url)
issueNo = int(data[idx + 17: idx + 21])

for i in range (n, 0, -1):
	if (issueNo == 0):
		break
	completeUrl = url + str(issueNo)
	response = requests.get(completeUrl)
	data = response.text
	print ("Complete Url is :", completeUrl)
	imgIdx = data.find("https://imgs.xkcd.com/comics/")
	idx = data.find(".png", imgIdx)
	imgName = data[imgIdx + 29: idx + 4]
	imgUrl = data[imgIdx: idx + 4]
	print ("Downloading xkcd comic ", issueNo, "with url: ", imgUrl)
	response = requests.get(imgUrl)
	ofile = open(comicsDirectory + imgName,"wb")
	for chunk in response.iter_content(100000):
		ofile.write(chunk)
	ofile.close()
	issueNo -= 1