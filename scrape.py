import nltk
import os
import csv
from itertools import islice
import sys
#from ABBYY import CloudOCR
from nltk.corpus import gazetteers
import re
from shutil import move, copy


scrapingFileNames = r'C:\scraping\Isaac\toBeScraped\namesOfScrapingFiles\\'
scrapingDir = r'C:\scraping\Isaac\toBeScraped\csvTxts\\'
os.chdir(scrapingDir)
for file in os.listdir (scrapingFileNames):
	filename = file[:-4]
	fileDirectory=filename

	ProjectName=""
	placelist = gazetteers.words('countries.txt')
	currencyList=gazetteers.words('currencyList.txt')
	# projectLine="name"
	filename=filename+'.txt'

#name of project
	print filename
	f = open(filename, 'r').read()
	projectCandidates = re.findall('(?:[A-Z][\w-]*\s)+Project', f)
	ProjectName = ''
	projectDict = nltk.defaultdict(int)
	for project in projectCandidates:
		if project == 'The Project' or project == 'Mineral Project':
			continue
		else:
		    projectDict[project] += 1
		    if len(ProjectName) == 0:
		    	ProjectName = project
		    else:
		    	if projectDict[project] > projectDict[ProjectName]:
		    		ProjectName = project
	    # print project
	if len(ProjectName) == 0:
		ProjectName = 'noName -- ' + filename[:-4]
	ProjectName = re.sub('\n+', ' ', ProjectName)
	print 'project name is ::::::::::::::::::::::: ' + ProjectName + '\n\n'

#commodity of project
	f = open(filename, 'r').read()
	commodities = 'Gold|Silver|Platinum|Iridium|Osmium|Palladium|Rhodium|Ruthenium|Bauxite|Lead|Chromium|Cobalt|Lithium|Magnesium|Manganese|Nickel|Nickel|Tin|Tungsten|Zinc|Phosphate|Copper|Molybdenum|Uranium|Iron|Iron|Iron|Coal|Coal|Aluminium|Alunite|Andalusite|Anthracite|Antimony|Arsenic|Asbestos|Barite|Barium|Barium-Barite|Beryllium|Bismuth|Boron-Borates|Bromine|Cadmium|Calcium Carbonate|Cerium|Cesium|Chalk|Chlorine|Chlorite|Chromium oxide|Copper Oxide|Copper Sulfide|Corundum|Diatomite|Dolomite|Dysprosium|Dysprosium oxide|Emery|Erbium|Europium|Feldspar|Ferrochrome|Ferromanganese|Ferrosilicon|Fluorine-Fluorite|Fluorite|Gallium|Gallium oxide|Garnet|Germanium|Gardolinium|Gilsonite|Granite|Graphite|Gypsum|Gypsum-Anhydrite|Hafnium|Hafnium oxide|Halite|High Calcium|Holmium|Ilmenite|Indium|Iodine|Jade|Jasper|Kaolin|Kyanite|Lanthanum|Leucoxene|Lignite|Lime|Limestone|Limestone-Limesand|Limonite|Lithium oxide|Lutetium|Magnesia|Magnesite|Magnetite|Hematite|Marble|Mercury|Mica|Monazite|Montmorillonite|Neodymium|Nickel|Niobium|Niobium pentoxide|Peat|Perlite|Phosphorus|Potassium|Potassium sulphate|Praseodymium|Pyrophyllite|Quartzite|Radium|Rare earth oxides|Rare Earth Elements|Total Rare Earth Oxide|Total Rare Earth Element|Rhenium|Rubidium|Sandstone|Saponite|Scandium|Selenium|Siderite|Silica|Sillimanite|Sodium|Sodium Carbonate|Sodium Sulfate|Samarium|Spodumene|Staurolite|Strontium|Sulfur|Sulfur-Pyrite|Tantalum pentoxide|Terbium|Tellurium|Thallium|Thorium|Titanium|Titanium dioxide|Thulium|Tungsten trioxide|Uranium oxide|Vanadium|Vanadium pentoxide|Wollastonite|Xenotime|Yttrium oxide|Yttrium|Ytterbium|Zeolites|Zircon|Zirconia|Zirconium|Platinum Group Metals|Platinum Group Elements|Gold Eq|Silver Eq|Zinc Eq|Copper Eq|Molybdenum Eq|Iron|Pig Iron|Iron Pellets|DSO|BFO|Coal'
	commodCandidates = re.findall(commodities, f)
	commodity = ''
	commodDict = nltk.defaultdict(int)

	for cd in commodCandidates:
	    commodDict[cd] += 1
	    if len(commodity) == 0:
	    	commodity = cd
	    else:
	    	if commodDict[cd] > commodDict[commodity]:
	    		commodity = cd
	if len(commodity) == 0:
		commodity = 'noCommodity'
	# for cds in commodDict:
	# 	print cds + ': ' + str(commodDict[cds])
	# print 'commodity is ::::::::::::::::::::::: ' + commodity + ' with ' + str(commodDict[commodity])

#country
	country="NULL"
	f2=open(filename,'rU')
	for line1 in f2:
		#print line1
		line1 = line1.decode('utf-8')
		for placeName in placelist:
			if (placeName in line1) and ("project" in line1 or "PROJECT" in line1 or "Project" in line1):
				country=placeName
				break
				
	f2.close()
	# print ("Country: "+country)

	currency = 'NULL'
	f5=open(filename,'rU')
	for line4 in f5:
		#print line1
		line4 = line4.decode('utf-8')
		if ("EUR" in line4 or "Euro" in line4 or 'U+20A0' in line4) and ("cost" in line4 or "COST" in line4 or "Cost" in line4):
			currency="EUR"
			break
		if "$" in line4:
			currency="USD"
			break
	f5.close()
	# print ("Currency: "+currency)




	if currency=="NULL":
		f4=open(filename,'rU')
		for line3 in f4:
			#print line1
			line3 = line3.decode('utf-8')
			for currencyName in currencyList:
				if (currencyName[:3] in line3) and ("cost" in line3 or "COST" in line3 or "Cost" in line3):
					currency=currencyName[:3]
					break
					break
		f4.close()
		# print ("Currency: "+currency)



	#f=open(r'C:\Python27\Scripts\1. PEA\2. Silver\SVBL_SierraMojada_PEA (1).txt','rU')
	#for line in f:
	#	if "report" in line:
	#		if "PEA" in line:
	#			if "This" in line or "this" in line:
	#				print line
	#f.close()



	#f=open(r'C:\Python27\Scripts\1. PEA\2. Silver\SVBL_SierraMojada_PEA (1).txt','rU')
	#raw=f.read()
	#tokens = nltk.word_tokenize(raw)
	#text = nltk.Text(tokens)
	#f.close()
	#text.concordance('project')

	#print("The word project appeared", counter, " times")

	#set the dictionary
	dict={}
	dict['gold']='ORE'
	#print(dict['gold'])
	#print(list(dict))





	#############################
	#############################
	###### getData2 #############





	totalrows=0
	counter=0;
	counter2=0;
	
	fileDirectory=fileDirectory+'.csv'


	tableList=[]
	tableBorderList=[]
	tableStartList=[]
	tableEndList=[]
	tableTitleList=[]
	counter0=0
	opexTableList=[]
	opexStartList=[]
	opexEndList=[]
	opexCounter=0
	capexTableList=[]
	capexStartList=[]
	capexEndList=[]
	capexCounter=0
	resourceTableList=[]
	resourceStartList=[]
	resourceEndList=[]
	resourceCounter=0
	reserveTableList=[]
	reserveStartList=[]
	reserveEndList=[]
	reserveCounter=0
	discrTableList=[]
	discrStartList=[]
	discrEndList=[]
	discrCounter=0
	comprTableList=[]
	comprStartList=[]
	comprEndList=[]
	comprCounter=0
	NPVTableList=[]
	NPVStartList=[]
	NPVEndList=[]
	NPVCounter=0


	with open(fileDirectory, mode='r') as f0:
		reader0 = csv.reader(f0)
		for row0 in islice(reader0, 0, None):
			totalrows += 1
			counter0=counter0+1
			if 1<len(row0):
				#print row0
				tableBorderList.append(counter0)
				

	#print "TOTAL ROWS: ", totalrows

	counterBeginTable=0
	numOfTables=1

	#print "TABLEBORDERLIST"
	#for n in range(0, len(tableBorderList)-1):
	#	print tableBorderList[n]

	if len(tableBorderList)!=0:
		tableStartList.append(tableBorderList[0])

	for n in range(1, len(tableBorderList)):
		if tableBorderList[n]!=tableBorderList[n-1]+1:
			tableStartList.append(tableBorderList[n])
			try:
				tableBorderList[n-1]
			except IndexError:
				print 'tableBorderList[n-1] list index out of range'
				continue
			else:
				tableEndList.append(tableBorderList[n-1])
	try:
		tableBorderList[len(tableBorderList)-1]
	except IndexError:
		print 'tableBorderList[len(tableBorderList)-1] list index out of range'
		continue
	else:
		tableEndList.append(tableBorderList[len(tableBorderList)-1])

	#print ("Start list has size: ", len(tableStartList))
	#print ("End list has size: ", len(tableEndList))

	#for n in range(0, len(tableStartList)):
	#	print (tableStartList[n], " ", tableEndList[n])


	with open(fileDirectory, mode='r') as f01:
		reader01 = csv.reader(f01)
		for i, line in enumerate(reader01):
			for n in range(0, len(tableStartList)):
				if i==tableStartList[n]-2:
	#				print "*********HEY HERE*********"
	#				print i,"   ",tableStartList[n]-2
	#				print line
					tableTitleList.append(line)
				elif i>tableStartList[len(tableStartList)-1]:
					break


	#for n in range(0, len(tableStartList)-1):
	#	print (tableStartList[n], " ", tableEndList[n])



	#print "LET'S SEE"
	#for n in range(0, len(tableTitleList)):
	#	print tableTitleList[n]
	counterwords=0
	#print "THE FILTER IS HERE"
	indexOfWrongTableNames=[]
	listRemoveIndex=[] 
	for n in range(0, len(tableTitleList)):
		for word in tableTitleList[n]:
			if "Table" not in word and "table" not in word and "TABLE" not in word:
				listRemoveIndex.append(n)
				counterwords+=1
	#			print "I FOUND IT", counterwords, n

	#print("THESE ARE THE INDICES TO BE REMOVED")
	#for n in range(0, len(listRemoveIndex)):
	#	print tableStartList[listRemoveIndex[n]]


	reverseStart=0
	reverseEnd=0
	reverseCounter=0
	for n in range(0,len(listRemoveIndex)):
		with open(fileDirectory, mode='r') as f001:
			reverseReader=reversed(list(csv.reader(f001)))
			reverseStart=totalrows-tableStartList[listRemoveIndex[n]]
			reverseEnd=reverseStart+3
			for row in islice(reverseReader, reverseStart,reverseEnd):
				try:
					row[0]
				except IndexError:
					print 'no row[0]'
					continue
				else:
		 			if 'Table' in row[0] or 'TABLE' in row[0]:
		 				#print row[0]
		 				indexOfWrongTableNames.append(n)
									
	#print "WRONG TABLE NAMES"
	#for m in range(0, len(indexOfWrongTableNames)-1):
	#	print indexOfWrongTableNames[m]
	#	del listRemoveIndex[indexOfWrongTableNames[m]]
				

	#print("THESE ARE THE INDICES TO BE REMOVED___UPDATED")
	#for n in range(0, len(listRemoveIndex)):
	#	print tableStartList[listRemoveIndex[n]]


	tableTitleList = [ item for item in tableTitleList if tableTitleList.index(item) not in listRemoveIndex ]
	tableStartList = [ item for item in tableStartList if tableStartList.index(item) not in listRemoveIndex ]
	tableEndList = [ item for item in tableEndList if tableEndList.index(item) not in listRemoveIndex ]


	#print ("Start list has size: ", len(tableStartList))
	#print ("End list has size: ", len(tableEndList))
	#print ("Titles list has size: ", len(tableTitleList))

	#print "THE UPDATED TITLE LIST:"
	#for n in range(0, len(tableTitleList)-1):
	#	print tableTitleList[n]
	#	print (tableStartList[n], " ", tableEndList[n])




	for n in range(0, len(tableTitleList)):
		for word in tableTitleList[n]:
			#print "HERE       ",word
			if ('Operating Cost' in word or 'Operating cost' in word or 'operating cost' in word or 'OPEX' in word or 'operating costs' in word or 'Operating Costs' in word or 'Operating costs' in word or 'operating unit cost' in word or 'Operating unit cost' in word or 'Operating Unit Cost' in word):
				opexTableList.append(n)
				opexStartList.append(tableStartList[n]-2)
				opexEndList.append(tableEndList[n])
				#print ("FOUND OPEX IN ",n)

	#print " "
	#print " "
	#print "OPEX TABLE LIST:"
	#print " "

	#for n in range(0, len(opexTableList)):
	#	print opexTableList[n]

	# print " "
	# print "The OPEX tables are the following: "
	# print " "

	mypath = r'C:\scraping\Isaac\results\%s\\' % (ProjectName)
	if not os.path.isdir(mypath):
	   os.makedirs(mypath)
	   # os.chdir(mypath)

	# os.chdir(scrapingDir)
	c = csv.writer(open(mypath+"OPEX.csv", "wb"))
	for n in range(0, len(opexTableList)):
		fCSV = open(fileDirectory)
		opexReader=csv.reader(fCSV)
		for line in islice(opexReader, opexStartList[n], opexEndList[n]-1):
			# print line
			c.writerow(line)
		# print " "
		# print "**********"
		# print " "
		c.writerow(" ") 
		c.writerow("**********")
		c.writerow(" ")
		fCSV.close()
	# c.close()
		





	for n in range(0, len(tableTitleList)):
		for word in tableTitleList[n]:
			#print "HERE       ",word
			if ('capital cost' in word or 'Capital Cost' in word or 'Capital cost' in word or 'CAPEX' in word):
				capexTableList.append(n)
				capexStartList.append(tableStartList[n]-1)
				capexEndList.append(tableEndList[n])
				#print ("FOUND CAPEX IN ",n)

	#print "THE CAPEX TABLES ARE:"
	#for n in range(0, len(capexTableList)-1):
	#	print capexTableList[n]
	#	print (capexStartList[n], " ", capexEndList[n]) 

	#capexTableList = filter(lambda name: str(name).strip(), capexTableList)

	#	print tableTitleList[capexTableList[n]]
	#print "CAPEXTABLELIST INDEX 4 IS"
	#print capexTableList[4]
	#print "TABLETITLELIST INDEX 75 IS"
	#print tableTitleList[75]
	#print "capexStartLIST HAS LENGTH ", len(capexStartList)
	#print "capexEndLIST HAS LENGTH ", len(capexEndList)
	#for n in range(0, len(capexTableList)-1):
	#	print capexTableList[n]

	# print "****************************************************"
	# print " "
	# print "The CAPEX tables are the following: "
	# print " "

	c = csv.writer(open(mypath+"CAPEX.csv", "wb"))
	for n in range(0, len(capexTableList)):
		fCSV = open(fileDirectory)
		capexReader=csv.reader(fCSV)
		for line in islice(capexReader, capexStartList[n]-1, capexEndList[n]):
			# print line
			c.writerow(line)
		# print " "
		# print "**********"
		# print " "
		c.writerow(" ") 
		c.writerow("**********")
		c.writerow(" ")
		fCSV.close()
		
				




	#	for y in range(capexStartList[n],capexEndList[n]):
				

	#		while x<len(row):
	#			print row[y][x]

	   		
	#		print text

	#print "THE TABLES SHOWING THE CAPITAL COST ARE THE FOLLOWING"
	#for n in range(0, len(capexTableList)):
	#	print tableTitleList[capexTableList[n]]


	#with open(fileDirectory, mode='r') as f:
	#    reader = csv.reader(f)
	#    for row in islice(reader, 0, None):
	#    	counter=counter+1
	#        if (('Resource' in row[0] or 'RESOURCE' in row[0] or 'resource' in row[0]) and ('Table' in row[0] or 'TABLE' in row[0] or 'table' in row[0]) and ":" in row[0])\
	#        or (('Estimate' in row[0] or 'ESTIMATE' in row[0] or 'estimate' in row[0]) and ('Table' in row[0] or 'TABLE' in row[0] or 'table' in row[0])) and ":" in row[0]:
	#        	print ("COUNTER 1 is now: ",counter)
	#        	print(row)
	#        	for  inrow in islice(reader, counter, counter+100):
	#        		counter2=counter2+1;
	#        		if 1<len(inrow) and inrow[1]!='' and ('inferred' in inrow[1] or 'INFERRED' in inrow[1] or 'Inferred' in inrow[1]) \
	#            	or 1<len(inrow) and inrow[1]!='' and ('indicated' in inrow[1] or 'INDICATED' in inrow[1] or 'Indicated' in inrow[1]) \
	#            	or 1<len(inrow) and inrow[1]!='' and ('measured' in inrow[1] or 'MEASURED' in inrow[1] or 'Measured' in inrow[1]) \
	#            	or 1<len(inrow) and inrow[1]!='' and ('M+I' in inrow[1]): 
	#            			print ("COUNTER 2 is now: ",counter2)
	#            			print(inrow)


	            	

	#RESOURCE TABLES
	for n in range(0, len(tableTitleList)):
		for word in tableTitleList[n]:
			#print "HERE       ",word
			if ('RESOURCE' in word or 'Resource' in word or 'resource' in word or 'resources' in word or 'Resources' in word or 'RESOURCES' in word):
				resourceTableList.append(n)
				resourceStartList.append(tableStartList[n]-1)
				resourceEndList.append(tableEndList[n])
				#print ("FOUND RESOURCE IN ",n)


	# print " "
	# print "The RESOURCE tables are the following: "
	# print " "

	c = csv.writer(open(mypath+"Resource.csv", "wb"))
	for n in range(0, len(resourceTableList)):
		fCSV = open(fileDirectory)
		resourceReader=csv.reader(fCSV)
		for line in islice(resourceReader, resourceStartList[n]-1, resourceEndList[n]):
			# print line
			c.writerow(line)
		# print " "
		# print "**********"
		# print " "
		c.writerow(" ") 
		c.writerow("**********")
		c.writerow(" ")
		fCSV.close()
		

	#RESERVE TABLES

	for n in range(0, len(tableTitleList)):
		for word in tableTitleList[n]:
			#print "HERE       ",word
			if ('RESERVE' in word or 'Reserve' in word or 'reserve' in word or 'reserves' in word or 'Reserves' in word or 'RESERVES' in word):
				reserveTableList.append(n)
				reserveStartList.append(tableStartList[n]-1)
				reserveEndList.append(tableEndList[n])
				#print ("FOUND RESERVE IN ",n)


	# print " "
	# print "The RESERVE tables are the following: "
	# print " "

	c = csv.writer(open(mypath+"Reserve.csv", "wb"))
	for n in range(0, len(reserveTableList)):
		fCSV = open(fileDirectory)
		reserveReader=csv.reader(fCSV)
		try:
			islice(reserveReader, reserveStartList[n]-1, reserveEndList[n])
		except ValueError:
			print 'Indices for islice() must be None or an integer: 0 <= x <= maxint'
			continue
		else:
			for line in islice(reserveReader, reserveStartList[n]-1, reserveEndList[n]):
				# print line
				c.writerow(line)
			# print " "
			# print "**********"
			# print " "
			c.writerow(" ") 
			c.writerow("**********")
			c.writerow(" ")
			fCSV.close()
		


	#COMMODITY PRICE TABLES
	for n in range(0, len(tableTitleList)):
		for word in tableTitleList[n]:
	#		print "HERE       ",word
			if ('Price' in word or 'PRICE' in word or 'price' in word):
				comprTableList.append(n)
				comprStartList.append(tableStartList[n]-1)
				comprEndList.append(tableEndList[n])
	#			print ("FOUND COMMODITY PRICE IN ",n)
				comprCounter+=1


	if comprCounter!=0:
		# print " "
		# print "The COMMODITY PRICE tables are the following: "
		# print " "	
		c = csv.writer(open(mypath+"Commodity_Price.csv", "wb"))
		for n in range(0, len(comprTableList)):
			fCSV = open(fileDirectory)
			comprReader=csv.reader(fCSV)
			for line in islice(comprReader, comprStartList[n]-1, comprEndList[n]):
				# print line
				c.writerow(line)
			# print " "
			# print "**********"
			# print " "
			c.writerow(" ") 
			c.writerow("**********")
			c.writerow(" ")
			fCSV.close()
	comprCounter=0






	#DISCOUNT RATE TABLES
	for n in range(0, len(tableTitleList)):
		for word in tableTitleList[n]:
			#print "HERE       ",word
			if ('DISCOUNT RATE' in word or 'Discount Rate' in word or 'Discount rate' in word or 'discount rate' in word):
				discrTableList.append(n)
				discrStartList.append(tableStartList[n]-1)
				discrEndList.append(tableEndList[n])
				#print ("FOUND DISCOUNT RATE IN ",n)


	# print " "
	# print "The DISCOUNT RATE tables are the following: "
	# print " "
	c = csv.writer(open(mypath+"Discount_Rate.csv", "wb"))
	for n in range(0, len(discrTableList)):
		fCSV = open(fileDirectory)
		discrReader=csv.reader(fCSV)
		try:
			islice(discrReader, discrStartList[n]-1, discrEndList[n])
		except ValueError:
			print 'Indices for islice() must be None or an integer: 0 <= x <= maxint'
			continue
		else:
			for line in islice(discrReader, discrStartList[n]-1, discrEndList[n]):
				# print line
				c.writerow(line)
		# print " "
		# print "**********"
		# print " "
			c.writerow(" ") 
			c.writerow("**********")
			c.writerow(" ")
			fCSV.close()


	#NPV TABLES
	for n in range(0, len(tableTitleList)):
		for word in tableTitleList[n]:
			#print "HERE       ",word
			if ('NPV' in word or 'npv' in word or 'Net Present Value' in word or 'net present value' in word or 'NET PRESENT VALUE' in word):
				NPVTableList.append(n)
				NPVStartList.append(tableStartList[n]-1)
				NPVEndList.append(tableEndList[n])
				#print ("FOUND DISCOUNT RATE IN ",n)


	# print " "
	# print "The NPV tables are the following: "
	# print " "
	c = csv.writer(open(mypath+"NPV.csv", "wb"))
	for n in range(0, len(NPVTableList)):
		fCSV = open(fileDirectory)
		NPVReader=csv.reader(fCSV)
		for line in islice(NPVReader, NPVStartList[n]-1, NPVEndList[n]):
			# print line
			c.writerow(line)
		# print " "
		# print "**********"
		# print " "
		c.writerow(" ") 
		c.writerow("**********")
		c.writerow(" ")
		fCSV.close()






	#MINING METHOD
	miningMethod='None' 
	inPitCounter=0
	undergroundCounter=0
	with open(fileDirectory, mode='r') as f1:
		reader1 = csv.reader(f1)
		for row1 in islice(reader1, 0, None):
			if 0<len(row1) and ('underground' in row1[0] or 'Underground' in row1[0]):
				undergroundCounter=undergroundCounter+1
			if 0<len(row1) and ('in-pit' in row1[0] or 'in pit' in row1[0] or 'In-pit' in row1[0] or 'open pit' in row1[0]):
				inPitCounter=inPitCounter+1
			
			
	if undergroundCounter<inPitCounter:
		miningMethod='In-pit'

	if undergroundCounter>inPitCounter:
		miningMethod='Underground'

	if undergroundCounter==inPitCounter:
		miningMethod='In-pit and Underground'
	#print 'Counts of in-pit:', inPitCounter
	#print 'Counts of underground:', undergroundCounter
	# print ('Mining method: '+miningMethod)


	productionRate=""
	rateLine="name"
	rateCounter=0
	rateUnits='None'
	prodRateCorrectSent=0
	with open(fileDirectory, mode='r') as f2:
		reader2 = csv.reader(f2)
		for row2 in islice(reader2, 0, None):
			if 0<len(row2) and ('mining rate' in row2[0] or 'Mining rate' in row2[0] or 'Production rate' in row2[0] or 'production rate' in row2[0] or 'troughput' in row2[0] or 'Throughput' in row2[0] or 'Production' in row2[0]) and ('mtpa' in row2[0] or 'Mtpa' in row2[0] or 'Mtpy' in row2[0] or 'Mt/y' in row2[0] or 'mt/y' in row2[0] or 't/d' in row2[0] or 'tpd' in row2[0]):
	#			print row2[0]
				rowTokenized=nltk.word_tokenize(row2[0])
				for word in rowTokenized:
					rateCounter=rateCounter+1
					
					if word.isdigit()==True	or ',000' in word:
	#					print word
						prodRateCorrectSent+=1
						try:
							rowTokenized[rateCounter]
						except IndexError:
							print 'No rowTokenized[%d]' % (rateCounter)
							continue
						else:
							rateUnits=rowTokenized[rateCounter]
	#					print "RATE UNITS "+ rateUnits
						if (rateUnits!='tpd' and rateUnits!='Mtpa' and rateUnits!='Mt/y' and rateUnits!='MTPA' and rateUnits!='Mtpy'):
							continue
						# else:print("Production rate: "+word+" "+rateUnits)	
						productionRate=word+rateUnits
						break
					else:continue
				break
				rateCounter=0
			#if 0<len(row2) and ('year' in row2[0] or 'Year' in row2[0] or 'years' in row2[0]) and ('mtpa' in row2[0] or 'Mtpa' in row2[0] or 'Mt/y' in row2[0] or 'mt/y' in row2[0] or 't/d' in row2[0] or 'tpd' in row2[0]):
				#print row2[0]

#Date of project
	f = open(filename, 'r').read()
	months = 'January|February|March|April|May|June|July|August|September|October|November|December|Jan|Feb|Mar|Apr|May|June|July|Aug|Sept|Oct|Nov|Dec'
	monthCandidates = re.findall(months, f)
	month = ''
	monthDict = nltk.defaultdict(int)

	for mn in monthCandidates:
	    monthDict[mn] += 1
	    if len(month) == 0:
	    	month = mn
	    else:
	    	if monthDict[mn] > monthDict[month]:
	    		month = mn
	if len(month) == 0:
		month = 'noMonth'

	years = ''
	for i in range(114):
		years += str(1900+i)
		if i != 113:
			years += '|'
	# print years
	yearCandidates = re.findall(years, f)
	year = ''
	yearDict = nltk.defaultdict(int)

	for yr in yearCandidates:
	    yearDict[yr] += 1
	    if len(year) == 0:
	    	year = yr
	    else:
	    	if yearDict[yr] > yearDict[year]:
	    		year = yr
	if len(year) == 0:
		year = 'noYear'

	date = month + ' ' + year

	c = csv.writer(open(mypath+"Info.csv", "wb"))
	c.writerow(["Date", date])
	c.writerow(["Project Name",ProjectName])
	c.writerow(["Commodity",commodity])
	c.writerow(["Country",country])
	c.writerow(["Currency",currency])
	c.writerow(["Mining method",miningMethod])
	c.writerow(["Production rate",productionRate])

	# for txt in os.listdir(src):
	# print txt
	# if txt[-3:] == 'txt':
	# 	print txt
	dstTXTCSV = 'C:\scraping\Isaac\isScraped\csvTxts'
	dstNames = 'C:\scraping\Isaac\isScraped\\namesOfScrapingFiles'
	dstPjt = mypath
	copy(filename, dstPjt)
	move(filename, dstTXTCSV)
	move(fileDirectory, dstTXTCSV)
	move(scrapingFileNames+fileDirectory, dstNames)
