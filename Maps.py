
from selenium import webdriver
from time import sleep

driver = webdriver.Chrome("D:\chromedriver_win32\chromedriver.exe") 
driver.get("https://www.google.com/maps/@12.994185,75.3295565,15z")
sleep(2)

def searchplace():
    place=driver.find_element_by_id("searchboxinput")
    place.send_keys("ujire")
    Submit=driver.find_element_by_xpath("//*[@id='searchbox-searchbutton']")
    Submit.click()
searchplace()    


def directions():
    sleep(10)
    directions=driver.find_element_by_xpath("/html/body/div[3]/div[9]/div[8]/div/div[1]/div/div/div[4]/div[1]/button/span")

    directions.click()
directions()    

def find():
    # sleep(10)
    find= driver.find_element_by_xpath("/html/body/div[3]/div[9]/div[8]/div/div[1]/div")
    find.send_keys("ujire")
    # sleep(10)
    search=driver.find_elements_by_xpath("/html/body/div[3]/div[9]/div[3]/div[1]/div[2]/div/div[3]/div[1]/div[1]/div[2]/button[1]")
    search.click()
find()

def kilometers():
    sleep(2)
    Totalkm=driver.find_element_by_xpath("/html/body/div[3]/div[9]/div[8]/div/div[1]/div/div/div[4]/div[1]/div/div[1]/div[1]/div[2]/div")
    print("Total Km by NH", Totalkm.text)
    sleep(2)
    train=driver.find_element_by_xpath("/html/body/div[3]/div[9]/div[8]/div/div[1]/div/div/div[4]/div[2]/div/div[2]/div[1]/div")
    print("Time by Train: ", train)
    sleep(2 )
    walk=driver.find_element_by_xpath("/html/body/div[3]/div[9]/div[8]/div/div[1]/div/div/div[4]/div[1]/div/div[3]/div[1]/div[2]")
    print("By walk Km ",walk)
    car=driver.find_element_by_xpath("/html/body/div[3]/div[9]/div[8]/div/div[1]/div/div/div[2]/div[2]/div[1]/h1/span[1]/span[2]/span")
    print("By car Km: ", car)
kilometers()    