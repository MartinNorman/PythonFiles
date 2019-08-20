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
IDs = codecs.open(r'W:\Martin\Nordnet\ID.txt', 'w', 'utf-8-sig')

#########################################
## Start loop for each page where the funds are listed
## Improvement is to automatically figure out how many pages there are
#########################################

static = "https://www.nordnet.se/mux/web/fonder/sok.html?nn_kategori=&kategori=&forvaltare=&sokord=&sok=1&ppm=0&nobuy=&flik=&nm=&typ=1"
driver_Link.get(static)
Links = driver_Link.find_elements_by_xpath("//table/child::tbody/descendant::tr/child::td[2]/child::div/child::a")

#########################################
## For each page with fund links loop through each fund page
#########################################
for Link in Links:

    PreID = Link.get_attribute("href")
    print(PreID)
#    CharToFind = '='
#    CharIsAt = PreID.index(CharToFind, 10)
    ID = PreID[61:71]
    print(ID)
    ################################################
    ## Write to file
    ################################################
    IDs.write("%s" %ID + '\r\n')


driver_Link.quit()
