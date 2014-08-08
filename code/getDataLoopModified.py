import nltk
import os
import csv
from itertools import islice
import sys
#from ABBYY import CloudOCR
from nltk.corpus import gazetteers
import re



for aFile in os.listdir (r'C:\scraping\Isaac\txt'):
	# filename=file.rstrip(file[-4:])
	# fileDirectory=filename
	# os.chdir(r'C:\scraping\Isaac\txt')

	ProjectName=""
	placelist = gazetteers.words('countries.txt')
	currencyList=gazetteers.words('currencyList.txt')
	projectLine="name"
	# filename=filename+'.txt'
		

	#Project name

	#print " "
	projectLineFound=0
	var=0
	f1=open(r'C:\scraping\Isaac\txt\\'+aFile,'r')
	for line in f1:
		if ("project" in line or "Project" in line or "PROJECT" in line  or "PROJECTS" in line or "projects" in line or "Projects" in line or "property" in line or "Property"in line or "PROPERTY" in line or "DEPOSITS" in line):
			if "\\" in line: continue 
			projectLine=line
			projectLineFound=1
			break
	f1.close()

	projectLineTokenized=nltk.word_tokenize(projectLine)
	indexPrStWd=0;
	indexPrEnWd=0;





	for word in projectLineTokenized:
		if word=="," and projectLineTokenized.index(word)!=len(projectLineTokenized)-1:
			indexPrStWd=projectLineTokenized.index(word)
		if word=="the" or word=="THE" or word=="The" or word=="." or word=="-" or word=="For" or word=="FOR" or word=="for":
			indexPrStWd=projectLineTokenized.index(word) 
		
			
	for word in projectLineTokenized:
		if word=="Project" or word=="project" or word=="PROJECT" or word=="property" or word=="Property" or word=="PROPERTY" or word=="REPORT" or word=="Report" or word=="report" or "PROJECTS" in line or "projects" in line or "Projects" in line or "DEPOSITS":
			indexPrEnWd=projectLineTokenized.index(word)+1
		
	if indexPrEnWd>0:
		print "Project name: ",
		if indexPrStWd==0:
			for x in range(indexPrStWd, indexPrEnWd):
				print projectLineTokenized[x],
				ProjectName+=projectLineTokenized[x]+" "
		else:
			for x in range(indexPrStWd+1, indexPrEnWd):
				print projectLineTokenized[x],
				ProjectName+=projectLineTokenized[x]+" "

	else:
		for word in projectLineTokenized:
			if word=="No" or word=="Number" or word=="NO" or word=="NUMBER":
				indexPrStWd=projectLineTokenized.index(word)	
				print "Project name: ",
				for x in range(indexPrStWd+1, projectLineTokenized.index(len(projectLineTokenized)-1)):
					print projectLineTokenized[x], 
					ProjectName+=projectLineTokenized[x]+" "

	ProjectName=ProjectName.rstrip(ProjectName[-1:])	
	print " "

	#Date of project
	f = open(r'C:\scraping\Isaac\txt\\'+aFile, 'r').read()
	projectCandidates = re.findall('(?:[A-Z]\w*\s)+Project', f)

	projectDict = nltk.defaultdict(int)
	for project in projectCandidates:
	    projectDict[project] += 1

	pD = dict(zip(projectDict.values(), projectDict.keys()))
	if not pD:
		continue
	print str(max(pD))+' of '+pD[max(pD)]+"\nis the project name of report <-- "+aFile+" -->\n"

	c = csv.writer(open("Info.csv", "wb"))
	c.writerow(["Project Name",ProjectName])
	# c.writerow(["Commodity",commodity])
	# c.writerow(["Country",country])
	# c.writerow(["Currency",currency])
	# c.writerow(["Mining method",miningMethod])
	# c.writerow(["Production rate",productionRate])