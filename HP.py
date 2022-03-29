import time

from appium import webdriver


desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['automationName'] = 'UiAutomator2'
desired_caps['platformVersion'] = '8.1.0'
desired_caps['deviceName'] = '192.168.1.102:5555'
#desired_caps['deviceId'] = '10.164.30.101:5555'
desired_caps['app'] = ('/home/sohansagar/Downloads/Posi.apk')
desired_caps['appPackage'] = 'com.example.punemetrotom'

driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub",desired_caps)