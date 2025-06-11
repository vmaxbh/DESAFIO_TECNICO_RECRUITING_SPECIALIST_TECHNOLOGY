import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import os
import time

class BasePage:
    """Classe base para encapsular métodos comuns de interação com elementos web."""

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def find_element(self, by_locator):
        return self.wait.until(EC.visibility_of_element_located(by_locator))

    def click_element(self, by_locator):
        """Clica em um elemento após ele se tornar clicável, rolando até ele antes."""
        element = self.wait.until(EC.element_to_be_clickable(by_locator))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        time.sleep(0.3)  # pequeno delay para garantir estabilidade
        element.click()


    def type_text(self, by_locator, text):
        element = self.find_element(by_locator)
        element.clear()
        element.send_keys(text)

    def get_text(self, by_locator):
        return self.find_element(by_locator).text

    def is_element_visible(self, by_locator):
        try:
            self.wait.until(EC.visibility_of_element_located(by_locator))
            return True
        except:
            return False

    def switch_to_new_window(self):
        self.wait.until(EC.number_of_windows_to_be(2))
        self.driver.switch_to.window(self.driver.window_handles[1])

    def switch_to_original_window(self):
        self.driver.switch_to.window(self.driver.window_handles[0])

    def close_current_window(self):
        self.driver.close()

    def capture_screenshot(self, cenario, id_test, step_name):
        folder_name = os.path.join("Screenshot", cenario, id_test)
        if not os.path.exists(folder_name):
            os.makedirs(folder_name)
        timestamp = time.strftime("%Y%m%d_%H%M%S")
        screenshot_path = os.path.join(folder_name, f"{step_name}_{timestamp}.png")
        self.driver.save_screenshot(screenshot_path)
        print(f"Screenshot salva em: {screenshot_path}")

    def action_keys(self, by_locator, key=Keys.TAB, repeat=1):
        element = self.driver.find_element(*by_locator)
        for _ in range(repeat):
            element.send_keys(key)

    def fill_field(self, by_locator, text, clear=True, timeout=10):
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(by_locator)
            )
            if clear:
                element.clear()
            element.send_keys(text)
        except Exception as e:
            raise Exception(f"Falha ao preencher campo {by_locator}: {str(e)}")

    def fill_subjects_field(self, subjects):
        try:
            input_field = self.find_element((By.CSS_SELECTOR, "#subjectsInput"))
            for subject in subjects.split(","):
                input_field.send_keys(subject.strip())
                time.sleep(0.5)
                input_field.send_keys(Keys.ENTER)
                time.sleep(0.3)
        except Exception as e:
            raise Exception(f"Falha ao preencher campo de Subjects: {str(e)}")

    def select_state(self, state_name="NCR"):
        try:
            state_container = self.find_element((By.ID, "state"))
            self.driver.execute_script("arguments[0].scrollIntoView(true);", state_container)
            time.sleep(0.5)
            dropdown_arrow = state_container.find_element(By.CSS_SELECTOR, "div.css-1wy0on6")
            ActionChains(self.driver).move_to_element(dropdown_arrow).click().perform()
            time.sleep(0.5)
            options = self.driver.find_elements(By.CSS_SELECTOR, "div.css-1n7v3ny-option")
            for option in options:
                if option.text.strip() == state_name:
                    ActionChains(self.driver).move_to_element(option).click().perform()
                    return
            input_field = state_container.find_element(By.CSS_SELECTOR, "input")
            input_field.send_keys(state_name)
            time.sleep(0.5)
            input_field.send_keys(Keys.ENTER)
        except Exception as e:
            raise Exception(f"Falha ao selecionar o estado '{state_name}': {str(e)}")

    def select_city(self, city_name="Delhi"):
        try:
            city_container = self.find_element((By.ID, "city"))
            self.driver.execute_script("arguments[0].scrollIntoView(true);", city_container)
            time.sleep(0.5)
            dropdown_arrow = city_container.find_element(By.CSS_SELECTOR, "div.css-1wy0on6")
            ActionChains(self.driver).move_to_element(dropdown_arrow).click().perform()
            time.sleep(0.5)
            options = self.driver.find_elements(By.CSS_SELECTOR, "div.css-1n7v3ny-option")
            for option in options:
                if option.text.strip() == city_name:
                    ActionChains(self.driver).move_to_element(option).click().perform()
                    return
            input_field = city_container.find_element(By.CSS_SELECTOR, "input")
            input_field.send_keys(city_name)
            time.sleep(0.5)
            input_field.send_keys(Keys.ENTER)
        except Exception as e:
            raise Exception(f"Falha ao selecionar a cidade '{city_name}': {str(e)}")


@pytest.fixture(scope="function")
def setup_browser():
    """Fixture para configurar o WebDriver com suporte a modo headless."""
    driver = None
    try:
        chrome_options = webdriver.ChromeOptions()
        if os.getenv("HEADLESS", "false").lower() == "true":
            chrome_options.add_argument("--headless")
            chrome_options.add_argument("--disable-gpu")
            chrome_options.add_argument("--window-size=1920,1080")
            chrome_options.add_argument("--no-sandbox")
            chrome_options.add_argument("--disable-dev-shm-usage")

        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=chrome_options)
        driver.maximize_window()
        yield driver
    finally:
        if driver:
            driver.quit()


@pytest.fixture(scope="function")
def base_page(setup_browser):
    """Fixture que fornece uma instância de BasePage para os testes."""
    return BasePage(setup_browser)
