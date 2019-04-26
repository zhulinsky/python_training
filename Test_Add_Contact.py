# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class TestAddContact(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)

    def test_add_contact(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd)
        self.neu_form(wd)
        self.fitstname(wd)
        self.middlname(wd)
        self.lastname(wd)
        self.address(wd)
        self.home_telefon(wd)
        self.mobile_telefon(wd)
        self.email(wd)
        self.b_day(wd)
        self.b_month(wd)
        self.b_year(wd)
        self.submit_contact_creation(wd)
        self.logout(wd)

    def logout(self, wd):
        wd.find_element_by_link_text("Logout").click()

    def submit_contact_creation(self, wd):
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()

    def b_year(self, wd, bd_year="1974"):
        wd.find_element_by_name("byear").click()
        wd.find_element_by_name("byear").clear()
        wd.find_element_by_name("byear").send_keys("%s" % bd_year)

    def b_month(self, wd, bd_month="January"):
        wd.find_element_by_name("bmonth").click()
        Select(wd.find_element_by_name("bmonth")).select_by_visible_text("%s" % bd_month)
        wd.find_element_by_name("bmonth").click()

    def b_day(self, wd, bd_day="11"):
        wd.find_element_by_name("bday").click()
        Select(wd.find_element_by_name("bday")).select_by_visible_text("%s" % bd_day)
        wd.find_element_by_name("bday").click()

    def email(self, wd, email="mous_dom@mail.ru"):
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys("%s" % email)

    def mobile_telefon(self, wd, mob_telefon="5687454653456"):
        wd.find_element_by_name("mobile").click()
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys("%s" % mob_telefon)

    def home_telefon(self, wd, home_telefon="34534534"):
        wd.find_element_by_name("home").click()
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys("%s" % home_telefon)

    def address(self, wd, address="ertwerwte"):
        wd.find_element_by_name("address").click()
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys("%s" % address)

    def lastname(self, wd, lastname="kldfg"):
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys("%sj" % lastname)

    def middlname(self, wd, middlname="gdhf"):
        wd.find_element_by_name("middlename").click()
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys("%s" % middlname)

    def fitstname(self, wd, fitstname="jdfdsfgs"):
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys("%s" % fitstname)

    def neu_form(self, wd):
        wd.find_element_by_link_text("add new").click()

    def login(self, wd, username="admin", login="secret"):
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys("%s" % username)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys("%s" % login)
        wd.find_element_by_xpath("//input[@value='Login']").click()

    def open_home_page(self, wd):
        wd.get("http://localhost/addressbook/")

    def is_element_present(self, how, what):
        try: self.wd.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.wd.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True

    def tearDown(self):
        self.wd.quit()

if __name__ == "__main__":
    unittest.main()
