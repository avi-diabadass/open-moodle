from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class OpenMoodle(object):

    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password
        self.path = '/Users/avigranoff/Desktop/chromedriver'
        self.driver = webdriver.Chrome(self.path)

    def open_subjects_pane(self):

        self.driver.get('https://moodle.mashov.info/kfar-batya/login/index.php')

        user_name = self.driver.find_element_by_id("username")
        user_name.send_keys(self.username)
        password = self.driver.find_element_by_id("password")
        password.send_keys(self.password)
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "loginbtn")))
        element.click()

    def math(self, course):
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.LINK_TEXT, course)))
        element.click()




things = ["Math", "Physics", "Talmud", "Rephuah"]

ouchy = {"1" : "מתמטיקה י2-י3 - [1157]",
         "2" : "פיסיקה י1-י2 - [1194]",
         "3" : "תלמוד י2 - [1159]",
         "4" : "מדעי הרפואה י1-י3 - [1188]"}

user = input("Enter your username: ")
password = input("Enter your password: ")

what = 1
for shiur in things:
    print(shiur, "ID: {}".format(what))
    what += 1
subject = input("What class do you want to go to? Enter the ID:   ")
it_is = ouchy[subject]


user1 = OpenMoodle(user, password)
user1.open_subjects_pane()
user1.math(it_is)
