#########################################
##Import needed libraries
#########################################
from selenium import webdriver
import time #To be able to sleep
from datetime import datetime
import codecs #To be able to write the file

#########################################
## Settings, create connection to Chrome and set timeout
#########################################
driver_Fund = webdriver.Chrome("C:\\Users\\clman\\Documents\\Funds\\chromedriver.exe")
driver_Fund.set_page_load_timeout(30)

#########################################
##Static paths and variables
#########################################
static1 = "https://secust.msse.se/se/nordnetny/funds/overview.aspx?cid="
static2 = "&cntry=SE"
vDate = datetime.now().strftime("%Y-%m-%d")


#########################################
## Create empty file so we can write to it later
#########################################
Nordnet = codecs.open(r'W:\Martin\Nordnet\Funds.txt', 'w', 'utf-8')
texttowrite = 'ID@TotalFee@FundFee@Category@ISIN@Morningstar@Risk@1Week@1Month@6Months@1Year@3Years@5Years'
Nordnet.write(texttowrite + '\r\n')

#########################################
## Get IDs to read
#########################################
with codecs.open('C:/Users/clman/Documents/Funds/Nordnet/ID.txt', 'r', encoding='utf-8') as Funds:
    for Fund in Funds:
        Fund2 = Fund.strip()
        driver_Fund.get(static1 + Fund2 + static2)
#        time.sleep(1)
        print(static1 + Fund2 + static2)


########################################
# Get data
########################################

        PreISIN = driver_Fund.find_element_by_xpath("/html/body/div/div[2]/div[3]/div[5]/table[2]/tbody/tr/td[2]")
        ISIN = PreISIN.text
#        print(ISIN)

        PreW1 = driver_Fund.find_element_by_xpath("/html/body/div/div[2]/div[3]/div[1]/table/tbody/tr[2]/td[2]")
        W1 = PreW1.text
#        print(W1)

        PreM1 = driver_Fund.find_element_by_xpath("/html/body/div/div[2]/div[3]/div[1]/table/tbody/tr[3]/td[2]")
        M1 = PreM1.text
#        print(M1)

        PreM6 = driver_Fund.find_element_by_xpath("/html/body/div/div[2]/div[3]/div[1]/table/tbody/tr[4]/td[2]")
        M6 = PreM6.text
#        print(M6)

        PreY1 = driver_Fund.find_element_by_xpath("/html/body/div/div[2]/div[3]/div[1]/table/tbody/tr[5]/td[2]")
        Y1 = PreY1.text
 #       print(Y1)

        PreY3 = driver_Fund.find_element_by_xpath("/html/body/div/div[2]/div[3]/div[1]/table/tbody/tr[6]/td[2]")
        Y3 = PreY3.text
#        print(Y3)

        PreY5 = driver_Fund.find_element_by_xpath("/html/body/div/div[2]/div[3]/div[1]/table/tbody/tr[7]/td[2]")
        Y5 = PreY5.text
#        print(Y5)

        PreFundFee = driver_Fund.find_element_by_xpath("/html/body/div/div[2]/div[3]/div[4]/table/tbody/tr[3]/td[2]")
        FundFee = PreFundFee.text
#        print(FundFee)

        PreTotalFee = driver_Fund.find_element_by_xpath("/html/body/div/div[2]/div[3]/div[4]/table/tbody/tr[5]/td[2]")
        TotalFee = PreTotalFee.text
#        print(TotalFee)

        PreRisk = driver_Fund.find_element_by_xpath("/html/body/div/div[2]/div[3]/div[2]/div[2]/img").get_attribute("src")
        PreRisk2 = PreRisk[-5:]
        Risk = PreRisk2[:1]
#        print(Risk)

        PreCategory = driver_Fund.find_element_by_xpath("/html/body/div/div[2]/div/table/tbody/tr/td")
        Category = PreCategory.text
#        print(Category)

        PreMorningstar = driver_Fund.find_element_by_xpath("/html/body/div/div[2]/div/table/tbody/tr/td[3]/img").get_attribute("src")
        PreMorningstar2 = PreMorningstar[-5:]
        Morningstar = PreMorningstar2[:1]
 #       print(Morningstar)

################################################
## Write to file
################################################
        Nordnet.write("%s" %Fund2 + "@" + "%s" %TotalFee + "@" + "%s" %FundFee + "@" + "%s" %Category + "@" + "%s" %ISIN + "@" + "%s" %Morningstar + "@" + "%s" %Risk + "@" + "%s" %W1 + "@" + "%s" %M1 + "@" + "%s" %M6 + "@" + "%s" %Y1 + "@" + "%s" %Y3 + "@" + "%s" %Y5 + '\r\n')

driver_Fund.quit()
