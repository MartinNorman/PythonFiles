#########################################
##Import needed libraries
#########################################
from selenium import webdriver
import codecs #To be able to write the file

Company = "Lansforsakringar"

#########################################
## Settings, create connection to Chrome and set timeout
#########################################
driver_Link = webdriver.Chrome("C:\\Users\\clman\\Documents\\Funds\\chromedriver.exe")
driver_Link.set_page_load_timeout(30)


########################################
# Create empty file so we can write to it later
########################################
Company = codecs.open(r'C:\Users\clman\Documents\Funds\Funds_Lansforsakringar.txt', 'w', 'utf-8-sig')
texttowrite = 'ISIN@Source'
Company.write(texttowrite + '\r\n')


########################################
# Get data
########################################
driver_Link.get("https://web.msse.se/lansforsakringar/lffs")

Funds = driver_Link.find_elements_by_xpath("//table[@class='biglist']/child::tbody/child::tr/child::td[3]/child::a")

for Fund in Funds:
    Link = Fund.get_attribute("href")
    CharToFind = '='
    CharIsAt = Link.index(CharToFind)
    ISIN = Link[CharIsAt + 1:]

    Source = "Länsförsäkringar"
    ###############################################
    # Write to file
    ###############################################
    Company.write("%s" %ISIN + "@" + "%s" %Source + '\r\n')

driver_Link.quit()
