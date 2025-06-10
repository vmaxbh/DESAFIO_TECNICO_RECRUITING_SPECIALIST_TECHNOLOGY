from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from faker import Faker
import random
from datetime import datetime

# Configura o Faker para dados em português do Brasil
fake = Faker('pt_BR')
dados = {
    "Nome": fake.first_name(),
    "Sobrenome": fake.last_name(),
    "Email": fake.email(),
    "Telefone": fake.numerify(text='##########'),
    "Cidade": fake.city(),
    "Estado": fake.estado_nome(),
    "Endereco": fake.address(),
    "subjects": fake.random_element(elements=("Maths", "Physics", "Chemistry", "Biology", "History", "English", "Computer Science"))
}

class TestForms:

    def test_forms_flow(self, base_page):
        # ============================
        # PASSO 2 - Testa a navegação para a página de formulários.
        # ============================
        base_page.driver.get("https://demoqa.com/" )

        # Clica no card 'Forms'
        base_page.click_element((By.XPATH, "//h5[text()=\'Forms\']"))
        base_page.capture_screenshot("Forms", "test_navigate_to_forms_page", "Clicou no card 'Forms'")

        # Clica no submenu 'Practice Form'
        base_page.click_element((By.XPATH, "//span[text()=\'Practice Form\']"))
        base_page.capture_screenshot("Forms", "test_navigate_to_forms_page", "Clicou no submenu 'Practice Form'")

        # Opcional: Adicione uma asserção para verificar se a navegação foi bem-sucedida
        # Por exemplo, verificar se o título da página ou um elemento específico do formulário está presente.
        assert "Practice Form" in base_page.driver.current_url or base_page.is_element_visible((By.ID, "userForm"))
        print("Navegação para 'Practice Form' concluída com sucesso!")

        # ============================
        # PASSO 3 - Preencher o Formulário com Valores Aleatórios.
        # ============================
        base_page.fill_field((By.ID, "firstName"), dados["Nome"])
        base_page.fill_field((By.ID, "lastName"), dados["Sobrenome"])
        base_page.fill_field((By.ID, "userEmail"), dados["Email"])
        base_page.click_element((By.XPATH, '//*[@id="genterWrapper"]/div[2]/div[1]/label'))
        base_page.click_element((By.XPATH, '//*[@id="hobbiesWrapper"]/div[2]/div[1]/label'))
        base_page.fill_field((By.ID, "userNumber"), dados["Telefone"])
        base_page.fill_field((By.ID, "currentAddress"), dados["Endereco"])
        base_page.click_element((By.XPATH, "//label[contains(text(), 'Current Address')]"))
        base_page.click_element((By.XPATH, "//div[contains(text(), 'Select State')]"))
        base_page.fill_field((By.XPATH, "//div[contains(text(), 'Select State')]"), "NCR")
        base_page.capture_screenshot("Forms", "test_forms_flow", "Preencheu o Formulário com Valores Aleatórios")

