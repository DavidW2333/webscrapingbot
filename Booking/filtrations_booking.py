from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class FiltrationBooking:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def apply_Amenities(self, *amenity):  # change amenity into random value
        drop_down = self.driver.find_element(By.XPATH, "//div[normalize-space()='More filters']")
        drop_down.click()
        amenities = self.driver.find_element(By.XPATH,
                                             "//body[1]/div[1]/main[1]/article[1]/section[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[6]/div[1]/span[1]/div[1]/div[1]/div[1]/div[1]/div[1]")
        all_amenities = amenities.find_elements(By.CSS_SELECTOR, "*")

        for all_elements in amenity:
            for child in all_amenities:
                if str(child.get_attribute('innerHTML')).strip() == f'{all_elements}':
                    child.click()
        apply_button = self.driver.find_element(By.XPATH,
                                                "//div[@class='filter-dropdown__popup-action filter-dropdown__popup-action--lg']")
        apply_button.click()

    #def set_price_range(self):
        #min_price = self.driver.find_element(By.XPATH, "//span[@class='ui-slider-handle ui-corner-all ui-state-default']")
        #max_price = self.driver.find_element(By.XPATH, "//span[@class='ui-slider-handle ui-corner-all ui-state-default']")
