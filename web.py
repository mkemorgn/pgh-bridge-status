"""
This file will be responsible for automatically downloading the latest csv from penndot
"""
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

download_dir = os.getcwd() + "/bridge_data"

fp = webdriver.FirefoxProfile()
fp.set_preference("browser.download.folderList", 2)
fp.set_preference("browser.download.manager.showWhenStarting", False)
fp.set_preference("browser.download.dir", download_dir)
fp.set_preference("browser.helperApps.neverAsk.saveToDisk", "text/csv")


driver = webdriver.Firefox(firefox_profile=fp)
driver.get(
    "https://gis.penndot.gov/paprojects/Reports/BridgeConditionsReport.aspx?aoiType=county&aoiValue=02"
)
driver.find_element(By.XPATH, '//*[@id="body"]/div/div[1]/div[1]/div/i').click()
driver.close()
