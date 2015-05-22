'''
Created on May 22, 2015

@author: cdabija
'''

from selenium import webdriver
browser=webdriver.Firefox()
browser.get('http://localhost:8000')


#dsgdf
#243242
assert 'Django' in browser.title
