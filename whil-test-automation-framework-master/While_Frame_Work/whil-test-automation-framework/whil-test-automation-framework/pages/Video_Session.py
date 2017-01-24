from selenium import webdriver
from pages.base import Page
from time import sleep
from selenium.webdriver.common.keys import Keys
from pages.locators import *
from selenium.webdriver.support import expected_conditions as EC

class VideoSession(Page):

    def FindVidButton(self):
        for i in range(10):
            try:
                self.find_element(*VideoSessionLocators.VID_ICON)
            except:
                continue


    def ClickExitButton(self):
        for i in range(10):
            try:
                self.find_element(*VideoSessionLocators.EXIT).click()
            except:
                continue

    def click_pause(self):
        self.find_element(*VideoSessionLocators.PAUSE_BTN).click()



    def assert_video_stopped(self):
            for i in range(20):
                try:
                    if self.find_element(*VideoSessionLocators.PLAY_BTN) is True:
                        break
                except:
                    continue


    def click_play(self):
            self.find_element(*VideoSessionLocators.PLAY_BTN).click()
            self.find_element(*VideoSessionLocators.PAUSE_BTN).click()










