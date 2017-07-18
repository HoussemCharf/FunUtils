from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.popup import Popup
import urllib2, urllib
from bs4 import BeautifulSoup as BS
import base64

class WordUI(GridLayout):
	def __init__(self,**kwargs):
		super(WordUI, self).__init__(**kwargs)
		self.cols=2
		#adding text label
		self.add_widget(Label(text="insert the words:"))
		#adding text Input
		self.letttersinput = TextInput(multiline=False)
		self.add_widget(self.letttersinput)
		#adding the action button
		self.add_widget(Button(text="Generate", on_press=self.game , pos=(50, 100)))
	def game(self,instance):
		letters=self.letttersinput.text
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
		# applying beautifulsoup for parsing
		soup = BS(page,"html.parser")
		# parsing the div with id
		res = soup.find("div", { "id" : "displayresults" })
		Con= res.contents[1].contents[1]
		line=""
		for child in Con.children:
			line+= child.string
		popup = Popup(title="Result",content=Label(text=line))
		popup.open()



class WordGen(App):
	def build(self):
		return WordUI()
if __name__ == "__main__":
	WordGen().run()