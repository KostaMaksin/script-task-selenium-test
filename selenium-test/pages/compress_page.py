import re

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from pages.base_page import BasePage


class CompressPage(BasePage):
    UPLOAD_LABEL = (By.CSS_SELECTOR, 'label[for="file-input"]')
    FILE_INPUT = (By.CSS_SELECTOR, 'input#file-input')
    DOWNLOAD_BUTTON = (By.CSS_SELECTOR, 'div.optimizer-download-btn')

    ORIGINAL_SIZE_VALUE = (
        By.XPATH,
        "//div[normalize-space()='Original size']/following-sibling::div[contains(@class,'size-value')]"
    )
    OUTPUT_SIZE_VALUE = (
        By.XPATH,
        "//div[normalize-space()='Output size']/following-sibling::div[contains(@class,'size-value')]"
    )

    def wait_until_loaded(self):
        self.switch_to_latest_window()
        self.wait.until(EC.presence_of_element_located(self.FILE_INPUT))
        self.wait.until(EC.presence_of_element_located(self.UPLOAD_LABEL))
        self.close_cookie_popup()

    def upload_video(self, file_path: str):
        file_input = self.wait.until(EC.presence_of_element_located(self.FILE_INPUT))
        file_input.send_keys(file_path)

    def wait_for_compression_to_finish(self):
        return WebDriverWait(self.driver, 180).until(
            EC.visibility_of_element_located(self.DOWNLOAD_BUTTON)
        )

    def download_video(self):
        download_element = self.wait_for_compression_to_finish()
        self.driver.execute_script("arguments[0].click();", download_element)

    def get_original_size_text(self) -> str:
        return self.wait.until(
            EC.visibility_of_element_located(self.ORIGINAL_SIZE_VALUE)
        ).text.strip()

    def get_output_size_text(self) -> str:
        return self.wait.until(
            EC.visibility_of_element_located(self.OUTPUT_SIZE_VALUE)
        ).text.strip()

    @staticmethod
    def size_to_bytes(size_text: str) -> int:
        match = re.search(r"([\d.]+)\s*(B|KB|MB|GB)", size_text.upper())
        if not match:
            raise ValueError(f"Could not parse size from text: {size_text}")

        value = float(match.group(1))
        unit = match.group(2)

        multipliers = {
            "B": 1,
            "KB": 1024,
            "MB": 1024 ** 2,
            "GB": 1024 ** 3,
        }

        return int(value * multipliers[unit])
