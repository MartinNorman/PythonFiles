#########################################
##Import needed libraries
#########################################
from selenium import webdriver
import codecs #To be able to write the file

Company = "Folksam"

#########################################
## Settings, create connection to Chrome and set timeout
#########################################
driver_Link = webdriver.Chrome("C:\\Users\\clman\\Documents\\Funds\\chromedriver.exe")
driver_Link.set_page_load_timeout(30)


########################################
# Create empty file so we can write to it later
########################################
Company = codecs.open(r'C:\Users\clman\Documents\Funds\Funds_Folksam.txt', 'w', 'utf-8-sig')
texttowrite = 'ISIN@Source'
Company.write(texttowrite + '\r\n')


########################################
# Get data
########################################
driver_Link.get("http://web.msse.se/FOLKSAM/Web/hand/quickrank/categoryandcodes?sort=name&sortdir=asc&intern=False&sortspec=0&ret=TrailingReturns.YTD&bl=2&bit=&category=&company=&freetext=&categorize=false&ppm=False")
Funds = driver_Link.find_elements_by_xpath("//div[@class='tablelist']/child::table/child::tbody/child::tr/child::td[6]")

for Fund in Funds:
    ISIN = Fund.text
    Source = "Folksam"
    ################################################
    ## Write to file
    ################################################
    Company.write("%s" %ISIN + "@" + "%s" %Source + '\r\n')

driver_Link.quit()
