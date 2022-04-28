import pytest
import time

from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from TestData.issuanceData import IssuanceData

class PE:
    def __init__(self, driver):
        self.driver =  driver

    def paid_exit(self,getData):
        time.sleep(1)
        m = self.driver.find_element(AppiumBy.XPATH,"//androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[8]")
        m.click()
        time.sleep(1)
        wait = WebDriverWait(self.driver, 60)
        pe_btn=self.driver.find_element(AppiumBy.ID, "com.example.punemetrotom:id/btn_paid_exit")
        pe_btn.click()
        time.sleep(1)
        print(getData["Type"])
        if getData["Type"]=="Tailgating Passenger":
            tg= self.driver.find_element(AppiumBy.ID, "com.example.punemetrotom:id/radio_btn_paid_tailgating")
            tg.click()
        else:
            tg = self.driver.find_element(AppiumBy.ID, "com.example.punemetrotom:id/radio_btn_paid_ticketless")
            tg.click()

        time.sleep(1)
        issue_btn =self.driver.find_element(AppiumBy.ID, "com.example.punemetrotom:id/btnIssuePaidFreeExit")
        issue_btn.click()
        time.sleep(1)

        Amount_temp = self.driver.find_element(AppiumBy.ID, "com.example.punemetrotom:id/totalAmount").text
        Amount = Amount_temp[1:len(Amount_temp) - 3]
        if getData["Mode"] == "Cash":
            amtTab= self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,'text("Cash")')
            amtTab.click()
            time.sleep(1)
            cash_reveived = self.driver.find_element(AppiumBy.ID, "com.example.punemetrotom:id/edtCashAmount")
            cash_reveived.send_keys(Amount)

        elif getData["Mode"] == "Card":
            amtTab = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'text("Card")')
            amtTab.click()
            time.sleep(1)
            enterRRN= self.driver.find_element(AppiumBy.ID, "com.example.punemetrotom:id/editText_rrn_number")
            enterRRN.send_keys("123456789012")
        else:
            amtTab = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'text("UPI")')
            amtTab.click()
            time.sleep(1)
            enterUPI = self.driver.find_element(AppiumBy.ID, "com.example.punemetrotom:id/editText_rrn_number")
            enterUPI.send_keys("1111")

        getData["Amt"] = Amount

        time.sleep(1)
        pe_btn = self.driver.find_element(AppiumBy.ID, "com.example.punemetrotom:id/btn_pay")
        pe_btn.click()
        time.sleep(1)
        wait.until(EC.presence_of_element_located((AppiumBy.ID, "com.example.punemetrotom:id/txtSuccess")))
        if getData["Receipt"] == 1:

            print_rec = self.driver.find_element(AppiumBy.ID, "com.example.punemetrotom:id/button_print")
        else:
            print_rec = self.driver.find_element(AppiumBy.ID, "com.example.punemetrotom:id/button_skip")
        print_rec.click()
        time.sleep(1)
        return True


