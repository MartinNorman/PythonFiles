import requests
import codecs
import json
import datetime

vDate = datetime.datetime.now().strftime("%Y-%m-%d")
print(vDate)

#Funds
Nav = codecs.open(r'/volume1/homes/Martin/Avanza/Result/Nav' + vDate + '.txt', 'w', 'utf-8')
texttowrite = 'ID@ISIN@NAV@NAVDATE'
Nav.write(texttowrite + '\r\n')
print("File to write to created")

#Get IDs to read
#f = open('/volume1/homes/Martin/Avanza/ID.txt', mode='r')
print("File to read from opened")
f = open('/volume1/homes/Martin/Avanza/ID.txt', mode='r', encoding = 'utf-8')
for x in f:
	print(x)
	static = "https://www.avanza.se/_cqbe/fund/guide/"
	res = requests.get(static + x.strip())
	x_stripped = x.strip()
	res2 = res.json()
	isin = res2["isin"]
	nav = res2["nav"]
	navDate = res2["navDate"]
	
	#Write to file
	Nav.write("%s" %x_stripped + "@" + "%s" %isin + "@" + "%s" %nav + "@" + "%s" %navDate + '\r\n')  
