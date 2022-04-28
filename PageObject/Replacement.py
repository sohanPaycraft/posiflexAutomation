import pytest
import time

from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from TestData.issuanceData import IssuanceData

class Replace:
    def __init__(self, driver):
        self.driver =  driver

    def replace_tic(self,getData):
        time.sleep(1)
        h=self.driver.find_element(AppiumBy.ID, "com.example.punemetrotom:id/imgPuneMetroLogo")
        h.click()


        time.sleep(1)
        m = self.driver.find_element(AppiumBy.XPATH,"//androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[6]")
        m.click()
        time.sleep(1)
        wait = WebDriverWait(self.driver, 60)
        replace_tic = self.driver.find_element(AppiumBy.ID, "com.example.punemetrotom:id/editText_ticket_id")
        replace_tic.send_keys(getData['Ticket'])
        time.sleep(1)
        confirm_btn = self.driver.find_element(AppiumBy.ID, "com.example.punemetrotom:id/btnIssueReplacement")
        confirm_btn.click()
        time.sleep(2)

        try:

            self.driver.find_element(AppiumBy.ID, "com.example.punemetrotom:id/button_go_to_home_screen").click()


        except  Exception as e:
            print(e)
        else:
            assert "a" in "b"

        wait.until(EC.presence_of_element_located((AppiumBy.ID, "com.example.punemetrotom:id/btnReplace")))
        type = self.driver.find_element(AppiumBy.ID, "com.example.punemetrotom:id/txtTicketTypeValue").text.split("-")[1]
        getData["Type"] = type
        replace_btn= self.driver.find_element(AppiumBy.ID, "com.example.punemetrotom:id/btnReplace")
        replace_btn.click()
        time.sleep(1)
        cash_reveived=self.driver.find_element(AppiumBy.ID, "com.example.punemetrotom:id/edtCashReceived")
        Amount_temp = self.driver.find_element(AppiumBy.ID, "com.example.punemetrotom:id/totalAmountValue").text
        Amount = Amount_temp[1:len(Amount_temp) - 3]
        getData["Amt"] = Amount
        if getData["Mode"] == "Cash":
            amtTab= self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,'text("Cash")')
            amtTab.click()

            cash_reveived.send_keys(Amount)
        elif getData["Mode"] == "Card":
            amtTab = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'text("Card")')
            amtTab.click()
            enterRRN= self.driver.find_element(AppiumBy.ID, "com.example.punemetrotom:id/editText_rrn_number")
            enterRRN.send_keys("123456789012")
        else:
            amtTab = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'text("UPI")')
            amtTab.click()
            enterUPI = self.driver.find_element(AppiumBy.ID, "com.example.punemetrotom:id/editText_rrn_number")
            enterUPI.send_keys("1111")


        pay_btn = self.driver.find_element(AppiumBy.ID, "com.example.punemetrotom:id/btn_pay")
        pay_btn.click()
        wait.until(EC.presence_of_element_located((AppiumBy.ID, "com.example.punemetrotom:id/txtSuccess")))
        if getData["Receipt"] == 1:

            print_rec = self.driver.find_element(AppiumBy.ID, "com.example.punemetrotom:id/button_print")
        else:
            print_rec = self.driver.find_element(AppiumBy.ID, "com.example.punemetrotom:id/button_skip")
        print_rec.click()
        time.sleep(1)
        return True






