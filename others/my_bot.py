from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.common.exceptions import ElementClickInterceptedException

class InstaFollower:
    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)

        self.driver = webdriver.Chrome(options=chrome_options)

    def login(self, user_name, passwords):
        self.driver.get("https://www.instagram.com/accounts/login")
        sleep(5)
        email = self.driver.find_element(By.XPATH, value='//*[@id="loginForm"]/div/div[1]/div/label/input')
        email.send_keys(user_name)
        password = self.driver.find_element(By.XPATH, value='//*[@id="loginForm"]/div/div[2]/div/label/input')
        password.send_keys(passwords)
        password.send_keys(Keys.ENTER)
        input("Please check the website")

    def find_followers(self, similar_account):
        sleep(2)
        new_url = f"https://www.instagram.com/{similar_account}"
        self.driver.execute_script(f"window.location = '{new_url}'")
        input("Please check the website")

    def follow(self):
        sleep(5)
        following_buttons = self.driver.find_elements(By.CSS_SELECTOR, value='button ._aacl')

        for n in range(15):
            for button in following_buttons:
                sleep(5)
                try:
                    button.click()
                except ElementClickInterceptedException:
                    cancel = self.driver.find_element(By.XPATH, value='/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div/div/button[2]')
                    cancel.click()


            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", following_buttons)




