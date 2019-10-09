#!/bin/python2.7
#########################################
##Import needed libraries
#########################################
import time #To be able to sleep
import requests
from bs4 import BeautifulSoup
from datetime import datetime
import codecs #To be able to write the file
from local_paths import output
from local_paths import output_error
from local_paths import input


#########################################
##Static paths and variables
#########################################
static1 = "https://secust.msse.se/se/nordnetny/funds/overview.aspx?cid="
static2 = "&cntry=SE"
vDate = datetime.now().strftime("%Y-%m-%d")


#########################################
## Create empty file so we can write to it later
#########################################
Nordnet_Nav = codecs.open(output + '/' + 'Nav' + vDate + '.txt', 'w', 'utf-8')
texttowrite = 'ID@NAV@NAVDATE'
Nordnet_Nav.write(texttowrite + '\r\n')

#########################################
# Funds with errors
#########################################
ErrorID = codecs.open(output_error + '/' + 'Error' + vDate + '.txt', 'w', 'utf-8')
texttowrite = 'ID@ERROR'
ErrorID.write(texttowrite + '\r\n')


#########################################
## Get IDs to read
#########################################
with codecs.open('/volume1/homes/Martin/Nordnet/ID.txt', 'r', encoding='utf-8') as Funds:
	for Fund in Funds:
		Fund2 = Fund.strip()
		res = requests.get(static1 + Fund2 + static2)
		try:
			soup = BeautifulSoup(res.content, 'lxml')
			table = soup.find('table', {"id" : "Table1"})
			Nav = table.find_all('td')[3].text
			PreNavDate = table.find_all('td')[5].text
			NavDate = PreNavDate.strip()
		except Exception as e:
			ErrorID.write("%s" % x_stripped  + "@" + "%s" % str(e) + '\r\n')
################################################
## Write to file
################################################
		Nordnet_Nav.write("%s" %Fund2 + "@" + "%s" %Nav + "@" "%s" %NavDate + '\r\n')