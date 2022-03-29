import time

from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from TestData.issuanceData import IssuanceData

class View:
    def __init__(self, driver):
        self.driver =  driver

    def view_tic(self):
        time.sleep(1)
        m = self.driver.find_element(AppiumBy.XPATH,"//androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[7]")
        m.click()
        time.sleep(1)
        ticketid = self.driver.find_elements(AppiumBy.ID, "com.example.punemetrotom:id/txtTicketSrlNum")
        for ticket in ticketid:
            print(ticket.text)