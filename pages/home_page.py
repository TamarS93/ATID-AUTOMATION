from urllib.parse import urlencode
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class HomePage:
    # Locators
    HOME_LINK = (By.LINK_TEXT, "HOME")
    STORE_LINK = (By.LINK_TEXT, "STORE")
    MEN_LINK = (By.LINK_TEXT, "MEN")
    WOMEN_LINK = (By.LINK_TEXT, "WOMEN")
    ACCESSORIES_LINK = (By.LINK_TEXT, "ACCESSORIES")
    ABOUT_LINK = (By.LINK_TEXT, "ABOUT")
    CONTACT_US_LINK = (By.LINK_TEXT, "CONTACT US")

    SHOP_NOW_BUTTON = (By.LINK_TEXT, "SHOP NOW")
    FIND_MORE_BUTTON = (By.LINK_TEXT, "FIND MORE")

    MAIN_HEADING = (By.XPATH, "//h1[contains(., 'ATID Demo Store')]")

    def __init__(self, driver, base_url):
        self.driver = driver
        self.base_url = base_url
        self.wait = WebDriverWait(driver, 10)

    def open(self):
        self.driver.get(self.base_url)

    def get_current_url(self):
        return self.driver.current_url

    def wait_for_home_page_to_load(self):
        self.wait.until(EC.visibility_of_element_located(self.MAIN_HEADING))

    def is_main_heading_displayed(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.MAIN_HEADING)
        ).is_displayed()

    def click_home(self):
        self.wait.until(EC.element_to_be_clickable(self.HOME_LINK)).click()

    def click_store(self):
        self.wait.until(EC.element_to_be_clickable(self.STORE_LINK)).click()

    def click_men(self):
        self.wait.until(EC.element_to_be_clickable(self.MEN_LINK)).click()

    def click_women(self):
        self.wait.until(EC.element_to_be_clickable(self.WOMEN_LINK)).click()

    def click_accessories(self):
        self.wait.until(EC.element_to_be_clickable(self.ACCESSORIES_LINK)).click()

    def click_about(self):
        self.wait.until(EC.element_to_be_clickable(self.ABOUT_LINK)).click()

    def click_contact_us(self):
        self.wait.until(EC.element_to_be_clickable(self.CONTACT_US_LINK)).click()

    def click_shop_now(self):
        self.wait.until(EC.element_to_be_clickable(self.SHOP_NOW_BUTTON)).click()

    def click_find_more(self):
        self.wait.until(EC.element_to_be_clickable(self.FIND_MORE_BUTTON)).click()

