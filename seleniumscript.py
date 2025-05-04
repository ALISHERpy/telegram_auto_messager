from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import requests
from bs4 import BeautifulSoup
import os
import re

class Telegram_auto_messager():
    """Appstore parser From AlisherPY"""

    def __init__(self):

        ###----------------------------------------------------------------------
        chrome_options = Options()

        # 👇 Change this path to a real folder you own
        chrome_options.add_argument(r"--user-data-dir=C:\telegramcashe")

        # 👇 Use a non-default profile (to avoid conflict with your normal Chrome)
        chrome_options.add_argument(r"--profile-directory=TelegramProfile1")

        # chrome_options.add_argument("--headless")  # Run in headless mode
        # chrome_options.add_argument("--disable-gpu")  # Disable GPU acceleration (optional)
        # chrome_options.add_argument("--no-sandbox")  # Disable sandboxing (optional)
        # self.driver = webdriver.Chrome(options=chrome_options)
        ###----------------------------------------------------------------------
        self.driver = webdriver.Chrome(options=chrome_options)
        ###----------------------------------------------------------------------
        self.driver.implicitly_wait(10)
        self.wait = WebDriverWait(self.driver, 10)

    def close_driver(self):
        print("...Driver closing...")
        self.driver.quit()

    def open_telegram_page(self, app_page_link):
        driver = self.driver
        driver.get(app_page_link)
        # Wait and click the "c-ripple" element
        ripple_btn = self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "c-ripple")))
        ripple_btn.click()

        phone_inputs = self.wait.until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, "input-field-input"))
        )
        phone_inputs[1].send_keys("998903540221")
        phone_inputs[1].send_keys(Keys.ENTER)
        time.sleep(20)

    def open_bot_chat(self, app_page_link):
        driver = self.driver
        driver.get(app_page_link)

        try:
            # Wait for the input field to be clickable
            message_space = self.wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "div.input-message-input[contenteditable='true']"))
            )
        except:
            message_space = self.wait.until(
                EC.element_to_be_clickable(
                    (By.CSS_SELECTOR, ".input-message-input.scrollable.scrollable-y.no-scrollbar.is-empty"))
            )

        message_space.click()

        for i in range(100):
            # Set and send the first message
            js_first = """
            arguments[0].innerText = '💌 / 📹';
            arguments[0].dispatchEvent(new InputEvent('input', { bubbles: true }));
            """
            self.driver.execute_script(js_first, message_space)
            message_space.send_keys(Keys.ENTER)
            time.sleep(1)  # Short delay to ensure the message is sent

            # Clear the input field
            js_clear = """
            arguments[0].innerText = '';
            arguments[0].dispatchEvent(new InputEvent('input', { bubbles: true }));
            """
            self.driver.execute_script(js_clear, message_space)
            time.sleep(0.5)  # Short delay to ensure the field is cleared

            # Set and send the second message
            js_second = """
            arguments[0].innerText = `Wouu🔥❤️❤️❤️
        @alex_pentesting`;
            arguments[0].dispatchEvent(new InputEvent('input', { bubbles: true }));
            """
            self.driver.execute_script(js_second, message_space)
            message_space.send_keys(Keys.ENTER)
            time.sleep(3)  # Delay before the next iteration

        print("✅ Message sent.")
