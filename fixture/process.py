from selenium.webdriver.common.by import By
from datetime import datetime

class ProcessHelper:
    def __init__(self, app):
        self.app = app

    def start(self):
        driver = self.app.driver
        driver.find_element_by_xpath("//*[@class='android.widget.RelativeLayout']").click()

    def stop_time(self):
        return self.write_current_time()

    def reset(self):
        driver = self.app.driver
        driver.find_element(By.ID, 'yoavsabag.easystopwatch:id/reset_imageView').click()
        return self.write_current_time()

    def validate_one_minute(self, certain_time):
        before = datetime.strptime(certain_time, '%M:%S.%f').time()
        after = datetime.strptime('01:10.00', '%M:%S.%f').time()
        while True:
            timer = self.write_current_time()
            if before <= timer <= after:
                break
            elif timer < before:
                pass
            else:
                raise Exception('Failed')

    def write_current_time(self):
        driver = self.app.driver
        value_init = driver.find_element(By.ID, 'yoavsabag.easystopwatch:id/chronometer').text
        value = datetime.strptime(value_init, '%M:%S.%f').time()
        return value

    def convert_time(self, str_time):
        return datetime.strptime(str_time, '%M:%S.%f').time()
'''
if before < timer < after:
    print(before, timer, after)
else:
    print(before, timer, after)
    print("Huy")
'''

#if '00:10' in value:
#cur='00:10'
#if any(x in cur for x in value):
    #print(value)
    #break






