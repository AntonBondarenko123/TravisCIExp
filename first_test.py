from time import sleep

from selenium import webdriver
import geckodriver_autoinstaller
from selenium.webdriver.firefox.options import Options

geckodriver_autoinstaller.install()  # Check if the current version of geckodriver exists


# and if it doesn't exist, download it automatically,


def test_login_button():
    options = Options()
    options.headless = True
    options.add_argument('-headless')
    driver = webdriver.Firefox(options=options)
    driver.get("http://www.python.org")
    assert "Python" in driver.title
    driver.quit()
