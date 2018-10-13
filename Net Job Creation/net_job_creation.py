from censuspy import bds
import csv

census_key = '61452b999f5349ac5ac1951f55506efb2f0ad72d'
bds = bds.bds(api_key=census_key, geo='us')

firm_size_range = [
	'a', 'b', 'c', 'd', 'e',
	'f', 'h', 'i', 'j', 'k',
	'l'
]

year_range = [
	1980, 1981, 1982, 1983, 1984,
	1985, 1986, 1987, 1988, 1989,
	1990, 1991, 1992, 1993, 1994,
	1995, 1996, 1997, 1998, 1999,
	2000, 2001, 2002, 2003, 2004,
	2005, 2006, 2007, 2008, 2009,
	2010, 2011, 2012, 2013, 2014
]

with open('result_set.csv', 'w', newline='') as csvfile:
	pen = csv.writer(csvfile, delimiter=',')
	pen.writerow(['year', 'firm_size', 'net_job_creation'])

	for year in year_range:
		for firm_size in firm_size_range:
			metric = bds.get(metric='net_job_creation', fsize=firm_size, time=year)
			row = [year, firm_size, metric]
			pen.writerow(row)

