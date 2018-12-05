from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import ui
import time
import pandas as pd
import numpy as np
from bs4 import *
import requests

url = "http://lt.morningstar.com/gvji07hh87/fundquickrank/default.aspx?LanguageId=en-GB"

data = {'ctl00$ContentPlaceHolder1$aFundQuickrankControl$txtSearchKey': 'LU0079474960'}
r = requests.post(url, data=data)
print(r.text)