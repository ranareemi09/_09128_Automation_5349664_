import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

url = "https://www.youtube.com/"
# test youtube for 5 different search queries
@pytest.mark.parametrize("search_query", ["Katalon Studio", "Appium", "Datadog", "Perfectto", "TestingWhiz"])
def test_youtube_search_results(search_query, num_results=5):
    # open google.co
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get(url)
    # enter search query
    search_box = driver.find_element(By.NAME,"search_query")
    search_box.send_keys(search_query)
    search_box.send_keys(Keys.RETURN)
    # check if search results are greater than 10
    search_results = driver.find_elements(By.CLASS_NAME,"yt-lockup-video")
    assert len(search_results) >= 5, "Search results are less than 5"
    driver.close()