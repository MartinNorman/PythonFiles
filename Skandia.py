#########################################
##Import needed libraries
#########################################
from selenium import webdriver
import codecs #To be able to write the file

Company = "Skandia"

#########################################
## Settings, create connection to Chrome and set timeout
#########################################
driver_Link = webdriver.Chrome("C:\\Users\\clman\\Documents\\Funds\\chromedriver.exe")
driver_Link.set_page_load_timeout(30)


########################################
# Create empty file so we can write to it later
########################################
Company = codecs.open(r'C:\Users\clman\Documents\Funds\Funds_Skandia.txt', 'w', 'utf-8-sig')
texttowrite = 'ISIN@Source'
Company.write(texttowrite + '\r\n')

########################################
# Get data
########################################
driver_Link.get("https://secure.msse.se/skandia/sweden/ska/all/sv/quickrank?showallfunds=True")

Funds = driver_Link.find_elements_by_xpath("//table[@class='table-responsive table-responsive--fondsliste snapper-table']/child::tbody/child::tr/child::td[1]/child::div[2]/child::div/child::a")

for Fund in Funds:
    Link = Fund.get_attribute("href")
    ISIN = Link[38:50]
    Source = "Skandia"

    ###############################################
    # Write to file
    ###############################################
    if len(ISIN) == 12:

        Company.write("%s" %ISIN + "@" + "%s" %Source + '\r\n')

driver_Link.quit()
