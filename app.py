from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from userInfo import username, password
import time

class Instagram:
    driver_path = "C:\Users\demir\Drivers\chromedriver"

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.browser = webdriver.Chrome(Instagram.driver_path)

    def signIn(self):
        self.browser.get("https://www.instagram.com/accounts/login/")
        time.sleep(3)
        usernameInput = self.browser.find_element_by_name("username")
        passwordInput = self.browser.find_element_by_name("password")

        usernameInput.send_keys(self.username)
        passwordInput.send_keys(self.password)

        passwordInput.send_keys(Keys.ENTER)

    def getFollowers(self):
        pass

    def followUser(self, username):
        pass

    def unFollowUser(self, username):
        pass

    def __del__(self):
        time.sleep(5)
        self.browser.quit()

app = Instagram(username, password)

app.signIn()
app.getFollowers()
app.followUser("target_username")
app.unFollowUser("target_username")
