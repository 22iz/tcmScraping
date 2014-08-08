# import nltk
# import os
# import csv
# from itertools import islice
# import sys
# # from ABBYY import CloudOCR
# from nltk.corpus import gazetteers
# import re

##################################################################################################################
# with open(r'C:\scraping\Isaac\csvTxts\20101029 Didipio Gold-Copper Project Au Cu, Philippines.txt', 'r') as f:
# 	for f1 in f:
# 		print f1
##################################################################################################################

##################################################################################################################
# scrapingFileNames = r'C:\scraping\Isaac\csvTxts'
# os.chdir(scrapingFileNames)
# for file in os.listdir(scrapingFileNames):
# 	filename=file[:-4]
# 	print filename

# 	f = open(filename+'.txt', 'r').read()
# 	projectCandidates = re.findall('(?:[A-Z]\w*\s)+Project', f)

# 	projectDict = nltk.defaultdict(int)
# 	for project in projectCandidates:
# 	    projectDict[project] += 1
# 	    # print project

# 	pD = dict(zip(projectDict.values(), projectDict.keys()))
# 	if not pD:
# 		continue
# 	print str(max(pD))+' of '+pD[max(pD)]+"\nis the project name of report <-- "+file+" -->\n"
##################################################################################################################

##################################################################################################################
# from shutil import move

# src = 'C:\scraping\Isaac\csvTxts\\'
# dst = 'C:\scraping\Isaac\isScraped\TXTs'

# for txt in os.listdir(src):
# 	# print txt
# 	if txt[-3:] == 'txt':
# 		print txt
# 		move(src+txt, dst)
##################################################################################################################

import nltk
import os
import csv
from itertools import islice
import sys
#from ABBYY import CloudOCR
from nltk.corpus import gazetteers
import re
from shutil import move


scrapingFileNames = r'C:\scraping\Isaac\toBeScraped\namesOfScrapingFiles\\'
scrapingDir = r'C:\scraping\Isaac\toBeScraped\csvTxts\\'
os.chdir(scrapingDir)
scrapingLogs = r'C:\scraping\Isaac\logs'

for file in os.listdir (scrapingFileNames):
	filename = file[:-4]
	fileDirectory=filename

	placelist = gazetteers.words('countries.txt')
	currencyList=gazetteers.words('currencyList.txt')
	filename=filename+'.txt'

	#name of project
	# print filename
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
	print 'file: ' + filename + '\n'
	# for pjs in projectDict:
	# 	print('	' + pjs + ': ' + str(projectDict[pjs]) + '\n')
	# 	print('	project name is ::::::::::::::::::::::: ' + ProjectName +'\n\n')

	with open(scrapingLogs+'\log-projects3.txt', 'a+') as fLog:
		fLog.write('file: ' + filename + '\n')
		for pjs in projectDict:
			fLog.write('	' + pjs + ': ' + str(projectDict[pjs]) + '\n')
		fLog.write('	project name is ::::::::::::::::::::::: ' + ProjectName +'\n\n')

#####################################################################################################################################################################
	# #Date of project
	# f = open(filename, 'r').read()
	# months = 'January|February|March|April|May|June|July|August|September|October|November|December|Jan|Feb|Mar|Apr|May|June|July|Aug|Sept|Oct|Nov|Dec'
	# monthCandidates = re.findall(months, f)
	# month = ''
	# monthDict = nltk.defaultdict(int)

	# for mn in monthCandidates:
	#     monthDict[mn] += 1
	#     if len(month) == 0:
	#     	month = mn
	#     else:
	#     	if monthDict[mn] > monthDict[month]:
	#     		month = mn
	# if len(month) == 0:
	# 	month = 'noDate'
	# # print 'month is ::::::::::::::::::::::: ' + month + ' with ' + str(dateDict[month])

	# years = ''
	# for i in range(115):
	# 	years += str(1900+i)
	# 	if i != 114:
	# 		years += '|'
	# # print years
	# yearCandidates = re.findall(years, f)
	# year = ''
	# yearDict = nltk.defaultdict(int)

	# for yr in yearCandidates:
	#     yearDict[yr] += 1
	#     if len(year) == 0:
	#     	year = yr
	#     else:
	#     	if yearDict[yr] > yearDict[year]:
	#     		year = yr
	# if len(year) == 0:
	# 	year = 'noYear'
	# print 'date is ::::::::::::::::::::::: ' + month + ' ' + year + ' with ' + str(monthDict[month]) + ' ' + str(yearDict[year])
#######################################################################################################################################################################


#commodity of project
	# f = open(filename, 'r').read()
	# commodities = 'Gold|Silver|Platinum|Iridium|Osmium|Palladium|Rhodium|Ruthenium|Bauxite|Lead|Chromium|Cobalt|Lithium|Magnesium|Manganese|Nickel|Nickel|Tin|Tungsten|Zinc|Phosphate|Copper|Molybdenum|Uranium|Iron|Iron|Iron|Coal|Coal|Aluminium|Alunite|Andalusite|Anthracite|Antimony|Arsenic|Asbestos|Barite|Barium|Barium-Barite|Beryllium|Bismuth|Boron-Borates|Bromine|Cadmium|Calcium Carbonate|Cerium|Cesium|Chalk|Chlorine|Chlorite|Chromium oxide|Copper Oxide|Copper Sulfide|Corundum|Diatomite|Dolomite|Dysprosium|Dysprosium oxide|Emery|Erbium|Europium|Feldspar|Ferrochrome|Ferromanganese|Ferrosilicon|Fluorine-Fluorite|Fluorite|Gallium|Gallium oxide|Garnet|Germanium|Gardolinium|Gilsonite|Granite|Graphite|Gypsum|Gypsum-Anhydrite|Hafnium|Hafnium oxide|Halite|High Calcium|Holmium|Ilmenite|Indium|Iodine|Jade|Jasper|Kaolin|Kyanite|Lanthanum|Leucoxene|Lignite|Lime|Limestone|Limestone-Limesand|Limonite|Lithium oxide|Lutetium|Magnesia|Magnesite|Magnetite|Hematite|Marble|Mercury|Mica|Monazite|Montmorillonite|Neodymium|Nickel|Niobium|Niobium pentoxide|Peat|Perlite|Phosphorus|Potassium|Potassium sulphate|Praseodymium|Pyrophyllite|Quartzite|Radium|Rare earth oxides|Rare Earth Elements|Total Rare Earth Oxide|Total Rare Earth Element|Rhenium|Rubidium|Sandstone|Saponite|Scandium|Selenium|Siderite|Silica|Sillimanite|Sodium|Sodium Carbonate|Sodium Sulfate|Samarium|Spodumene|Staurolite|Strontium|Sulfur|Sulfur-Pyrite|Tantalum pentoxide|Terbium|Tellurium|Thallium|Thorium|Titanium|Titanium dioxide|Thulium|Tungsten trioxide|Uranium oxide|Vanadium|Vanadium pentoxide|Wollastonite|Xenotime|Yttrium oxide|Yttrium|Ytterbium|Zeolites|Zircon|Zirconia|Zirconium|Platinum Group Metals|Platinum Group Elements|Gold Eq|Silver Eq|Zinc Eq|Copper Eq|Molybdenum Eq|Iron|Pig Iron|Iron Pellets|DSO|BFO|Coal'
	# commodCandidates = re.findall(commodities, f)
	# commodity = ''
	# commodDict = nltk.defaultdict(int)

	# for cd in commodCandidates:
	#     commodDict[cd] += 1
	#     if len(commodity) == 0:
	#     	commodity = cd
	#     else:
	#     	if commodDict[cd] > commodDict[commodity]:
	#     		commodity = cd
	# if len(commodity) == 0:
	# 	commodity = 'noCommodity'
	# for cds in commodDict:
	# 	print cds + ': ' + str(commodDict[cds])
	# print 'commodity is ::::::::::::::::::::::: ' + commodity + ' with ' + str(commodDict[commodity])