from datetime import datetime

import pytest
import time

from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from TestData.issuanceData import IssuanceData

class FE:
    def __init__(self, driver):
        self.driver =  driver

    def free_exit(self,getData):
        time.sleep(1)
        h = self.driver.find_element(AppiumBy.ID, "com.example.punemetrotom:id/imgPuneMetroLogo")
        h.click()


        time.sleep(1)
        m = self.driver.find_element(AppiumBy.XPATH,"//androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[8]")
        m.click()
        time.sleep(1)
        wait = WebDriverWait(self.driver, 60)
        tick_id=self.driver.find_element(AppiumBy.ID, "com.example.punemetrotom:id/editText_ticket_id")
        tick_id.send_keys(getData['Ticket'])
        time.sleep(1)
        pe_btn=self.driver.find_element(AppiumBy.ID, "com.example.punemetrotom:id/btnIssuePaidFreeExit")
        pe_btn.click()
        time.sleep(1)
        try:

            self.driver.find_element(AppiumBy.ID, "com.example.punemetrotom:id/button_go_to_home_screen").click()


        except  Exception as e:
            print(e)
        else:
            self.driver.save_screenshot(str("fe"+str(datetime.now()))+".png")
            assert "a" in "b"
        time.sleep(2)
        wait.until(EC.presence_of_element_located((AppiumBy.ID, "com.example.punemetrotom:id/btn_pay")))
        btn = self.driver.find_element(AppiumBy.ID, "com.example.punemetrotom:id/btn_pay")
        btn.click()
        time.sleep(1)
        wait.until(EC.presence_of_element_located((AppiumBy.ID, "com.example.punemetrotom:id/txtSuccess")))
        print_rec = self.driver.find_element(AppiumBy.ID, "com.example.punemetrotom:id/button_print")
        print_rec.click()
        time.sleep(1)
        getData["Amt"] = "0"
        return True

