from selenium import webdriver
import os

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

import Booking.constants as cons
from selenium.webdriver.chrome.options import Options

from Booking.filtrations_booking import FiltrationBooking


# driver = webdriver.Chrome(options=c_options)
# c_options = webdriver.ChromeOptions
# c_options.add_experimental_option(self, "detach", True)

class Booking(webdriver.Chrome):
    def __init__(self, driver_path=r"C:\seleniumdriver", teardown=False):
        self.driver_path = driver_path
        self.teardown = teardown
        os.environ['PATH'] += self.driver_path

        super(Booking, self).__init__()
        # self.implicitly_wait(15)
        self.maximize_window()

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.quit()

    def get_firstPage(self):
        self.get(cons.web_URL)

    def select_place(self, location):
        search_bar = self.find_element(By.XPATH, "//input[@id='autocomplete_search']")
        search_bar.send_keys(location)

    def select_dates(self, checkInDate, checkOutDate):
        check_in = self.find_element(By.XPATH, "//input[@id='start_date']")
        check_in.send_keys(checkInDate)
        check_out = self.find_element(By.XPATH, "//input[@id='end_date']")
        check_out.send_keys(checkOutDate)

    def select_num_guests(self, count):
        number_of_guest = self.find_element(By.XPATH, "//select[@name='num_sleeps']")
        # number_of_guest.click()
        number = self.find_element(By.XPATH, f"//option[normalize-space()='{count}']")
        number.click()

    def search(self):
        search_button = self.find_element(By.XPATH, "//div[@class='col col--sm-4']//button[@type='submit']")
        search_button.click()

    def apply_filtration(self):
        filtration = FiltrationBooking(driver=self)
        filtration.apply_Amenities("WIFI", "TV", "BBQ")

    def report_results(self):
        hotel_boxes = self.find_element(By.ID, "ListView"
                                        ).find_elements(By.CLASS_NAME, "col col--set-block")
        print(len(hotel_boxes))
        return hotel_boxes
