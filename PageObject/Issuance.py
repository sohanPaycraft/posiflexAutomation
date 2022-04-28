import pytest
import time

from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from TestData.issuanceData import IssuanceData




class TicketIssue():

    def __init__(self, driver):
        self.driver =  driver



    def test_ticket(self,getData):
        time.sleep(1)
        h = self.driver.find_element(AppiumBy.ID, "com.example.punemetrotom:id/imgPuneMetroLogo")
        h.click()


        time.sleep(1)
        m = self.driver.find_element(AppiumBy.XPATH,"//androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[2]")
        m.click()
        wait = WebDriverWait(self.driver, 60)
        wait.until(EC.presence_of_element_located((AppiumBy.ID, "com.example.punemetrotom:id/txtAlphabet")))
        alphas = self.driver.find_elements(AppiumBy.ID, "com.example.punemetrotom:id/txtAlphabet")
        for alp in alphas:

            if alp.text == getData["Alphabet"]:
                alp.click()
                break
        wait.until(EC.presence_of_element_located((AppiumBy.ID, "com.example.punemetrotom:id/textDestinationStation")))
        dstn = self.driver.find_element(AppiumBy.ID, "com.example.punemetrotom:id/textDestinationStation")
        dstn.click()
        if getData["Type"] == "SJT":
            tickType = self.driver.find_element(AppiumBy.ID, "com.example.punemetrotom:id/btnSJT")
        elif getData["Type"] == "RJT":
            tickType = self.driver.find_element(AppiumBy.ID, "com.example.punemetrotom:id/btnRJT")
        else:
            tickType = self.driver.find_element(AppiumBy.ID, "com.example.punemetrotom:id/btnGroup")
            getData['Qty']=1
        tickType.click()

        TickIncr = self.driver.find_element(AppiumBy.ID, "com.example.punemetrotom:id/txtQuantityIncrement")
        ticks= int(getData["Qty"])
        for a in range(1,ticks):
            TickIncr.click()

        payConfirm = self.driver.find_element(AppiumBy.ID, "com.example.punemetrotom:id/btnConfirm")
        payConfirm.click()
        wait.until(EC.presence_of_element_located((AppiumBy.ID, "com.example.punemetrotom:id/txtTotalAmount")))
        enterCash = self.driver.find_element(AppiumBy.ID, "com.example.punemetrotom:id/edtCashAmount")
        Amount_temp = self.driver.find_element(AppiumBy.ID, "com.example.punemetrotom:id/txtTotalAmount").text
        Amount = Amount_temp[1:len(Amount_temp) - 3]
        getData["Amt"] = Amount
        if getData["Mode"] == "Cash":
            amtTab= self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,'text("Cash")')
            amtTab.click()

            enterCash.send_keys(Amount)
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



        pay = self.driver.find_element(AppiumBy.ID, "com.example.punemetrotom:id/btnPay")
        pay.click()
        time.sleep(2)
        try:

            self.driver.find_element(AppiumBy.ID, "com.example.punemetrotom:id/button_go_to_home_screen").click()


        except  Exception as e:
            print(e)
        else:
            assert "a" in "b"
        wait.until(EC.presence_of_element_located((AppiumBy.ID, "com.example.punemetrotom:id/txtSuccess")))

        print(getData["Receipt"])
        if getData["Receipt"] == 1:

            print_rec = self.driver.find_element(AppiumBy.ID, "com.example.punemetrotom:id/button_print")
        else:
            print_rec = self.driver.find_element(AppiumBy.ID, "com.example.punemetrotom:id/button_skip")
        print_rec.click()
        time.sleep(1)
        return  True

