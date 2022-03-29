import time

from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By



desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['automationName'] = 'UiAutomator2'
desired_caps['platformVersion'] = '9'
desired_caps['deviceName'] = 'B2153CC46B'
desired_caps['app'] = ('/home/sohansagar/Downloads/Posi.apk')
desired_caps['noReset'] = "true"
desired_caps['fullReset'] = "false"
desired_caps['appPackage'] = 'com.example.punemetrotom'
desired_caps['appWaitActivity']='com.example.punemetrotom.activity.ActivityLogin'

driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub",desired_caps)
wait = WebDriverWait(driver,60)
wait.until(EC.presence_of_element_located((AppiumBy.ID,"com.example.punemetrotom:id/txtUsername")))
loginUsername= driver.find_element(AppiumBy.ID,"com.example.punemetrotom:id/txtUsername")
loginUsername.send_keys("10001")
wait.until(EC.presence_of_element_located((AppiumBy.ID,"com.example.punemetrotom:id/txtPassword")))
loginPWD=driver.find_element(AppiumBy.ID,"com.example.punemetrotom:id/txtPassword")
loginPWD.send_keys("10001")
loginBTN=driver.find_element(AppiumBy.ID,"com.example.punemetrotom:id/btnLogin")
loginBTN.click()
wait.until(EC.presence_of_element_located((AppiumBy.ID,"com.example.punemetrotom:id/txtPassword")))
wait.until(EC.presence_of_element_located((AppiumBy.ID,"com.example.punemetrotom:id/editText_stock_qr_added")))
enterStock=driver.find_element(AppiumBy.ID,"com.example.punemetrotom:id/editText_stock_qr_added")
enterStock.send_keys("500")
updateButton=driver.find_element(AppiumBy.ID,"com.example.punemetrotom:id/button_stock_qr_update")
updateButton.click()
enterChangeMoney=driver.find_element(AppiumBy.ID,"com.example.punemetrotom:id/editText_stock_money_added")
enterChangeMoney.send_keys("1000")
chnageMoneyUpdate=driver.find_element(AppiumBy.ID,"com.example.punemetrotom:id/button_stock_money_update")
chnageMoneyUpdate.click()
confirm= driver.find_element(AppiumBy.ID,"com.example.punemetrotom:id/button_stock_update")
confirm.click()

wait.until(EC.presence_of_element_located((AppiumBy.CLASS_NAME,"android.widget.TextView")))
time.sleep(2)


#m=driver.find_element(AppiumBy.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[2]")
m=driver.find_elements(AppiumBy.XPATH,"//androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout/android.widget.TextView")

for i,n in enumerate(m):
    print(n.text)
    if n.text=="QR Ticket":
        pass



wait.until(EC.presence_of_element_located((AppiumBy.ID,"com.example.punemetrotom:id/txtAlphabet")))
alphas = driver.find_elements(AppiumBy.ID,"com.example.punemetrotom:id/txtAlphabet")
for alp in alphas:

    if alp.text=="A":
        alp.click()
        break
wait.until(EC.presence_of_element_located((AppiumBy.ID,"com.example.punemetrotom:id/textDestinationStation")))
dstn = driver.find_element(AppiumBy.ID,"com.example.punemetrotom:id/textDestinationStation")
dstn.click()
tickType = driver.find_element(AppiumBy.ID,"com.example.punemetrotom:id/btnSJT")
tickType.click()

TickIncr = driver.find_element(AppiumBy.ID,"com.example.punemetrotom:id/txtQuantityIncrement")

payConfirm = driver.find_element(AppiumBy.ID,"com.example.punemetrotom:id/btnConfirm")
payConfirm.click()
wait.until(EC.presence_of_element_located((AppiumBy.ID,"com.example.punemetrotom:id/txtTotalAmount")))

enterCash = driver.find_element(AppiumBy.ID,"com.example.punemetrotom:id/edtCashAmount")
enterCash.send_keys("10")
pay= driver.find_element(AppiumBy.ID,"com.example.punemetrotom:id/btnPay")
pay.click()
wait.until(EC.presence_of_element_located((AppiumBy.ID,"com.example.punemetrotom:id/txtSuccess")))

succesTxtissue=  driver.find_element(AppiumBy.ID,"com.example.punemetrotom:id/txtSuccess")
print(succesTxtissue.text)
#assert succesTxtissue.text == "Payment received and QR ticket issued successfully!"

print_rec = driver.find_element(AppiumBy.ID,"com.example.punemetrotom:id/button_print")
print_rec.click()
time.sleep(1)









