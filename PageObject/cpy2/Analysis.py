import pytest
import time

from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from TestData.issuanceData import IssuanceData

class Analysis:
    def __init__(self, driver):
        self.driver =  driver

    def analyse_tic(self,getData):
        time.sleep(1)
        h = self.driver.find_element(AppiumBy.ID, "com.example.punemetrotom:id/imgPuneMetroLogo")
        h.click()


        time.sleep(1)
        m = self.driver.find_element(AppiumBy.XPATH,"//androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[4]")
        m.click()
        wait = WebDriverWait(self.driver, 60)
        time.sleep(1)
        enterTick = self.driver.find_element(AppiumBy.ID, "com.example.punemetrotom:id/edtTicketId")
        enterTick.send_keys(getData["Ticket"])

        time.sleep(1)
        confirmBtn= self.driver.find_element(AppiumBy.ID, "com.example.punemetrotom:id/btnConfirmAnalysis")
        confirmBtn.click()
        time.sleep(1)
        try:

            self.driver.find_element(AppiumBy.ID, "com.example.punemetrotom:id/button_go_to_home_screen").click()


        except  Exception as e:
            print(e)
        else:
            assert "a" in "b"
        wait.until(EC.presence_of_element_located((AppiumBy.ID, "com.example.punemetrotom:id/btnAdjust")))
        type = self.driver.find_element(AppiumBy.ID, "com.example.punemetrotom:id/txtTicketTypeValue").text.split("-")[
            1]
        getData["Type"] = type
        adjust_btn = self.driver.find_element(AppiumBy.ID, "com.example.punemetrotom:id/btnAdjust")
        unpaid= self.driver.find_element(AppiumBy.ID, "com.example.punemetrotom:id/radio_btn_unpaid")

        Amount=0
        if adjust_btn.is_enabled():
            adjust_btn.click()
            time.sleep(1)
            cash_received= self.driver.find_element(AppiumBy.ID, "com.example.punemetrotom:id/edtCashAmount")
            if getData["Mode"] == "Cash":
                amtTab = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'text("Cash")')
                amtTab.click()
                Amount_temp = self.driver.find_element(AppiumBy.ID, "com.example.punemetrotom:id/txtTotalAmount").text
                Amount = Amount_temp[1:len(Amount_temp) - 3]

                time.sleep(1)
                cash_received.send_keys(Amount)
            elif getData["Mode"] == "Card":
                amtTab = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'text("Card")')
                amtTab.click()
                enterRRN = self.driver.find_element(AppiumBy.ID, "com.example.punemetrotom:id/editText_rrn_number")
                time.sleep(1)
                enterRRN.send_keys("123456789012")
                Amount_temp = self.driver.find_element(AppiumBy.ID, "com.example.punemetrotom:id/txtTotalAmount").text
                Amount = Amount_temp[1:len(Amount_temp) - 3]
            else:
                amtTab = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'text("UPI")')
                amtTab.click()
                enterUPI = self.driver.find_element(AppiumBy.ID, "com.example.punemetrotom:id/editText_rrn_number")
                time.sleep(1)
                enterUPI.send_keys("1111")
                Amount_temp = self.driver.find_element(AppiumBy.ID, "com.example.punemetrotom:id/txtTotalAmount").text
                Amount = Amount_temp[1:len(Amount_temp) - 3]
            time.sleep(1)
            pay=self.driver.find_element(AppiumBy.ID, "com.example.punemetrotom:id/btnPayAnalysis")
            pay.click()
        else:
            unpaid.click()
            time.sleep(1)
            assert adjust_btn.is_enabled()
            adjust_btn.click()
            time.sleep(1)
            pay = self.driver.find_element(AppiumBy.ID, "com.example.punemetrotom:id/btnPayAnalysis")
            pay.click()
        wait.until(EC.presence_of_element_located((AppiumBy.ID, "com.example.punemetrotom:id/txtSuccess")))
        getData["Amt"] = Amount
        succesTxtissue = self.driver.find_element(AppiumBy.ID, "com.example.punemetrotom:id/txtSuccess")
        print(succesTxtissue.text)
        # assert succesTxtissue.text == "Payment received and QR ticket issued successfully!"
        #assert "successfully" in succesTxtissue.text

        print_rec = self.driver.find_element(AppiumBy.ID, "com.example.punemetrotom:id/button_print")
        print_rec.click()
        time.sleep(1)
        return True




