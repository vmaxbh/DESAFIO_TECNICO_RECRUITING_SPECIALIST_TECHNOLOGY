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
        base_page.click_element((By.XPATH, "//h5[text()=\'Forms\']"))
        base_page.capture_screenshot("2.2.2_Forms", "test_navigate_to_forms_page", "Clicou no card 'Forms'")
        base_page.click_element((By.XPATH, "//span[text()=\'Practice Form\']"))
        base_page.capture_screenshot("2.2.2_Forms", "test_navigate_to_forms_page", "Clicou no submenu 'Practice Form'")
        assert "Practice Form" in base_page.driver.current_url or base_page.is_element_visible((By.ID, "userForm"))
        print("Navegação para 'Practice Form' concluída com sucesso!")
        # ============================
        # PASSO 3 - Preencher o Formulário com Valores Aleatórios.
        # ============================
        base_page.fill_field((By.ID, "firstName"), dados["Nome"])
        base_page.fill_field((By.ID, "lastName"), dados["Sobrenome"])
        base_page.fill_field((By.ID, "userEmail"), dados["Email"])
        base_page.capture_screenshot("2.2.2_Forms", "test_forms_flow", "Preencheu o Formulário com Nomes e Email Aleatórios")
        base_page.click_element((By.XPATH, '//*[@id="genterWrapper"]/div[2]/div[1]/label'))
        base_page.click_element((By.XPATH, "//h1[contains(text(), 'Practice Form')]"))
        base_page.action_keys((By.ID, "userEmail"), Keys.PAGE_DOWN, repeat=1)
        base_page.click_element((By.XPATH, '//*[@id="hobbiesWrapper"]/div[2]/div[1]/label'))
        base_page.fill_field((By.ID, "userNumber"), dados["Telefone"])
        base_page.fill_field((By.ID, "currentAddress"), dados["Endereco"])
        base_page.action_keys((By.ID, "userEmail"), Keys.TAB, repeat=3)
        base_page.fill_subjects_field("Maths, Physics")
        base_page.select_state("NCR")
        base_page.select_city("Delhi")
        base_page.capture_screenshot("2.2.2_Forms", "test_forms_flow", "Preencheu o Formulário com Valores Aleatórios")
        # ============================
        # PASSO 4 - Submeter o Formulário.
        # ============================
        base_page.click_element((By.ID, "submit"))
        base_page.capture_screenshot("2.2.2_Forms", "test_forms_flow", "Submeteu o Formulário")
        # ============================
        # PASSO 5 - Verificar se o Formulário foi submetido com sucesso.
        # ============================
        assert "Thanks for submitting the form" in base_page.driver.page_source
        print("Formulário submetido com sucesso!")

