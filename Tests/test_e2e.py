import time

import pytest

from appium.webdriver.common.appiumby import AppiumBy

from PageObject.Analysis import Analysis
from PageObject.Cancel import Cancel
from PageObject.FreeExit import FE
from PageObject.Issuance import TicketIssue
from PageObject.Logout import Logout
from PageObject.PaidExit import PE
from PageObject.Refund import Refund
from PageObject.Replacement import Replace
from PageObject.TicketId import View
from TestData.ReplaceData import Replace_Data
from TestData.issuanceData import IssuanceData
from TestData.newIssuanceex import IssuanceEXData
from Utilities.BaseClass import BaseClass



class TestOne(BaseClass):

    temp=""
    shiftId=""

    @pytest.mark.default
    def test_login(self):


        self.verify_element_presence( "ID","com.example.punemetrotom:id/txtUsername")

        log=self.getLogger()
        log.info("To check Login")
        loginUsername = self.driver.find_element(AppiumBy.ID, "com.example.punemetrotom:id/txtUsername")
        loginUsername.send_keys("10001")
        self.verify_element_presence("ID", "com.example.punemetrotom:id/txtPassword")
        loginPWD = self.driver.find_element(AppiumBy.ID, "com.example.punemetrotom:id/txtPassword")
        loginPWD.send_keys("10001")
        loginBTN = self.driver.find_element(AppiumBy.ID, "com.example.punemetrotom:id/btnLogin")
        loginBTN.click()
        self.verify_element_presence("ID", "com.example.punemetrotom:id/editText_stock_qr_added")
        print("Login is successfull")

    @pytest.mark.default
    def test_shift(self):
        shift=self.driver.find_element(AppiumBy.ID, "com.example.punemetrotom:id/txtShiftId")
        print(shift.text)
        shiftstring =str(shift.text)
        TestOne.shiftId = shiftstring.split(":")[1].replace(" ","")

    @pytest.mark.default
    def test_stock(self):
        log = self.getLogger()
        log.info("To check stock management")
        TestOne.temp =self.create_excel(TestOne.shiftId)
        enterStock = self.driver.find_element(AppiumBy.ID, "com.example.punemetrotom:id/editText_stock_qr_added")
        enterStock.send_keys("500")
        updateButton = self.driver.find_element(AppiumBy.ID, "com.example.punemetrotom:id/button_stock_qr_update")
        updateButton.click()
        enterChangeMoney = self.driver.find_element(AppiumBy.ID, "com.example.punemetrotom:id/editText_stock_money_added")
        enterChangeMoney.send_keys("1000")
        chnageMoneyUpdate = self.driver.find_element(AppiumBy.ID, "com.example.punemetrotom:id/button_stock_money_update")
        chnageMoneyUpdate.click()
        confirm = self.driver.find_element(AppiumBy.ID, "com.example.punemetrotom:id/button_stock_update")
        confirm.click()

    isssue =IssuanceEXData()
    @pytest.fixture(params=isssue.conv_dict("issuance"))
    def getData(self, request):
        return request.param
    @pytest.mark.issuance
    def test_issue(self,getData):
        log = self.getLogger()
        log.info("Issuing " + str(getData["Type"]) + " ticket from Vanaz  to " + str(getData["Dstn"]) + " of Qty "  + str(getData["Qty"]) + " by " + str(getData["Mode"] + "amounting RS " + str(getData["Amt"]) ) )
        Ticket_issuance =   TicketIssue(self.driver)
        status = Ticket_issuance.test_ticket(getData)
        if status:
            self.open_write_excel(TestOne.temp,getData)
        #View_id= View(self.driver)
        #View_id.view_tic()
        #Ticket_cancel = Cancel(self.driver)
        #Ticket_cancel.cancel_tic()

    @pytest.fixture(params=isssue.conv_dict("cancel"))
    def getDataCan(self, request):
        return request.param
    @pytest.mark.cancel
    def test_cancel(self,getDataCan):
        log = self.getLogger()
        log.info(
            "Issuing " + str(getDataCan["Type"]) + " ticket from Vanaz  to " + str(getDataCan["Dstn"]) + " of Qty " + str(
                getDataCan["Qty"]) + " by " + str(getDataCan["Mode"] + "amounting RS " + str(getDataCan["Amt"])))

        Ticket_issuance = TicketIssue(self.driver)
        status = Ticket_issuance.test_ticket(getDataCan)
        if status:
            getDataCan["flow"] = "issuance"
            self.open_write_excel(TestOne.temp, getDataCan)
        Ticket_cancel = Cancel(self.driver)
        status = Ticket_cancel.cancel_tic()
        if status:
            getDataCan["flow"]="Cancelation"
            self.open_write_excel(TestOne.temp, getDataCan)

    re=Replace_Data()
    @pytest.fixture(params=  re.conv_dict("replace"))
    def getData1(self, request):
        return request.param
    @pytest.mark.replace
    def test_replace(self,getData1):
        replace= Replace(self.driver)
        status =replace.replace_tic(getData1)
        if status:
            getData1["flow"]="Replacement"
            self.open_write_excel(TestOne.temp, getData1)

    @pytest.fixture(params=re.conv_dict("analyse"))
    def getData3(self, request):
        return request.param

    @pytest.mark.analysis
    def test_analyse(self, getData3):
        analyse = Analysis(self.driver)
        status = analyse.analyse_tic(getData3)
        if status:
            getData3["flow"] = "Analysis"
            self.open_write_excel(TestOne.temp, getData3)


    @pytest.fixture(params=re.conv_dict("refund"))
    def getData2(self, request):
        return request.param
    @pytest.mark.refund
    def test_refund(self, getData2):
        refund = Refund(self.driver)
        status = refund.refund_tic(getData2)
        if status:
            getData2["flow"] = "Refund"
            self.open_write_excel(TestOne.temp, getData2)

    @pytest.fixture(params=re.conv_dict("PE"))
    def getDataPE(self, request):
        return request.param

    @pytest.mark.pe
    def test_pe(self,getDataPE):
        pe=PE(self.driver)
        status = pe.paid_exit(getDataPE)
        if status:
            getDataPE["flow"] = "PE"
            self.open_write_excel(TestOne.temp, getDataPE)

    @pytest.fixture(params=re.conv_dict("FE"))
    def getDataFE(self, request):
        return request.param

    @pytest.mark.fe
    def test_fe(self, getDataFE):
        fe = FE(self.driver)
        status = fe.free_exit(getDataFE)
        if status:
            getDataFE["flow"] = "FE"
            self.open_write_excel(TestOne.temp, getDataFE)

    @pytest.mark.logout
    def test_logout(self):
        logout =Logout(self.driver)
        logout.do_logout()



