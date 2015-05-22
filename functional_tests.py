'''
Created on May 22, 2015

@author: cdabija
'''

from selenium import webdriver
browser=webdriver.Firefox()
browser.get('http://localhost:8000')

assert 'Django' in browser.title