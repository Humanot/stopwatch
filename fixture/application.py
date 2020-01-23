from appium import webdriver
from fixture.process import ProcessHelper

class Application:

    def __init__(self):
        desired_capabilities = {
            "platformName": "Android",
            "udid": "0123456789ABCDEF",
            "platformVersion": "4.4",
            "deviceName": "MicroMax",
            "automationName":"UiAutomator1",
            #"app": "D:\Future\Development\Projects\Auto\stopwatch\Easy Stopwatch_v1.5.0.15122019_apkpure.com.apk",
            "appPackage": "yoavsabag.easystopwatch",
            "appActivity": "yoavsabag.easystopwatch.MainActivity",
            "newCommandTimeout": "120"
        }

        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capabilities=desired_capabilities)
        self.process = ProcessHelper(self)

    def is_valid(self):
        try:
            self.driver.current_url
            return True
        except:
            return False

    def destroy(self):
        self.driver.quit()