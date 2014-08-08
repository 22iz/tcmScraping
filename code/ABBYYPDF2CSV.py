import os, sys, tempfile
import SendKeys
from SendKeys import SendKeys
from pywinauto import application
import time
from shutil import move


def addToClipBoard(text):
    command = 'echo ' + text.strip() + '| clip'
    os.system(command)

#time.sleep(10)

path = r'C:\scraping\Isaac\toBeScraped\pdfsForABBYY\\'

for file in os.listdir (path):
	filename=file.rstrip()
	addToClipBoard(filename)
	app = application.Application()
	app.Start_("C:\Program Files (x86)\ABBYY PDF Transformer+\Transformer.exe")
	app.connect_(path="C:\Program Files (x86)\ABBYY PDF Transformer+\Transformer.exe")
	time.sleep(5)
	SendKeys("""{TAB}{TAB}{RIGHT}{RIGHT}{RIGHT}{RIGHT}{RIGHT}{SPACE}""")
	# app.Transformer.Click()
	SendKeys("""{DOWN}{DOWN}{DOWN}{DOWN}{ENTER}""")
	SendKeys("""C:\scraping\Isaac\\toBeScraped\pdfsForABBYY""")
	SendKeys("""{\}""")
	SendKeys("""^v""")
	time.sleep(2)
	SendKeys("""{ENTER}""")
	time.sleep(600)
	SendKeys("""{ENTER}""")
	time.sleep(10)
	app.Kill_()
	#SendKeys("""%{F4}""")


	# dstPDFs = 'C:\scraping\Isaac\isScraped\PDFs'
	# move(path + filename, dstPDFs)