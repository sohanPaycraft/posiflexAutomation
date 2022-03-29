import time

from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['automationName'] = 'UiAutomator2'
desired_caps['deviceName'] = 'POCO F1'
desired_caps['app'] = ('/home/sohansagar/Downloads/com.flipkart.android.1470100.apk')



driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub",desired_caps)
driver.implicitly_wait(60)
lang = driver.find_element(AppiumBy.ID , "com.flipkart.android:id/tv_text")
print(lang.text)
actions = ActionChains(driver)
actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
actions.w3c_actions.pointer_action.move_to_location(460, 1668)
actions.w3c_actions.pointer_action.pointer_down()
actions.w3c_actions.pointer_action.move_to_location(480, 568)
actions.w3c_actions.pointer_action.release()
actions.perform()
lang = driver.find_elements(AppiumBy.ID , "com.flipkart.android:id/tv_text")
for l in lang:
    print(l.text)
    if l.text=="English":
        l.click()
        break

driver.find_element(AppiumBy.ID,"com.flipkart.android:id/select_btn").click()