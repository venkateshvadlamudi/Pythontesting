import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from testCases.confitest import setup
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

class Test_001_Login:
    #baseURL="https://cms.allmysons.com/"
    #username="venkatesh"
    #password="Cms@123"

    baseURL= ReadConfig.getApplicationURL()
    username= ReadConfig.getUsername()
    password= ReadConfig.getPassword()

    logger=LogGen.loggen()

    @pytest.mark.sanity
    def test_homePageTitle(self, setup):

        self.logger.info("****** Test_001_Login ******")
        self.logger.info("****** Verify Home Page Tittle ******")
        self.driver= setup
        self.driver.get(self.baseURL)
        act_title=self.driver.title

        if act_title == "All My Sons Client Management System":
            assert True
            self.driver.close()
            self.logger.info("****** Home page tittle is passed: ******")
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_homePageTitle.png")
            self.driver.close()
            self.logger.erroe("****** Home page title is failed ******")
            assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_login(self, setup):
        self.logger.info("****** Verifying login test******")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp=LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        act_title = self.driver.title

        if act_title == "All My Sons Client Management System":
            assert True
            self.driver.close()
            self.logger.info("****** Login Pass test******")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "LoginFailed.png")
            self.driver.close()
            self.logger.error("****** Login Failed test******")
            assert False














