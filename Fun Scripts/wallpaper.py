import urllib2
import json
import os
import os.path
import datetime
import time
from os.path import expanduser

def getName(urlname):
	i = urlname.find("_EN")
	i -= 1
	s1 = ""
	while (urlname[i] != '/') :
		s1 += urlname[i]
		i -= 1
	s1 = s1[::-1] + '.jpg'
	return s1

market = "en-US"
resolution = "1920x1080"
wallpaperDirectory = expanduser("~")+'/Pictures/Wallpapers/'

i = 1
while (i == 1) :
	try :
		urllib2.urlopen("http://google.com")
	except urllib2.URLError:
		time.sleep(5)
		print("Hello")
	else :
		i = 0

response = urllib2.urlopen("http://www.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1&mkt=" + market)
obj = json.load(response)
url = obj['images'][0]['urlbase']

wallpaperName = getName(url)
print("The name of wallpaper is %s" %(wallpaperName))

url = 'http://www.bing.com' + url + '_' + resolution + '.jpg'
print(url)

if not os.path.exists(wallpaperDirectory) :
	os.makedirs(wallpaperDirectory)
path = wallpaperDirectory + wallpaperName

print("Downloading Bing Wallpaper to %s" %(path))
f = open(path,"w")
bingpic = urllib2.urlopen(url)
f.write(bingpic.read())
s1 = "/usr/bin/gsettings set org.gnome.desktop.background picture-uri file:///home/fbd/Pictures/Wallpapers/" + wallpaperName
os.system(s1)
