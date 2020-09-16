import time

import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from testCases.confitest import setup
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities import XLUtilities

class Test_002_DDT_Login:
    #baseURL="https://cms.allmysons.com/"
    #username="venkatesh"
    #password="Cms@123"

    baseURL= ReadConfig.getApplicationURL()
    # username= ReadConfig.getUsername()
    # password= ReadConfig.getPassword()
    path=".//TestData/LoginData.xlsx"

    logger=LogGen.loggen()

    @pytest.mark.regression
    def test_login(self, setup):
        self.logger.info("****** Test_002_DDT_Login ******")
        self.logger.info("****** Verifying login DDT test******")
        self.driver = setup
        self.driver.get(self.baseURL)

        self.lp=LoginPage(self.driver)

        lst_status=[]

        self.rows=XLUtilities.getRowCount(self.path,'Sheet1')
        print("Number of Rows is a Excel:" , self.rows)

        for r in range(2,self.rows+1):
            self.username=XLUtilities.readData(self.path,'Sheet1',r,1)
            self.Password = XLUtilities.readData(self.path, 'Sheet1', r, 2)
            self.exp=XLUtilities.readData(self.path, 'Sheet1', r, 3)

            self.lp.setUserName(self.username)
            self.lp.setPassword(self.Password)
            self.lp.clickLogin()
            time.sleep(5)

            act_title = self.driver.title
            exp_title = "All My Sons Client Management System"

            if act_title==exp_title:
                if self.exp=="Pass":
                    self.logger.info("******* Passed ********")
                    self.driver.get(self.baseURL)
                    lst_status.append("pass")
                elif self.exp=="Fail":
                    self.logger.info("******* Failed.... ********")
                    self.driver.get(self.baseURL)
                    lst_status.append("fail")
            elif act_title!=exp_title:
                if self.exp=="Pass":
                    self.logger.info("******* Failed ********")
                    lst_status.append("fail")
                elif self.exp=="Fail":
                    self.logger.info("******* Passed ********")
                    lst_status.append("pass")

            if "fail" not in lst_status:
                self.logger.info("LOGIN DDT test Passed.....")
                self.driver.close
                assert True
            else:
                self.logger.info("LOGIN DDT test Failed.....")
                self.driver.close


            self.logger.info("******* END of Login Test ****")
            self.logger.info("******** Completed TC_Login_DDT_002 test ******")
























