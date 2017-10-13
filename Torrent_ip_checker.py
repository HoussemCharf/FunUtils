#!/usr/bin/python
import Tkinter
import ctypes
import tkMessageBox
import socket
import sys
import urllib2
import httplib
from bs4 import BeautifulSoup as BS
class window(Tkinter.Tk):
	Ip_text = ''
	def __init__(self,parent):
		Tkinter.Tk.__init__(self,parent)
		self.parent = parent
		self.iconbitmap(default='eye.ico') 
		self.geometry("500x100")
		self.resizable(0, 0)
		self.initialize()

	def initialize(self):
		L = Tkinter.Label(master=self,text="Targeted IP:")
		L.pack()
		self.E = Tkinter.Entry(master=self,width=50)
		self.E.pack()
		B= Tkinter.Button(master=self,text='Check IP',command=self.checkIp)
		B.pack()
		self.grid()
	def work(IP):
		conn = httplib.HTTPConnection("www.iknowwhatyoudownload.com/en/peer/?ip="+IP)
		conn.request("GET","/")
		response = conn.getresponse()
		data =response.read()
		soup = BS(data,"html.parser")
		table = soup.find('tbody')
		rows = table.findAll('tr')
		for tr in rows:
			cols = tr.findAll('td')
			Begin,End,Category,title,size=[c.text for c in cols]
			RESULT+="\n"+Begin+" "+Category+" "+title+" "+size
		toplevel = Toplevel()
		label= Label(toplevel,text=RESULT,height=0,width=100)
		label.pack()
		print RESULT

	def checkIp(self):
		IP=self.E.get()
		try:
			urllib2.urlopen('http://172.217.23.110',timeout=1)
			print IP
			self.work(IP)
		except urllib2.URLError as err:
			tkMessageBox.showerror('No Internet Connection','You have no Internet Connection')
if __name__ == "__main__":
	app = window(None)
	app.title('Torrent IP tracker - By Houssem Charfeddine v0.1')
	AppID= "Torrent Tracker By Houssem. Torrent IP Tracker.V0.1"
	ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(AppID)
	app.mainloop()
