from selenium import webdriver

taburl="http://www.google.com?#q=";
searchterm = raw_input("Enter Search Query :");

browser = webdriver.Firefox()
browser.get(taburl+searchterm)
