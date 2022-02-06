import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


url = "https://www.google.com"
# search queries

@pytest.mark.parametrize("search_query", ["dog", "cat", "camel", "elephant", "rabbit", "tortoise", "sheep", "foxy", "peacock", "lion"])
def test_search_results(search_query, num_results=10):
     # visit google.com
     driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
     driver.get(url)
     # enter search query for this
     search_box = driver.find_element(By.NAME,"q")
     search_box.send_keys(search_query)
     search_box.send_keys(Keys.RETURN)
     # verify if search results are greater than 10
     search_results = driver.find_elements(By.CLASS_NAME, "g")
     assert len(search_results) >= 10, "Srch res are less than 10"
     driver.close()

