from time import sleep
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from urllib.parse import quote


class RechtspersonenregisterBot:
    RPR = "ONDERNEMINGSRECHTBANK"

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://territoriale-bevoegdheid.just.fgov.be/cgi-main/competence-territoriale.pl")
        sleep(2)

    def select_postal_code(self, postal_code):
        postal_code_button = self.driver.find_element_by_xpath(
            '//html/body/div[2]/div/div/div/div[1]/form/div[2]/div/span/span[1]/span/span[1]').click()
        postal_code_field = self.driver.find_element_by_xpath('/html/body/span/span/span[1]/input')
        postal_code_field.send_keys(postal_code)
        sleep(1)
        self.driver.find_element_by_xpath('/html/body/span/span/span[2]/ul/li').click()

    def select_street(self, streetname):
        streetname_button = self.driver.find_element_by_xpath(
            '/html/body/div[2]/div/div/div/div[1]/form/div[3]/div/div/span/span[1]/span/span[1]').click()
        streetname_field = self.driver.find_element_by_xpath('/html/body/span/span/span[1]/input')
        streetname_field.send_keys(streetname)
        sleep(1)
        self.driver.find_element_by_xpath('/html/body/span/span/span[2]/ul/li').click()

    def get_rpr_details(self):
        i = 0
        found = False

        while found is False:
            i += 1
            try:
                single_table_element = self.driver.find_element_by_xpath(
                    "/html/body/div[2]/div/div/div/div[1]/div/div/div/table/tbody/tr[" + str(i) + "]/td[1]").text

                words = single_table_element.split()

                if self.RPR in words:
                    found = True
                    print("------")
                    print(single_table_element)
            except NoSuchElementException:
                return False

    def is_Displayed(self, xpath_param):
        try:
            self.driver.find_element_by_xpath(xpath_param).is_displayed()
        except NoSuchElementException:
            return False
        return True

    def fill_data(self, postal_code, streetname):
        self.select_postal_code(postal_code)
        sleep(1)

        if self.is_Displayed(
                '/html/body/div[2]/div/div/div/div[1]/form/div[3]/div/div/span/span[1]/span/span[1]') is True:
            self.select_street(streetname)

        sleep(1)

    def close(self):
        self.driver.close()


bot = RechtspersonenregisterBot()
bot.fill_data(9000, "stropstraat")
bot.get_rpr_details()
bot.close()
