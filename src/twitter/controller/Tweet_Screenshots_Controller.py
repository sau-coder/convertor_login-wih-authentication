import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager


class Tweet_Screenshot_Controller:
    def __init__(self, tweet_url):
        self.tweet_url = tweet_url
        self.chrome_options = Options()
        self.chrome_options.add_argument("--headless")

    def get_base_64_of_tweet(self):
        driver = webdriver.Chrome(
            executable_path=ChromeDriverManager().install(),
            chrome_options=self.chrome_options,
        )
        driver.get(self.tweet_url)
        WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located(
                (By.XPATH, '//div[@data-testid="cellInnerDiv"]')
            )
        )
        time.sleep(1)
        required_width = driver.execute_script(
            "return document.body.parentNode.scrollWidth"
        )
        required_height = driver.execute_script(
            "return document.body.parentNode.scrollHeight"
        )
        driver.set_window_size(required_width, required_height)
        return driver.find_element(
            By.XPATH, '//div[@data-testid="cellInnerDiv"]'
        ).screenshot_as_base64
