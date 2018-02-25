# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import time
from django.test import TestCase,LiveServerTestCase

from selenium import webdriver
from django.contrib.auth import get_user_model
# Create your tests here.
class UserIbanCase(LiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

        self.browser.implicitly_wait(1)
        self.admin_user = get_user_model().objects.create_superuser(username='islam', email='islam@example.com',
                                                                    password='password1')
        self.admin_user = get_user_model().objects.create_superuser(username='ahmed', email='ahmed@example.com',
                                                                    password='password2')
        self.admin_user = get_user_model().objects.create_superuser(username='ali', email='ali@example.com',
                                                                    password='password3')

    # this test Case just try to test admin login
    """
    def test_failed_admin_login(self):

        home_page = self.browser.get(self.live_server_url + '/admin')

        user_name_input = self.browser.find_element_by_name("username")
        password_input = self.browser.find_element_by_name("password")
        submit =  self.browser.find_element_by_xpath("//input[@type='submit']")
        user_name_input.send_keys("islam")
        password_input.send_keys("password")
        submit.submit()

        error = self.browser.find_element_by_class_name("errornote")
        self.assertIsNotNone(error)
    """
    # this test Case just try to test admin login
    def test_admin_login(self):
        home_page = self.browser.get(self.live_server_url + '/admin')

        user_name_input = self.browser.find_element_by_name("username")
        password_input = self.browser.find_element_by_name("password")
        submit = self.browser.find_element_by_xpath("//input[@type='submit']")

        user_name_input.clear()
        password_input.clear()

        user_name_input.send_keys("islam")
        password_input.send_keys("password1")
        submit.submit()
        time.sleep(1)
        body = self.browser.find_element_by_tag_name('body')
        self.assertIn('Site administration', body.text)

    # check add users in admin pannel
    def test_admin_add_user(self):
        home_page = self.browser.get(self.live_server_url + '/admin')

        #find inputs
        user_name_input = self.browser.find_element_by_name("username")
        password_input = self.browser.find_element_by_name("password")
        submit = self.browser.find_element_by_xpath("//input[@type='submit']")

        user_name_input.clear()
        password_input.clear()
        #send Keys To inputs
        user_name_input.send_keys("islam")
        password_input.send_keys("password1")
        #submit
        submit.submit()

        users_link = self.browser.find_elements_by_partial_link_text("Users IBAN")
        users_link[0].click()
        add_user = self.browser.find_element_by_partial_link_text('Add user')
        add_user.click()

        #find inputs
        first_name_input = self.browser.find_element_by_name("first_name")
        last_name_input = self.browser.find_element_by_name("last_name")
        iban_input = self.browser.find_element_by_name("iban")

        #send Keys To inputs
        first_name_input.send_keys("ahmed")
        last_name_input.send_keys("samy")
        iban_input.send_keys("123456789")
        #submit
        self.browser.find_element_by_name("_save").submit()
        time.sleep(1)
        body = self.browser.find_element_by_tag_name('body')
        self.assertIn('was added successfully', body.text)
        self.assertIn('ahmed', body.text)


    def tearDown(self):
        time.sleep(1)
        self.browser.quit()