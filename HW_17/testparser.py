from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

from CONCTANTS import *
from my_logger import get_logger
from time import sleep

logger = get_logger()


class Twitter:
    def __init__(self, executable_path):
        self.driver = webdriver.Chrome(executable_path=executable_path)

    def find_necessary_person(self, username: str):
        self.driver.get(GOOGLE_URL)
        self.driver.find_element_by_xpath(XPATH_SEARCH).send_keys(f'Twitter {username}')
        self.driver.find_element_by_xpath(SEARCH_IN_GOOGLE).click()
        self.driver.find_element_by_xpath(USERS_XPATH).click()
        try:
            name = self.driver.find_element_by_xpath(FIRST_LAST_NAME).text
            nick_name = self.driver.find_element_by_xpath(NICKNAME).text
            followers = self.driver.find_element_by_xpath(FOLLOWERS).text

            logger.debug(f'{name, nick_name, followers}')
        except NoSuchElementException:
            logger.debug(f'Похоже ты очень старался, но что то пошло не так!!')


if __name__ == '__main__':
    twitter_finder = Twitter(executable_path=PATH_TO_DRIVER)
    twitter_finder.find_necessary_person(username="Soloduha")
    sleep(3)
    twitter_finder.driver.close()
