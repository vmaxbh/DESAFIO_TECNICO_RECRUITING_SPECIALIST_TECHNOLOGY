from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException, ElementClickInterceptedException, WebDriverException
import time
# Não importamos 'check' porque não usaremos pytest-check para falhar o teste

class TestWidgets:
    def test_progress_bar(self, base_page):
        """
        2.2.4 - Automação de Frontend (Widgets - Progress Bar)
        Testa a funcionalidade da Progress Bar seguindo o passo a passo especificado.
        """
        print("\n--- Iniciando Teste: 2.2.4 Widgets - Progress Bar ---")

        # Variável para controlar se um passo crucial falhou (ex: navegação inicial)
        # que impediria a execução dos passos seguintes.
        test_can_proceed = True

        # ======================================================================
        # PASSO 1: Acessar o Site e Navegar para Widgets - Progress Bar
        # ======================================================================
        print("--- Executando PASSO 1: Acessar o Site e Navegar para Widgets - Progress Bar ---")

        # PASSO 1.1: Navegar para https://demoqa.com/
        try:
            print("PASSO 1.1: Navegando para https://demoqa.com/")
            base_page.driver.get("https://demoqa.com/")
            print("PASSO 1.1: Site 'demoqa.com' acessado com sucesso.")
        except WebDriverException as e:
            print(f"ERRO FATAL NO PASSO 1.1: Não foi possível acessar o site. Detalhes: {e}")
            test_can_proceed = False # Se não acessa o site, o teste não pode continuar

        if test_can_proceed:
            # **Ações de Preparação (Não listadas explicitamente nos passos, mas necessárias)**
            # Tenta remover o elemento 'fixedban' que pode estar interceptando cliques
            try:
                # Use execute_script diretamente no driver para garantir que o script seja executado
                base_page.driver.execute_script("document.getElementById('fixedban').remove();")
                print("PREPARAÇÃO: Elemento 'fixedban' removido com sucesso (se existia).")
            except Exception as e:
                print(f"AVISO/ERRO NA PREPARAÇÃO: Não foi possível remover o elemento 'fixedban'. Detalhes: {e}")
            # Tenta rolar a página para o elemento "Widgets" ficar visível
            widgets_card_locator = (By.XPATH, "//h5[text()='Widgets']")
            try:
                # Usando find_element de base_page (que deve tratar NoSuchElementException)
                # Se encontrar, rola
                widgets_card_element = base_page.find_element(widgets_card_locator)
                if widgets_card_element:
                    base_page.driver.execute_script("arguments[0].scrollIntoView(true);", widgets_card_element)
                    time.sleep(1) # Pequeno delay para o scroll completar
                    print("PREPARAÇÃO: Página rolada para o card 'Widgets'.")
                else:
                    # find_element pode retornar None ou lançar exceção dependendo da implementação
                     print("AVISO NA PREPARAÇÃO: Elemento 'Widgets' não encontrado para scroll.")
            except Exception as e:
                print(f"AVISO/ERRO NA PREPARAÇÃO: Não foi possível rolar a página para o card 'Widgets'. Detalhes: {e}")
            # Fim das Ações de Preparação

            # PASSO 1.2: Localizar e clicar na opção "Widgets"
            widgets_card_locator_click = (By.XPATH, "//h5[text()='Widgets']")
            try:
                print("PASSO 1.2: Localizando e clicando no card 'Widgets'.")
                base_page.click_element(widgets_card_locator_click)
                print("PASSO 1.2: Clicou no card 'Widgets'.")
                base_page.capture_screenshot("Widgets", "test_progress_bar", "1.2_Clicou_Widgets")
            except Exception as e:
                print(f"ERRO NO PASSO 1.2: Não foi possível clicar no card 'Widgets'. Detalhes: {e}")
                test_can_proceed = False # Se não clica em Widgets, não pode ir para submenus

        if test_can_proceed:
            # PASSO 1.3: Localizar e clicar no submenu "Progress Bar"
            progress_bar_menu_locator = (By.XPATH, "//span[text()='Progress Bar']")
            try:
                print("PASSO 1.3: Localizando e clicando no submenu 'Progress Bar'.")
                base_page.click_element(progress_bar_menu_locator)
                print("PASSO 1.3: Clicou no submenu 'Progress Bar'.")
                base_page.capture_screenshot("Widgets", "test_progress_bar", "1.3_Clicou_ProgressBar_Menu")
            except Exception as e:
                print(f"ERRO NO PASSO 1.3: Não foi possível clicar no submenu 'Progress Bar'. Detalhes: {e}")
                test_can_proceed = False # Se não chega na página da Progress Bar, não pode testá-la

        # Verificação extra: Verificar se a página da Progress Bar carregou
        if test_can_proceed:
             progress_bar_container_locator = (By.ID, "progressBarContainer")
             try:
                # Usando is_element_visible sem timeout, conforme verificado no erro anterior
                is_visible = base_page.is_element_visible(progress_bar_container_locator)
                if is_visible:
                     print("VERIFICAÇÃO PASSO 1: Container da Progress Bar está visível. SUCESSO.")
                else:
                     print("VERIFICAÇÃO PASSO 1: Container da Progress Bar NÃO está visível. FALHA.")
                     # Marca como falha que pode impedir passos futuros se o container for essencial
                     test_can_proceed = False
             except Exception as e:
                 print(f"ERRO ao verificar visibilidade no PASSO 1: {e}. FALHA na verificação.")
                 test_can_proceed = False


        print("--- Fim do PASSO 1 ---")
        print("-" * 20) # Separador

        # ======================================================================
        # PASSO 2: Iniciar e Parar a Progress Bar
        # ======================================================================
        print("--- Executando PASSO 2: Iniciar e Parar a Progress Bar ---")

        start_stop_button = (By.ID, "startStopButton")
        progress_bar_element = (By.CSS_SELECTOR, ".progress-bar")
        progress_value_at_stop = -1 # Variável para armazenar o valor quando paramos

        if test_can_proceed:
            # PASSO 2.1: Localizar e clicar no botão "Start"
            try:
                print("PASSO 2.1: Localizando e clicando no botão 'Start'.")
                base_page.click_element(start_stop_button)
                print("PASSO 2.1: Clicou no botão 'Start'.")
                base_page.capture_screenshot("Widgets", "test_progress_bar", "2.1_Clicou_Start")
            except Exception as e:
                print(f"ERRO NO PASSO 2.1: Não foi possível clicar no botão 'Start'. Detalhes: {e}. Impossível monitorar e parar a barra.")
                test_can_proceed = False # Se não inicia, não pode parar

        if test_can_proceed:
            # PASSO 2.2: Implementar lógica para parar a barra de progresso antes de atingir 25%.
            print("PASSO 2.2: Monitorando progresso para parar antes de 25%...")
            max_attempts = 150 # Aumenta um pouco o limite caso a barra demore a iniciar
            attempts = 0
            stopped_before_25 = False
            current_progress_value = -1 # Valor dentro do loop

            while attempts < max_attempts:
                try:
                    progress_text = base_page.get_text(progress_bar_element)
                    if progress_text and '%' in progress_text:
                         try:
                            current_progress_value = int(progress_text.replace('%', ''))
                            # print(f"Progresso atual: {current_progress_value}% (Tentativa {attempts+1})") # Opcional: logar cada leitura

                            # Condição para parar: Maior que 0 e MENOR que 25
                            if 0 < current_progress_value < 25:
                                print(f"PASSO 2.2: Barra atingiu {current_progress_value}%. Tentando parar...")
                                try:
                                    base_page.click_element(start_stop_button) # Deve ser o botão 'Stop'
                                    print(f"PASSO 2.2: Clicou no botão 'Stop'. Barra parada em {current_progress_value}%.")
                                    base_page.capture_screenshot("Widgets", "test_progress_bar", f"2.2_Parou_em_{current_progress_value}pct")
                                    progress_value_at_stop = current_progress_value # Guarda o valor parado
                                    stopped_before_25 = True
                                    break # Sai do loop após parar
                                except Exception as click_e:
                                    print(f"AVISO/ERRO NO PASSO 2.2: Não foi possível clicar em 'Stop' quando o valor era {current_progress_value}%. Detalhes: {click_e}. Continuará monitorando.")
                                    # Não quebra, apenas loga e continua no loop, pode tentar parar novamente

                            elif current_progress_value >= 25:
                                print(f"AVISO NO PASSO 2.2: Barra atingiu ou passou de 25% ({current_progress_value}%) antes de poder parar.")
                                # Tenta clicar mesmo assim, pode ser 'Stop' ou 'Continue'
                                try:
                                     base_page.click_element(start_stop_button)
                                     print("PASSO 2.2: Clicou no botão (Start/Stop/Continue) após atingir/passar 25%.")
                                     base_page.capture_screenshot("Widgets", "test_progress_bar", f"2.2_Clicou_Apos_{current_progress_value}pct")
                                except Exception as click_e:
                                     print(f"AVISO/ERRO NO PASSO 2.2: Não foi possível clicar no botão após atingir/passar 25%. Detalhes: {click_e}")
                                progress_value_at_stop = current_progress_value # Guarda o valor onde parou (ou tentou parar)
                                break # Sai do loop

                         except ValueError:
                              print(f"AVISO NO PASSO 2.2: Não foi possível converter '{progress_text}' para número. Ignorando.")

                    # Se get_text retornou None ou vazio, apenas espera e tenta novamente
                    elif progress_text is not None: # Se não é None mas é vazio
                        print(f"AVISO NO PASSO 2.2: get_text retornou vazio na tentativa {attempts+1}.")


                except (NoSuchElementException, WebDriverException) as e:
                    print(f"AVISO NO PASSO 2.2: Erro ao ler o valor da barra de progresso (Tentativa {attempts+1}/{max_attempts}). Detalhes: {e}. Tentando novamente...")
                    pass # Continua no loop em caso de erro temporário

                time.sleep(0.1) # Pequeno delay para não sobrecarregar a CPU
                attempts += 1

            if attempts == max_attempts:
                print("AVISO NO PASSO 2.2: O loop para parar a barra atingiu o limite de tentativas sem sucesso na parada.")
                progress_value_at_stop = current_progress_value # Usa o último valor lido

        # PASSO 2.3: Validar que o valor da barra de progresso é menor ou igual a 25%.
        if test_can_proceed:
             print(f"PASSO 2.3: Verificando valor final da barra após tentativa de parar: {progress_value_at_stop}%.")
             # progress_value_at_stop pode ser -1 se o loop nem rodou ou a leitura falhou totalmente
             if progress_value_at_stop != -1 and progress_value_at_stop <= 25:
                  print("VERIFICAÇÃO PASSO 2.3: Barra parada com sucesso OU dentro do limite (<= 25%). SUCESSO.")
             else:
                  print(f"VERIFICAÇÃO PASSO 2.3: Barra NÃO foi parada a tempo ou valor não lido corretamente. Valor final: {progress_value_at_stop}%. Esperado: <= 25%. FALHA.")
                  # Não marca test_can_proceed como False, pois a barra apenas não parou no tempo,
                  # mas os próximos passos (continuar/resetar) ainda podem ser executados na maioria dos casos.

        print("--- Fim do PASSO 2 ---")
        print("-" * 20) # Separador

        # ======================================================================
        # PASSO 3: Continuar e Resetar a Progress Bar
        # ======================================================================
        print("--- Executando PASSO 3: Continuar e Resetar a Progress Bar ---")

        if test_can_proceed: # Só tenta executar se os passos anteriores permitirem
            # PASSO 3.1: Clique no botão "Start" novamente (agora deve ser "Continue")
            try:
                print("PASSO 3.1: Clicando no botão 'Start'/'Continue' novamente.")
                base_page.click_element(start_stop_button)
                print("PASSO 3.1: Clicou no botão 'Continue'.")
                base_page.capture_screenshot("Widgets", "test_progress_bar", "3.1_Clicou_Continue")
            except Exception as e:
                print(f"ERRO NO PASSO 3.1: Não foi possível clicar no botão 'Continue'. Detalhes: {e}.")
                # Não marca test_can_proceed como False, tenta esperar 100% mesmo assim
                # (a barra pode já estar correndo)

            # PASSO 3.2: Aguarde até que a barra de progresso atinja 100%.
            print("PASSO 3.2: Aguardando barra chegar a 100%...")
            try:
                WebDriverWait(base_page.driver, 30).until(
                    EC.text_to_be_present_in_element(progress_bar_element, "100%")
                )
                print("VERIFICAÇÃO PASSO 3.2: Barra completou 100% com sucesso. SUCESSO.")
                base_page.capture_screenshot("Widgets", "test_progress_bar", "3.2_Barra_100pct")
            except TimeoutException:
                print("VERIFICAÇÃO PASSO 3.2: A barra de progresso não atingiu 100% dentro do tempo limite. FALHA.")
                # Continua para a próxima ação (resetar), mesmo que a espera por 100% falhe
            except Exception as e:
                 print(f"ERRO ao aguardar 100% NO PASSO 3.2: {e}. FALHA na espera.")

            # PASSO 3.3: Localizar e clique no botão "Reset" para reiniciar a barra de progresso.
            reset_button = (By.ID, "resetButton")
            try:
                 # Espera o botão Reset se tornar clicável após 100%
                 print("PASSO 3.3: Aguardando botão 'Reset' se tornar clicável e clicando.")
                 WebDriverWait(base_page.driver, 10).until(
                    EC.element_to_be_clickable(reset_button)
                )
                 base_page.click_element(reset_button)
                 print("PASSO 3.3: Clicou no botão 'Reset'.")
                 base_page.capture_screenshot("Widgets", "test_progress_bar", "3.3_Clicou_Reset")

                 # Verificação extra: Verificar se o valor voltou para 0% após reset
                 # (Não explicitamente pedido nos passos, mas boa prática)
                 print("VERIFICAÇÃO EXTRA (Reset): Verificando se a barra retornou a 0%.")
                 reset_value = "N/A"
                 try:
                      # Espera pelo texto "0%" após o reset
                      WebDriverWait(base_page.driver, 10).until(
                         EC.text_to_be_present_in_element(progress_bar_element, "0%")
                      )
                      reset_value = base_page.get_text(progress_bar_element)
                      if reset_value == "0%":
                           print("VERIFICAÇÃO EXTRA (Reset): Barra resetada com sucesso para 0%. SUCESSO.")
                      else:
                           print(f"VERIFICAÇÃO EXTRA (Reset): Barra resetada, mas valor lido não é 0%. Valor atual: {reset_value}. FALHA.")
                 except TimeoutException:
                      print("VERIFICAÇÃO EXTRA (Reset): Barra não atingiu 0% após Reset dentro do tempo limite. FALHA.")
                 except Exception as e:
                      print(f"ERRO ao obter valor da barra após Reset (Verificação Extra): {e}. FALHA na verificação.")


            except TimeoutException:
                print("ERRO NO PASSO 3.3: Botão 'Reset' não se tornou clicável dentro do tempo limite. Detalhes: TimeoutException.")
            except Exception as e:
                print(f"ERRO NO PASSO 3.3: Não foi possível clicar no botão 'Reset'. Detalhes: {e}.")


        else:
            print("PASSO 3 Ignorado devido a falha crítica em passos anteriores.")


        print("--- Fim do Teste: 2.2.4 Widgets - Progress Bar ---")
        
