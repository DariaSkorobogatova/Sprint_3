import pytest
from selenium import webdriver


@pytest.fixture(scope='function')
def driver():
    wd = webdriver.Chrome()
    yield wd
    wd.quit()
