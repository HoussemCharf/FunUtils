import os
import json
import sys
import datetime
from subprocess import call

args = ""
if len(sys.argv) < 2:
	print("Provide an argument: backup, push or restore")
else:
	args = sys.argv[1]

if (args == "backup"):
	data = json.load(open('list.json'))
	for itr in data:
		command = "cp " + itr[0] + " " + itr[1]
		try:
			call(command, shell = True)
		except OSError:
			print("OS Error")

elif (args == "push"):
	try:
		call("git add .", shell = True)
		call("git commit -m \"Backup at time: " + datetime.datetime.now().strftime("%y-%m-%d, %H:%M") + "\"", shell = True)
		call("git push origin master", shell = True)
	except OSError:
		print("OS Error")

elif (args == "restore"):
	data = json.load(open('list.json'))
	try:
		call("git fetch --all", shell = True)
		call("git pull origin master", shell = True)
	except OSError:
		print("OS Error")
	for itr in data:
		command = "cp " + itr[1] + " " + itr[0]
		try:
			call(command, shell = True)
		except OSError:
			print("OS Error")