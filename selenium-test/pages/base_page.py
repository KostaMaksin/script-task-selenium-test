from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException


class BasePage:
    COOKIE_ACCEPT = (By.CSS_SELECTOR, 'button[data-tid="banner-accept"]')

    def __init__(self, driver, timeout: int = 60):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def wait_for_presence(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def wait_for_visible(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def wait_for_clickable(self, locator):
        return self.wait.until(EC.element_to_be_clickable(locator))

    def click(self, locator):
        self.wait_for_clickable(locator).click()

    def close_cookie_popup(self, timeout=5):
        try:
            button = WebDriverWait(self.driver, timeout).until(
                EC.element_to_be_clickable(self.COOKIE_ACCEPT)
            )
            button.click()
        except TimeoutException:
            pass

    def switch_to_latest_window(self):
        self.driver.switch_to.window(self.driver.window_handles[-1])