import pytest
import time

from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from TestData.issuanceData import IssuanceData

class Refund:
    def __init__(self, driver):
        self.driver =  driver

    def refund_tic(self,getData):
        time.sleep(1)
        h = self.driver.find_element(AppiumBy.ID, "com.example.punemetrotom:id/imgPuneMetroLogo")
        h.click()


        time.sleep(1)
        m = self.driver.find_element(AppiumBy.XPATH,"//androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[5]")
        m.click()
        time.sleep(1)
        wait = WebDriverWait(self.driver, 60)
        refund_tic = self.driver.find_element(AppiumBy.ID, "com.example.punemetrotom:id/edtTicketId")
        refund_tic.send_keys(getData['Ticket'])
        time.sleep(1)
        confirm=  self.driver.find_element(AppiumBy.ID, "com.example.punemetrotom:id/btnConfirmRefund")
        confirm.click()
        time.sleep(2)
        try:

            self.driver.find_element(AppiumBy.ID, "com.example.punemetrotom:id/button_go_to_home_screen").click()


        except  Exception as e:
            print(e)
        else:
            assert "a" in "b"
        wait.until(EC.presence_of_element_located((AppiumBy.ID, "com.example.punemetrotom:id/btnRefund")))
        type=self.driver.find_element(AppiumBy.ID, "com.example.punemetrotom:id/txtTicketTypeValue").text.split("-")[1]
        getData["Type"]=type
        refund_btn=self.driver.find_element(AppiumBy.ID, "com.example.punemetrotom:id/btnRefund")
        assert refund_btn.is_enabled()
        refund_btn.click()
        wait.until(EC.presence_of_element_located((AppiumBy.ID, "com.example.punemetrotom:id/ticketRefundableAmount")))
        Amount_temp = self.driver.find_element(AppiumBy.ID, "com.example.punemetrotom:id/ticketRefundableAmount").text
        Amount_temp= Amount_temp + ".00"
        Amount = Amount_temp[1:len(Amount_temp) - 3]
        print(1)
        print(Amount)
        print(1)
        getData["Amt"] = Amount
        refund_confirm=self.driver.find_element(AppiumBy.ID, "com.example.punemetrotom:id/btnRefund")
        refund_confirm.click()
        wait.until(EC.presence_of_element_located((AppiumBy.ID, "com.example.punemetrotom:id/txtSuccess")))
        print_rec = self.driver.find_element(AppiumBy.ID, "com.example.punemetrotom:id/button_print")
        print_rec.click()
        time.sleep(1)
        return True


