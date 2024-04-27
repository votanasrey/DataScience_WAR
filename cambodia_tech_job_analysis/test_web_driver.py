from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import os

class DataScraper:
    def __init__(self, base_path=None, driver_name=None):

        if base_path is None:
            base_path = 'D:/MIS/DataScience_WAR/cambodia_tech_job_analysis'
        if driver_name is None:
            driver_name = './driver/chromedriver.exe'
        
        self.base_path = base_path
        self.driver_path = os.path.join(base_path, driver_name)
        
        options = Options()
        options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        
        service = Service(self.driver_path)
        
        try:
            self.driver = webdriver.Chrome(service=service, options=options)
        except Exception as e:
            print(f"Failed to initialize the Chrome driver: {e}")
            raise

data_scraper = DataScraper()
