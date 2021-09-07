from selenium import webdriver

#open the news website using webdriver
PATH = "/Users/qin/Downloads/chromedriver"
driver = webdriver.Chrome(PATH)
driver.get("https://arstechnica.com/")

#locate the search box
click_button = driver.find_element_by_id("header-search").click()
#send a existent title to the search box
text_area = driver.find_element_by_id("hdr_search_input")
text_area.send_keys("California streaming: Apple’s next big event is September 14")
#click enter to search the post
text_area.submit()