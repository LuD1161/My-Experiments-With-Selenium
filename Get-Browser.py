from selenium import webdriver

browser = webdriver.Firefox()
browser.get('http://bing.com')
print('Firefox Version:'+browser.capabilities['version'])