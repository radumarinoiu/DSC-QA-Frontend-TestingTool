from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options


opts = Options()
opts.headless = False
browser = Firefox(options=opts)