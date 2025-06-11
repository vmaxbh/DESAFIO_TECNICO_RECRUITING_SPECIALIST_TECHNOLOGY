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
    def fill_field(self, by_locator, text, clear=True, timeout=10):
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(by_locator)
            )
            if clear:
                element.clear()  # Limpa apenas se clear=True
            element.send_keys(text)
        except Exception as e:
            raise Exception(f"Falha ao preencher campo {by_locator}: {str(e)}")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10) # Tempo de espera padrão de 10 segundos

    def find_element(self, by_locator):
        """Encontra um elemento usando o localizador fornecido."""
        return self.wait.until(EC.visibility_of_element_located(by_locator))

    def click_element(self, by_locator):
        """Clica em um elemento após ele se tornar clicável."""
        self.wait.until(EC.element_to_be_clickable(by_locator)).click()

    def type_text(self, by_locator, text):
        """Digita um texto em um campo de entrada."""
        element = self.find_element(by_locator)
        element.clear()
        element.send_keys(text)

    def get_text(self, by_locator):
        """Obtém o texto de um elemento."""
        element = self.find_element(by_locator)
        return element.text

    def is_element_visible(self, by_locator):
        """Verifica se um elemento está visível."""
        try:
            self.wait.until(EC.visibility_of_element_located(by_locator))
            return True
        except:
            return False

    def switch_to_new_window(self):
        """Muda o foco para a nova janela aberta."""
        self.wait.until(EC.number_of_windows_to_be(2))
        self.driver.switch_to.window(self.driver.window_handles[1])

    def switch_to_original_window(self):
        """Muda o foco de volta para a janela original."""
        self.driver.switch_to.window(self.driver.window_handles[0])

    def close_current_window(self):
        """Fecha a janela atual."""
        self.driver.close()

    def capture_screenshot(self, cenario, id_test, step_name):
        """Captura o print da tela e salva com o nome do step"""
        # Define o diretório onde as capturas de tela serão salvas
        folder_name = os.path.join("Screenshot", cenario, id_test)
        if not os.path.exists(folder_name):
            os.makedirs(folder_name)

        # Cria o caminho do arquivo baseado no step_name
        timestamp = time.strftime(
            "%Y%m%d_%H%M%S"
        )  # Adiciona timestamp para evitar sobrescrita
        screenshot_path = os.path.join(folder_name, f"{step_name}_{timestamp}.png")

        # Captura a tela
        self.driver.save_screenshot(screenshot_path)
        print(f"Screenshot salva em: {screenshot_path}")

    def action_keys(self, by_locator, key=Keys.TAB, repeat=1):
        element = self.driver.find_element(*by_locator)
        for _ in range(repeat):
            element.send_keys(key)

    def fill_subjects_field(self, subjects):
        try:
            # Localiza o campo de input dentro do subjectsContainer
            input_field = self.find_element((By.CSS_SELECTOR, "#subjectsInput"))

            # Para cada subject na lista
            for subject in subjects.split(","):
                input_field.send_keys(subject.strip())
                time.sleep(0.5)  # Espera o autocomplete aparecer
                input_field.send_keys(Keys.ENTER)
                time.sleep(0.3)

        except Exception as e:
            raise Exception(f"Falha ao preencher campo de Subjects: {str(e)}")

    def select_state(self, state_name="NCR"):
        """
        Seleciona um estado no dropdown de forma confiável
        """
        try:
            # Localiza o container principal do dropdown
            state_container = self.find_element((By.ID, "state"))

            # Rola até o elemento para garantir visibilidade
            self.driver.execute_script("arguments[0].scrollIntoView(true);", state_container)
            time.sleep(0.5)  # Pequeno delay para o scroll completar

            # Localiza o elemento clicável do dropdown (usando CSS selector mais estável)
            dropdown_arrow = state_container.find_element(By.CSS_SELECTOR, "div.css-1wy0on6")

            # Clica usando ActionChains para maior confiabilidade
            ActionChains(self.driver).move_to_element(dropdown_arrow).click().perform()
            time.sleep(0.5)  # Espera o dropdown abrir

            # Localiza todas as opções do dropdown
            options = self.driver.find_elements(By.CSS_SELECTOR, "div.css-1n7v3ny-option")

            # Procura a opção desejada
            for option in options:
                if option.text.strip() == state_name:
                    # Clica na opção encontrada
                    ActionChains(self.driver).move_to_element(option).click().perform()
                    return

            # Se não encontrou, tenta método alternativo via input
            input_field = state_container.find_element(By.CSS_SELECTOR, "input")
            input_field.send_keys(state_name)
            time.sleep(0.5)
            input_field.send_keys(Keys.ENTER)

        except Exception as e:
            raise Exception(f"Falha ao selecionar o estado '{state_name}': {str(e)}")

    def select_city(self, city_name="Delhi"):
        """
        Seleciona uma cidade no dropdown de forma confiável
        """
        try:
            # Localiza o container principal do dropdown
            city_container = self.find_element((By.ID, "city"))

            # Rola até o elemento
            self.driver.execute_script("arguments[0].scrollIntoView(true);", city_container)
            time.sleep(0.5)

            # Localiza o elemento clicável do dropdown
            dropdown_arrow = city_container.find_element(By.CSS_SELECTOR, "div.css-1wy0on6")
            ActionChains(self.driver).move_to_element(dropdown_arrow).click().perform()
            time.sleep(0.5)

            # Localiza todas as opções do dropdown
            options = self.driver.find_elements(By.CSS_SELECTOR, "div.css-1n7v3ny-option")

            # Procura a opção desejada
            for option in options:
                if option.text.strip() == city_name:
                    ActionChains(self.driver).move_to_element(option).click().perform()
                    return

            # Método alternativo se não encontrar
            input_field = city_container.find_element(By.CSS_SELECTOR, "input")
            input_field.send_keys(city_name)
            time.sleep(0.5)
            input_field.send_keys(Keys.ENTER)

        except Exception as e:
            raise Exception(f"Falha ao selecionar a cidade '{city_name}': {str(e)}")

@pytest.fixture(scope="function")
def setup_browser():
    """Fixture para configurar e derrubar o WebDriver para cada função de teste."""
    driver = None
    try:
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)
        driver.maximize_window()
        yield driver  # Fornece o driver para o teste
    finally:
        if driver:
            driver.quit() # Garante que o navegador seja fechado após o teste

@pytest.fixture(scope="function")
def base_page(setup_browser):
    """Fixture que fornece uma instância de BasePage para os testes."""
    return BasePage(setup_browser)
