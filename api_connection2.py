from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from webdriver_manager.chrome import ChromeDriverManager

# pagina web
url = "https://www-scopus-com.uchile.idm.oclc.org/search/form.uri?display=basic#basic"
def open_web_page(link):
    try_again = None
    try:
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get(link)
    except:
        try_again = True
    return driver, try_again

# ingreso cuenta universidad
def login_university_user(driver,university_user, university_password):
    try_again = None
    try:
        driver.find_element_by_xpath('//input[@name="user"]').send_keys(university_user)
        driver.find_element_by_xpath('//input[@name="pass"]').send_keys(university_password)
        driver.find_element_by_class_name("button").click()
    except:
        try_again = True
    return driver, try_again

import time
# login cuenta personal
def login_scorpus_account(driver, personal_mail, personal_password):
    try_again = None
    try:
        notnow=driver.find_elements_by_xpath("//*[starts-with(text(), 'Sign in')]")
        notnow[0].click()
        
        time.sleep(7) # Sleep for 3 seconds

        driver.find_element_by_xpath("//*[@aria-labelledby='emaillabel emailerror']").send_keys(personal_mail)
        driver.find_element_by_id("bdd-elsPrimaryBtn").click()
        time.sleep(7)
        driver.find_element_by_id("bdd-password").send_keys(personal_password)
        driver.find_element_by_id("bdd-elsPrimaryBtn").click()
    except:
        try_again = True
    return driver, try_again
# realizar busqueda
def query(driver):
    try_again = None
    try:
        driver.get("https://www-scopus-com.uchile.idm.oclc.org/results/results.uri?sort=plf-f&src=s&searchTerms=handling+dewatering%3f%21%22*%24&sid=debe611e57e8db86b776cc29f1dbcfc7&sot=b&sdt=b&sl=95&s=%28TITLE-ABS-KEY%28tailings%29+OR+TITLE-ABS-KEY%28mine+tailings%29+OR+TITLE-ABS-KEY%28handling+dewatering%29%29&origin=searchhistory&txGid=d4a2e4abc9847171abf42d5d91598041")
    except:
        try_again = True
    return driver, try_again

# filtrando por tipo de investigacion
def filter_type_research(driver, type_feald):
    try_again = None
    try:
        driver.find_elements_by_xpath("//*[@id='viewAllLink_SUBJAREA']/span[contains(text(), 'View all')]")[0].click()
        time.sleep(7)
        driver.find_elements_by_xpath("//*/ul[@class='refineResults col-xs-3 overlayUL']/li/label[@class='checkbox-label' and @for='cat_" + type_feald + "']")[0].click()
        driver.find_elements_by_xpath("//*[@class='btn btn-primary btn-sm btnLmtExcEnable' and @value='Limit to']")[0].click()
    except:
        try_again = False
    return driver, try_again

# filtrando por año
def filter_year(driver, year):
    try_again = None
    try:
        driver.find_elements_by_xpath("//*[@id='viewAllLink_PUBYEAR']/span[contains(text(), 'View all')]")[0].click()
        time.sleep(7)
        driver.find_elements_by_xpath("//*/ul[@class='refineResults col-xs-3 overlayUL']/li/label[@class='checkbox-label' and @for='cat_" + year +"']")[0].click()
        driver.find_elements_by_xpath("//*[@class='btn btn-primary btn-sm btnLmtExcEnable' and @value='Limit to']")[0].click()
    except:
        try_again = False
    return driver, try_again

import os
import shutil
# descargar datos ya filtrados
def download_data(driver, type_feald, year):
    try_again = None
    try:
        time.sleep(7)
        driver.find_elements_by_xpath("//*[@id='mainResults-allPageSelectedValue']")[0].click()
        driver.find_elements_by_xpath("//*[@for='mainResults-selectAllTop']")[0].click()
        driver.find_elements_by_xpath("//*[contains(text(), 'CSV export')]")[0].click()

        Initial_path = "C:/Users/joaqu/Downloads"

        import os.path
        file_path = "C:/Users/joaqu/Downloads/scopus.csv"
        while not os.path.exists(file_path):
            time.sleep(10)

        name_file = type_feald + "_" + year

        if os.path.isfile(file_path):
            filename = max([Initial_path + "\\" + f for f in os.listdir(Initial_path)],key=os.path.getctime)
            shutil.move(filename, Initial_path + "/" + name_file + ".csv")
    except:
        try_again = False
    return driver, try_again

def search_concept_by_feald_or_year(link, university_user, university_password, personal_mail, personal_password, type_feald, year):
    driver, try_again = open_web_page(link)
    if try_again == True:
        driver.close()
        return "again"
    elif try_again == False:
        driver.close()
        return "not again"
    driver, try_again = login_university_user(driver,university_user, university_password)
    if try_again == True:
        driver.close()
        return "again"
    elif try_again == False:
        driver.close()
        return "not again"
    driver, try_again = login_scorpus_account(driver, personal_mail, personal_password)
    if try_again == True:
        driver.close()
        return "again"
    elif try_again == False:
        driver.close()
        return "not again"
    driver, try_again = query(driver)
    if try_again == True:
        driver.close()
        return "again"
    elif try_again == False:
        driver.close()
        return "not again"
    driver, try_again = filter_type_research(driver, type_feald)
    if try_again == True:
        driver.close()
        return "again"
    elif try_again == False:
        driver.close()
        return "not again"
    driver, try_again = filter_year(driver, year)
    if try_again == True:
        driver.close()
        return "again"
    elif try_again == False:
        driver.close()
        return "not again"
    driver, try_again = download_data(driver, type_feald, year)
    if try_again == True:
        driver.close()
        return "again"
    elif try_again == False:
        driver.close()
        return "not again"
    driver.close()
    return "null"

# queries = [
#     "handling dewatering", 
#     # "emphasizing", 
#     "mine tailings"
#     ]
years = [
    # "2010", 
    # "2011", 
    # "2012", 
    # "2013", 
    # "2014", 
    # "2015", 
    # "2016", 
    # "2017", 
    # "2018", 
    # "2019", 
    "2020"
    ]
fealds = [
    # "AGRI",
    # "ARTS", 
    # "BIOC", 
    # "BUSI", 
    # "CENG", 
    # "CHEM", 
    # "COMP", 
    # "DECI", 
    # "DENT", 
    # "EART", 
    # "ECON", 
    "ENER",
    "ENGI",
    "ENVI",
    "HEAL",
    "IMMU",
    "MATE",
    "MATH",
    "MEDI",
    "NEUR",
    "NURS",
    "PHAR",
    "PHYS",
    "PSYC",
    "SOCI",
    "VETE",
    "MULT"
    ]

def loop_downloads():
    for y in years:
        for f in fealds:
            string_try_again = "again"
            while string_try_again == "again":
                string_try_again = search_concept_by_feald_or_year(link = url, university_user = "UNIVERSITY_USER", university_password = "PASSWORD",personal_mail = "PERSONAL_EMAIL", personal_password = "PERSONAL_PASSWORD", type_feald = f, year = y)

def simple_try(f, y):
    string_try_again = search_concept_by_feald_or_year(link = url, university_user = "UNIVERSITY_USER", university_password = "UNIVERSITY_PASSWORD",personal_mail = "PERSONAL_EMAIL", personal_password = "PERSONAL_PASSWORD", type_feald = f, year = y)

def run():
    loop_downloads()
    # simple_try(y = "2010", f = "ECON")

if __name__ == "__main__":
    run()