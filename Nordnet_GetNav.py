#!/bin/python2.7
#########################################
##Import needed libraries
#########################################
import time #To be able to sleep
import requests
from bs4 import BeautifulSoup
from datetime import datetime
import codecs #To be able to write the file


#########################################
##Static paths and variables
#########################################
static1 = "https://secust.msse.se/se/nordnetny/funds/overview.aspx?cid="
static2 = "&cntry=SE"
vDate = datetime.now().strftime("%Y-%m-%d")


#########################################
## Create empty file so we can write to it later
#########################################
Nordnet_Nav = codecs.open(r'/volume1/homes/Martin/Nordnet/Result/Nav' + vDate + '.txt', 'w', 'utf-8')

#########################################
## Get IDs to read
#########################################
with codecs.open('/volume1/homes/Martin/Nordnet/ID.txt', 'r', encoding='utf-8') as Funds:
	for Fund in Funds:
		Fund2 = Fund.strip()
		res = requests.get(static1 + Fund2 + static2)
		soup = BeautifulSoup(res.content, 'lxml')
		table = soup.find('table', {"id" : "Table1"})
		Nav = table.find_all('td')[3].text
		PreNavDate = table.find_all('td')[5].text
		NavDate = PreNavDate.strip()
################################################
## Write to file
################################################
		Nordnet_Nav.write("%s" %Fund2 + "@" + "%s" %Nav + "@" "%s" %NavDate + '\r\n')