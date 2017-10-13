#!/usr/bin/python
# -*- coding: <Houssem Charf> -*-
# -*- Github: <https://github.com/HoussemCharf> -*-

import sys, getopt ,os,csv

def delete_from_csv(source,result,mode,number):

	if os.path.isfile(source) and not os.path.isfile(result):
	#reading from source file
		with open(source,"rb") as s:
			rdr= csv.reader( s )
			with open(result,"wb") as res:
				if mode.upper() == "COL":
					wtr= csv.writer( res )
					wtr.writerows(
            [col for idx, col in enumerate(row)
             if idx != int(number)-1]
            for row in rdr)
				else:
					wtr= csv.writer( res )
					for i, row in enumerate(rdr):
						if i == int(number)-1:
							continue
						else:
							wtr.writerow(row)
	else:
		print 'Either <inputfile> doesnt exist in this folder or the <outputfile> exist go figure. '



def main(argv):
	inputfile = ''
	outputfile = ''
	mode=''
	number=''
	try:
		opts, args = getopt.getopt(argv,"hi:o:m:n:",["ifile=","ofile=","mode=","number="])
		if opts == []:
			print 'Add -h for help'
	except getopt.GetoptError:
		print 'code.py -i <inputfile> -o <outputfile> -m <mode> -n <number> (Desired column or row to be deleted count start from 0) \n'
		print 'PS: mode should be only "row" or "col"'
		sys.exit(2)
	for opt, arg in opts:
		if opt == '-h':
			print 'code.py -i <inputfile> -o <outputfile> -m <mode> -n <number> (Desired column or row to be deleted count start from 0) \n'
			print 'PS: mode should be only "row" or "col"'
			sys.exit()
		elif opt in ("-i", "--ifile"):
			inputfile = arg
		elif opt in ("-o", "--ofile"):
			outputfile = arg
		elif opt in ("-m","--mode"):
			if arg.upper() in ("ROW","COL"):
				mode = arg
			else:
				print 'PS: mode should be only "row" or "col"'
				sys.exit()
		elif opt in ("-n","--number"):
			number = arg
		delete_from_csv(inputfile,outputfile,mode,number)

if __name__ == "__main__":
	main(sys.argv[1:])
	print 'Thanks for using my program Houssem ;)'