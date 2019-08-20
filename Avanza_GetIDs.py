#########################################
##Import needed libraries
#########################################
from selenium import webdriver
import codecs #To be able to write the file
#import time #To be able to sleep
#########################################
## Settings, create connection to Chrome and set timeout
#########################################
driver_Link = webdriver.Chrome("C:\\Users\\clman\\Documents\\Funds\\chromedriver.exe")
driver_Link.set_page_load_timeout(30)

#########################################
## Create empty file so we can write to it later
#########################################
IDs = codecs.open(r'C:\Users\clman\Documents\Funds\Avanza\ID.txt', 'w', 'utf-8-sig')
texttowrite = 'ID'
IDs.write(texttowrite + '\r\n')

#########################################
## Start loop for each page where the funds are listed
## Improvement is to automatically figure out how many pages there are
#########################################

for page in range(1,45,1):
    print(page)

    static = "https://www.avanza.se/fonder/lista.html?page="
    dynamic = str(page)
    sortorder = "&sortField=NAME&sortOrder=ASCENDING"
    driver_Link.get(static + dynamic + sortorder)
    Links = driver_Link.find_elements_by_xpath("//table[@id='contentTable']/child::tbody/descendant::tr/child::td[@class='overview tLeft fundListName']/child::a")

    #########################################
    ## For each page with fund links loop through each fund page
    #########################################
    for Link in Links:
        PreID = Link.get_attribute("href")
        CharToFind = '/'
        SlashIsAt = PreID.index(CharToFind, 44)
        ID = PreID[44:SlashIsAt]

        ################################################
        ## Write to file
        ################################################
        IDs.write("%s" %ID + '\r\n')


driver_Link.quit()
