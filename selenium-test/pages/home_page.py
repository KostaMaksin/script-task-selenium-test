from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class HomePage(BasePage):
    URL = "https://jpegmini.com/"

    COMPRESS_VIDEO_BUTTON = (
        By.XPATH,
        "//a[contains(@href, 'compress-videos')]"
    )

    def open(self):
        self.driver.get(self.URL)
        self.close_cookie_popup()

    def click_compress_videos(self):
        self.click(self.COMPRESS_VIDEO_BUTTON)