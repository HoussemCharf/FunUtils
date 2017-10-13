import os, sys
# extension to which all files gonna be changed to
Ext =".png"
# parsing all files in the folder
for filename in os.listdir(os.path.dirname(os.path.abspath(__file__))):
	#splitting the extension and filename
  base_file, ext = os.path.splitext(filename)
  #renaming and adding the extension desired 
  os.rename(filename, base_file + Ext)