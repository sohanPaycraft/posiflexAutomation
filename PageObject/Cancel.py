import pytest
import time

from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from TestData.issuanceData import IssuanceData

class Cancel:
    def __init__(self, driver):
        self.driver =  driver

    def cancel_tic(self,x):
        time.sleep(1)
        m = self.driver.find_element(AppiumBy.XPATH,"//androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[7]")
        m.click()
        time.sleep(1)


        select_all= self.driver.find_element(AppiumBy.ID ,"com.example.punemetrotom:id/checkboxSelectAll")
        select_all.click()
        ticketid = self.driver.find_elements(AppiumBy.ID, "com.example.punemetrotom:id/txtTicketSrlNum")
        for ticket in ticketid:
            print(ticket.text)
        cancel_btn= self.driver.find_element(AppiumBy.ID ,"com.example.punemetrotom:id/btn_cancel")
        time.sleep(1)
        cancel_btn.click()
        time.sleep(1)
        yes_cancel= self.driver.find_element(AppiumBy.ID ,"com.example.punemetrotom:id/yesCancel")
        yes_cancel.click()
        time.sleep(1)
        print(self.driver.find_element(AppiumBy.ID ,"com.example.punemetrotom:id/txtSuccess"))
        succesTxtissue=self.driver.find_element(AppiumBy.ID, "com.example.punemetrotom:id/txtSuccess")
        #assert "successfully" in succesTxtissue.text

        #rec_pr =self.driver.find_element(AppiumBy.ID ,"com.example.punemetrotom:id/button_print")
        #rec_pr.click()
        if x == 1:

            print_rec = self.driver.find_element(AppiumBy.ID, "com.example.punemetrotom:id/button_print")
        else:
            print_rec = self.driver.find_element(AppiumBy.ID, "com.example.punemetrotom:id/button_skip")

        print_rec.click()
        return True
        #selects= self.driver.find_elements(AppiumBy.ID ,"com.example.punemetrotom:id/btn_cancel")



