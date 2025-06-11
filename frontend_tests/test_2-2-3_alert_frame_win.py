from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class TestAlertsFrameWindows:
    def test_browser_windows(self, base_page):
        """
        2.2.3 - Automação de Frontend (Alerts, Frame & Windows)
        Testa a funcionalidade de Browser Windows
        """
        # ============================
        # PASSO 1: Acessar o Site e Navegar para Alerts, Frame & Windows
        # ============================
        base_page.driver.get("https://demoqa.com/")
        base_page.click_element((By.XPATH, "//h5[text()='Alerts, Frame & Windows']"))
        base_page.capture_screenshot("2.2.3_AlertsFrameWindows", "test_browser_windows", "Clicou no card 'Alerts, Frame & Windows'")
        base_page.click_element((By.XPATH, "//span[text()='Browser Windows']"))
        base_page.capture_screenshot("2.2.3_AlertsFrameWindows", "test_browser_windows", "Clicou no submenu 'Browser Windows'")
        # Verifica se a navegação foi bem-sucedida
        assert base_page.is_element_visible((By.ID, "browserWindows"))
        print("Navegação para 'Browser Windows' concluída com sucesso!")
        # ============================
        # PASSO 2: Interagir com Nova Janela
        # ============================
        # Guarda a janela original
        original_window = base_page.driver.current_window_handle
        # Clica no botão "New Window"
        base_page.click_element((By.ID, "windowButton"))
        base_page.capture_screenshot("2.2.3_AlertsFrameWindows", "test_browser_windows", "Clicou no botão 'New Window'")
        # Aguarda a nova janela e muda o foco
        base_page.switch_to_new_window()
        # Valida a mensagem na nova janela
        sample_text = base_page.get_text((By.TAG_NAME, "body"))
        assert "This is a sample page" in sample_text
        base_page.capture_screenshot("2.2.3_AlertsFrameWindows", "test_browser_windows", "Validou mensagem na nova janela")
        print("Mensagem na nova janela validada com sucesso!")
        # Fecha a nova janela e retorna para a original
        base_page.close_current_window()
        base_page.switch_to_original_window()
        # Verifica se voltou para a janela original
        assert base_page.driver.current_window_handle == original_window
        print("Foco retornado para a janela original com sucesso!")
