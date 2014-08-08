import os
os.chdir(r'C:\Python27\Scripts')
import pdf2txt
import glob
import fnmatch


files_in_dir = os.listdir(r'C:\scraping\Isaac\toBeScraped\pdf2txt')

filename="NAME"

os.chdir(r'C:\scraping\Isaac\toBeScraped\pdf2txt')
#for file_in_dir in files_in_dir:
	#os.system("pdf2txt.py -o "+file_in_dir+" "+file_in_dir)
#	 print os.path.splitext("path_to_file")[0]

	 
#for file in glob.glob("*.pdf"):
#    print file
	
for file in os.listdir (r'C:\scraping\Isaac\toBeScraped\pdf2txt'):
	filename=file.rstrip(file[-3:])
	os.system("pdf2txt.py -o"+"\""+filename+"txt"+""" " """+"\""+filename+"pdf"+""" " """)