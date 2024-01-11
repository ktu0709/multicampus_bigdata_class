import os
import re
import subprocess
from time import sleep
from bs4 import BeautifulSoup

from selenium import webdriver
options = webdriver.EdgeOptions()
driver = webdriver.Edge(options=options)
url = "https://comic.naver.com/webtoon?tab=tue"
soup = BeautifulSoup(driver.page_source,'html.parser')
print(soup)