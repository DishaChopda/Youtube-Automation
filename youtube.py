import time
from selenium.webdriver.common.by import By
from selenium import webdriver


chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")


#Enter your path name where your chromedriver is being installed 
driver = webdriver.Chrome(r"C:\Users\DELL\PycharmProjects\SeleniumTesting\Browsers\chromedriver.exe", chrome_options=chrome_options)
driver.maximize_window()

driver.get("https://www.youtube.com/")
time.sleep(2)

#search box
driver.find_element_by_xpath("/html/body/ytd-app/div/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/form/div/div[1]/input").send_keys("automation")#change the search key accordingly
time.sleep(5)

#seach button
driver.find_element_by_xpath("//*[@id='search-icon-legacy']/yt-icon").click()
time.sleep(5)

driver.find_element_by_xpath('/html/body/ytd-app/div/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-video-renderer[3]/div[1]/div/div[1]/div/h3/a/yt-formatted-string').click()
time.sleep(3)

url = driver.current_url
print(url)
print(driver.title)

driver.get("https://en.savefrom.net/1-youtube-video-downloader-2/")
time.sleep(2)

driver.find_element_by_id("sf_url").send_keys(url)
time.sleep(2)

driver.find_element_by_id("sf_submit").click()
time.sleep(10)

driver.find_element(By.XPATH, "//*[@id='sf_result']/div/div[1]/div[2]/div[2]/div[2]/div[1]").click()
print("Download Started")
time.sleep(5)
driver.find_element(By.XPATH, "//*[@id='sf_result']/div/div[1]/div[2]/div[2]/div[2]/div[2]/div/div/div[1]/a[1]").click()
print("Download Started")
time.sleep(10)

driver.quit()

