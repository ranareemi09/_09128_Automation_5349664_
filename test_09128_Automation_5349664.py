import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


url = "https://www.google.com"
# for 10 different search queries
@pytest.mark.parametrize("search_query", ["selenium", "python", "java", "c++", "c#", "javascript", "ruby", "php", "c", "go"])
def test_search_results(search_query, num_res=10):
     # open google.com
     driver = webdriver.Chrome()
     driver.get(url)
     # enter search query
     search_box = driver.find_element_by_name("q")
     search_box.send_keys(search_query)
     search_box.send_keys(Keys.RETURN)
     # check if search results are greater than 10
     search_results = driver.find_elements_by_class_name("g")
     assert len(search_results) >= 10, "Search results are less than 10"
     driver.close()

url2 = "https://www.youtube.com/"
# test youtube for 5 different search queries
@pytest.mark.parametrize("search_query", ["selenium", "python", "java", "c++", "c#"])
def test_youtube_search_results(search_query, num_res=5):
    # open google.com
    driver = webdriver.Chrome()
    driver.get(url)
    # enter search query
    search_box = driver.find_element_by_name("search_query")
    search_box.send_keys(search_query)
    search_box.send_keys(Keys.RETURN)
    # check if search results are greater than 10
    search_results = driver.find_elements_by_class_name("yt-lockup-video")
    assert len(search_results) >= 5, "Search results are less than 5"
    driver.close()