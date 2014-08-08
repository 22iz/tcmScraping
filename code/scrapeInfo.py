'''
1. requirements: os, csv, sqlalchemy, psycopg2


2. placement: this should be put into a folder containing many folders about project data within which there is a Info.csv of content


'''

import os
import csv
from sqlalchemy import *

db = create_engine('postgresql://postgres:tcm2014@localhost:5432/scrapeData')
metadata = MetaData(db)
users = Table('scrape_quality', metadata, autoload=True)

path = 'C:\scraping\Isaac\\results'
folders = os.listdir(path)
print
for aFolder in folders:
	print "current folder is: " + aFolder
	# files = os.listdir(Path + aFolder)
	try:
		open(path+'\\'+aFolder+'\\'+'Info.csv', 'rb')
	except IOError:
		print "No Info.csv in" + str(csvfile)
		continue
	else:
		with open(path+'\\'+aFolder+'\\'+'Info.csv', 'rb') as csvfile:
			spamreader = csv.reader(csvfile, delimiter=',')
			record = []
			for row in spamreader:
				# print row
				record.append(row[1])
			print record
			s = users.insert().values(project_name = record[1], commodity_name = record[2], country_name = record[3], currency = record[4], mining_method = record[5], production_rate = record[6], project_date = record[0])
			s.execute()