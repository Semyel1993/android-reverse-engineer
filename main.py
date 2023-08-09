import time

from appium import webdriver
from appium.webdriver.webelement import AppiumBy

desired_caps = dict(
    platformName='Android',
    deviceName='Android',
    automationName='uiautomator2',
    appPackage='com.android.chrome',
    appActivity='com.google.android.apps.chrome.Main',
    noReset=True,
)

wd = webdriver.Remote('http://localhost:4723', desired_caps)
wd.implicitly_wait(30)
size = wd.get_window_size()
swipe_start_x = size['width'] / 2
swipe_start_y = size['height'] - size['height'] / 6
swipe_end_x = size['width'] / 2
swipe_end_y = 5
print(swipe_start_y)

search_field = wd.find_element(by=AppiumBy.ID, value='com.android.chrome:id/url_bar')
search_field.click()
search_field.send_keys('42')
wd.press_keycode(66)

if wd.is_keyboard_shown():
    wd.hide_keyboard()

wd.swipe(swipe_start_x, swipe_start_y, swipe_end_x, swipe_end_y, duration=200)
time.sleep(0.3)

links = wd.find_elements(by=AppiumBy.CLASS_NAME, value='android.widget.TextView')
links[-1].click()
time.sleep(5)

wd.back()

wd.quit()
