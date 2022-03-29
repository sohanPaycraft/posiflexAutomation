import time

from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['automationName'] = 'UiAutomator2'
desired_caps['platformVersion'] = '9'
desired_caps['deviceName'] = 'B2153CC46B'
desired_caps['app'] = ('/home/sohansagar/Downloads/Posi.apk')
desired_caps['noReset'] = "true"
desired_caps['fullReset'] = "false"
#desired_caps['appPackage'] = 'com.code2lead.kwad'
#desired_caps['appActivity'] = 'com.code2lead.kwad.MainActivity'

driver=webdriver.Remote("http://127.0.0.1:4723/wd/hub",desired_caps)
ele_id = driver.find_element(AppiumBy.ID,"com.code2lead.kwad:id/EnterValue")
ele_id.click()
#driver.back()
#ind=driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,"UiSelector().index(4)")
#ind.click()
#driver.back()
#ele_id.click()
#time.sleep(2)
#cl=driver.find_element(AppiumBy.CLASS_NAME,"android.widget.EditText")
#cl.send_keys("djjjjjjjjjjjjdahjdah")
#driver.close_app()