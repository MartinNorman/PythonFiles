#########################################
##Import needed libraries
#########################################
from selenium import webdriver
import codecs #To be able to write the file
import time #To be able to sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

Company = "SEB"

#########################################
## Settings, create connection to Chrome and set timeout
#########################################
driver_Link = webdriver.Chrome("C:\\Users\\clman\\Documents\\Funds\\chromedriver.exe")
driver_Link.set_page_load_timeout(30)


########################################
# Create empty file so we can write to it later
########################################
Company = codecs.open(r'C:\Users\clman\Documents\Funds\Funds_SEB.txt', 'w', 'utf-8-sig')
texttowrite = 'ISIN@Source'
Company.write(texttowrite + '\r\n')

########################################
# Get data
########################################
driver_Link.get("https://seb.se/bors-och-finans/fonder/fondlista#/")

#driver_Link.find_element_by_xpath("//div[@class='pw-helper__submit-cell']/child::button[@class='sdv-button']").click()
#driver_Link.find_element_by_xpath("/html/body/main/div/div/div/fund-list-root/div/fund-list-home/div[2]/section/div/fund-list-table/section/infront-table/div[3]/div[2]").click()
#time.sleep(3)
#driver_Link.find_element_by_xpath("//section[@class='card bg-success mb-4 hello-box mt-2']/child::footer/child::p/child::button").click()
driver_Link.find_element_by_xpath("//section[@class='card bg-success mb-4 hello-box mt-2']/child::footer/child::p/child::button").click()
time.sleep(3)
#driver_Link.find_element_by_xpath("//section[@class='alternate-even-row-color']/child::infront-table/child::div[@id='showMoreFundsLink']").click()
driver_Link.find_element_by_xpath("//section[@class='alternate-even-row-color']/child::infront-table/child::div[@id='showMoreFundsLink']").click()
time.sleep(3)
#driver_Link.find_element_by_xpath("//section[@class='alternate-even-row-color']/child::infront-table/child::div[@id='showAllFundsLink']").click()
driver_Link.find_element_by_xpath("//section[@class='alternate-even-row-color']/child::infront-table/child::div[@id='showAllFundsLink']").click()
time.sleep(3)
#/child::div[@class='cell-arrow  cell-arrow--down  cell-flex-list__expand-icon']
#elem = driver_Link.find_element_by_xpath("//section[@class='alternate-even-row-color']/child::infront-table/child::div/child::div[@class='cell-table-wrapper']/child::div[@class='cell-flex-list-wrapper table']/child::div[@class='cell-flex-list  cell-flex-list--body']/child::div[@class='cell-flex-list__row-wrapper']/child::div[@id='DIV40']/child::div[@class='cell-arrow  cell-arrow--down  cell-flex-list__expand-icon']") #.send_keys('\n')
#Elements = driver_Link.find_elements_by_xpath("//div[@class='cell-arrow  cell-arrow--down  cell-flex-list__expand-icon']")
Elements = driver_Link.find_elements_by_xpath("//div[@class='cell-flex-list  cell-flex-list--body']/div")

for Element in Elements:
        #for Elem in reversed(Element.find_elements_by_xpath('//div[@class="cell-flex-list__row  cell-flex-list__row--main-fields cell-row--interaction"]')):
    for Elem in Element.find_elements_by_xpath('//div[@class="cell-flex-list__row  cell-flex-list__row--main-fields cell-row--interaction"]'):
##########################################
#Open Div
##########################################
        ActionChains(driver_Link).move_to_element_with_offset(Elem,2,2).click().perform()
        time.sleep(2)
##########################################
#Get ISIN
##########################################

        Faktablad = Elem.find_element_by_xpath("//ul[@class='link-list']/child::li[2]/child::a")
        Faktablad2 = Faktablad.get_attribute("href")
        CharToFind = '_'
        CharIsAt = Faktablad2.index(CharToFind, 37)
        ISIN = Faktablad2[37:CharIsAt]
        print(ISIN)
        time.sleep(2)
##########################################
#Close div again
#########################################
        ActionChains(driver_Link).move_to_element_with_offset(Elem, 2, 2).click().perform()
        time.sleep(3)

###############################################
# Write to file
###############################################
        Source = "SEB"
        if len(ISIN) == 12:
            Company.write("%s" %ISIN + "@" + "%s" %Source + '\r\n')

driver_Link.quit()
