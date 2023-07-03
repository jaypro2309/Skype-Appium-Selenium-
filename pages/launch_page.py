from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pyperclip
import time

class LaunchPage():
    def __init__(self, driver):
        self.driver = driver

    def allow(self):
        try:
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable
                                             ((AppiumBy.XPATH, "//android.widget.Button[@text='Allow']"))).click()
        except:
            print("this setp is skiped.")
    def create(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable
                                             ((AppiumBy.XPATH, "//android.widget.Button[@content-desc='Sign in or create']"))).click()

    def enter_email(self, email):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable
                                             ((AppiumBy.CLASS_NAME, "android.widget.EditText"))).send_keys(email)
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable
                                             ((AppiumBy.XPATH, "//android.widget.Button[@text='Next']"))).click()
    def otp(self):
        try:
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable
                                                 ((AppiumBy.XPATH,"//android.widget.TextView[@text='Email code to json7753@gmail.com']"))).click()
        except:
            self.driver.start_activity('com.google.android.gm','com.google.android.gm.ConversationListActivityGmail')

    def email(self):
        # try:
            self.driver.start_activity('com.google.android.gm', 'com.google.android.gm.ConversationListActivityGmail')
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable
                                                 ((AppiumBy.XPATH, "//android.widget.TextView[@text='Your single-use code']"))).click()
            verification_element = self.driver.find_element(AppiumBy.XPATH,
                                                       "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.FrameLayout/androidx.viewpager.widget.ViewPager/android.widget.FrameLayout/android.view.ViewGroup/android.webkit.WebView/android.webkit.WebView/android.view.View/android.widget.TextView[4]")
            time.sleep(3)
            self.verification_code = verification_element.text.split('Your single-use code is: ')[-1]
            self.copy(verification_code)
            self.opy_code = pyperclip.paste()

        # except:
        #     self.driver.start_activity('com.google.android.gm', 'com.google.android.gm.ConversationListActivityGmail')
        #     WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable
        #                                          ((AppiumBy.XPATH, "//android.widget.TextView[@text='Your single-use code']"))).click()
        #     verification_element = self.driver.find_element(AppiumBy.XPATH,
        #                                                "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.FrameLayout/androidx.viewpager.widget.ViewPager/android.widget.FrameLayout/android.view.ViewGroup/android.webkit.WebView/android.webkit.WebView/android.view.View/android.widget.TextView[4]")
        #     time.sleep(3)
        #     self.verification_code = verification_element.text.split('Your single-use code is: ')[-1]
        #     self.copy(verification_code)
        #     self.otp_code = pyperclip.paste()
        #     self.driver.activate_app('com.skype.raider')

    def enter_opt(self):
        time.sleep(5)
        self.driver.hide_keyboard()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable
                                             ((AppiumBy.CLASS_NAME, "android.widget.EditText"))).send_keys(otp_code)

        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable
                                             ((AppiumBy.CLASS_NAME, "android.widget.Button"))).click()


