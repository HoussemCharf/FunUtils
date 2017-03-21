import os
import shutil
# array of files ONLY no Folders included 
files = [f for f in os.listdir('.') if os.path.isfile(f)]
# parsing all files in the directory
for filename in files:
	#extracting the extension and the name of the file
	file,extension = os.path.splitext(filename)
	#getting rid of . in the beggining of string
	extension = extension[1:]
	# trying not to move the script to a folder
	if (not(filename=="code.py")):
		#checking if the Folder made with extension exist and creating it if it doesnt exist
		if (not(os.path.isdir(os.getcwd()+'\\'+extension.upper()))):
			os.makedirs(os.getcwd()+'\\'+extension.upper())
		# moving the file
		shutil.move(os.getcwd()+'\\'+filename,os.getcwd()+'\\'+extension.upper()+'\\'+filename)