from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from xpaths import url_xpaths
from configparser import ConfigParser
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import logging
import time
from selenium.common.exceptions import TimeoutException

lazy_page_product_list =[]

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("saucecode_execution_logs.log"),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)


class testUrl:
    def __init__(self):
        self.driver = webdriver.Chrome()
        options = webdriver.ChromeOptions()

        prefs = {
            "credentials_enable_service": False,
            "profile.password_manager_enabled": False,
        }

        options.add_experimental_option("prefs", prefs)

        self.driver = webdriver.Chrome(options=options)
        self.wait = WebDriverWait(self.driver, 10)

        logger.info("WebDriver initiated")

        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 20)
        logger.info("webdriver initiated")


    def login(self, url, username, password):
        try :
            self.driver.get(url)
            self.wait.until(EC.element_to_be_clickable((By.XPATH,url_xpaths.username_xpath))).send_keys(username)
            self.wait.until(EC.element_to_be_clickable((By.XPATH,url_xpaths.password_xpath))).send_keys(password)
            self.wait.until(EC.element_to_be_clickable((By.XPATH,url_xpaths.login_button_xpath))).click()
        except Exception as e:
            logger.error(f"Error occured : {e}")

    def handling_orders(self):
        try:
            logger.info("Performing operation on products")
            self.wait.until(EC.element_to_be_clickable((By.XPATH,url_xpaths.left_hanmburger_menu_xpath))).click()
            self.wait.until(EC.element_to_be_clickable((By.XPATH,url_xpaths.dynamic_cat_xpath))).click()
            self.wait.until(EC.element_to_be_clickable((By.XPATH,url_xpaths.lazy_load_xpath))).click()
            time.sleep(2)
            count = self.wait.until(EC.presence_of_all_elements_located((By.XPATH,url_xpaths.items_on_lazy_load_xpath)))
            logger.info("Getting number of product number on page..")
            count = len(count)

            for i in range(count):
                product_name = self.wait.until(EC.element_to_be_clickable((By.XPATH,url_xpaths.item_names_xpath[i]))).text
                lazy_page_product_list.append(product_name)
        except Exception as e:
            raise


def main():
    config = ConfigParser()
    config.read("config.ini")
    username = config["credentials"]["username"]
    password = config["credentials"]["password"]
    url = "https://www.saucedemo.com"
    processor = testUrl()
    
    processor.login(url, username, password)
    processor.handling_orders()

    print(f"Products on lazy load page: {lazy_page_product_list}")

if __name__ == "__main__":
    main()