from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains # Importa ActionChains
from selenium.common.exceptions import TimeoutException, NoSuchElementException, ElementClickInterceptedException, WebDriverException
import time

# Mapeamento para converter texto para número para comparação/validação
# Isso é necessário porque 'One' e 'Two' são strings, precisamos compará-los numericamente
TEXT_TO_NUMBER = {
    "One": 1,
    "Two": 2,
    "Three": 3,
    "Four": 4,
    "Five": 5,
    "Six": 6
}

class TestInteractions:
    def test_sortable_list(self, base_page):
        """
        2.2.5 - Automação de Frontend (Interactions - Sortable - List Tab)
        Testa a funcionalidade de ordenar elementos arrastáveis na aba 'List'.
        """
        print("\n--- Iniciando Teste: 2.2.5 Interactions - Sortable (List) ---")

        # ======================================================================
        # PASSO 1: Acessar o Site e Navegar para Interactions - Sortable
        # ======================================================================
        print("--- Executando PASSO 1: Acessar o Site e Navegar para Interactions - Sortable ---")

        # PASSO 1.1: Navegar para https://demoqa.com/
        print("PASSO 1.1: Navegando para https://demoqa.com/")
        try:
            base_page.driver.get("https://demoqa.com/")
            print("PASSO 1.1: Site 'demoqa.com' acessado com sucesso.")
        except WebDriverException as e:
            # Se não conseguir acessar o site, é um erro fatal para o teste
            print(f"ERRO FATAL NO PASSO 1.1: Não foi possível acessar o site. Detalhes: {e}")
            raise # Lança a exceção para falhar o teste

        # **Ações de Preparação (Não listadas explicitamente, mas úteis)**
        # Tenta remover o elemento 'fixedban' que pode estar interceptando cliques
        try:
            base_page.driver.execute_script("document.getElementById('fixedban').remove();")
            print("PREPARAÇÃO: Elemento 'fixedban' removido com sucesso (se existia).")
        except Exception as e:
            print(f"AVISO NA PREPARAÇÃO: Não foi possível remover o elemento 'fixedban'. Detalhes: {e}")

        # Tenta rolar a página para o elemento "Interactions" ficar visível
        interactions_card_locator = (By.XPATH, "//h5[text()='Interactions']")
        try:
            interactions_card_element = base_page.find_element(interactions_card_locator)
            if interactions_card_element:
                base_page.driver.execute_script("arguments[0].scrollIntoView(true);", interactions_card_element)
                time.sleep(1) # Pequeno delay para o scroll completar
                print("PREPARAÇÃO: Página rolada para o card 'Interactions'.")
            else:
                 print("AVISO NA PREPARAÇÃO: Elemento 'Interactions' não encontrado para scroll.")
        except Exception as e:
            print(f"AVISO/ERRO NA PREPARAÇÃO: Não foi possível rolar a página para o card 'Interactions'. Detalhes: {e}")
        # Fim das Ações de Preparação

        # PASSO 1.2: Localizar e clicar na opção "Interactions"
        interactions_card_locator_click = (By.XPATH, "//h5[text()='Interactions']")
        try:
            print("PASSO 1.2: Localizando e clicando no card 'Interactions'.")
            base_page.click_element(interactions_card_locator_click)
            print("PASSO 1.2: Clicou no card 'Interactions'.")
            base_page.capture_screenshot("Interactions", "test_sortable_list", "1.2_Clicked_Interactions")
        except Exception as e:
            print(f"ERRO NO PASSO 1.2: Não foi possível clicar no card 'Interactions'. Detalhes: {e}")
            raise # Lança a exceção para falhar o teste

        # PASSO 1.3: Localizar e clicar no submenu "Sortable"
        sortable_menu_locator = (By.XPATH, "//span[text()='Sortable']")
        try:
            print("PASSO 1.3: Localizando e clicando no submenu 'Sortable'.")
            base_page.click_element(sortable_menu_locator)
            print("PASSO 1.3: Clicou no submenu 'Sortable'.")
            base_page.capture_screenshot("Interactions", "test_sortable_list", "1.3_Clicked_Sortable_Menu")
        except Exception as e:
            print(f"ERRO NO PASSO 1.3: Não foi possível clicar no submenu 'Sortable'. Detalhes: {e}")
            raise # Lança a exceção para falhar o teste

        # Verificação: Esperar que a página Sortable esteja carregada (lista visível)
        sortable_list_container_locator = (By.ID, "sortableContainer")
        print("VERIFICAÇÃO PASSO 1: Esperando o container da lista Sortable ficar visível.")
        try:
            WebDriverWait(base_page.driver, 10).until(
                EC.visibility_of_element_located(sortable_list_container_locator)
            )
            print("VERIFICAÇÃO PASSO 1: Container da lista Sortable está visível. Navegação bem-sucedida.")
            base_page.capture_screenshot("Interactions", "test_sortable_list", "1.4_On_Sortable_Page")
        except TimeoutException:
            print("FALHA NA VERIFICAÇÃO PASSO 1: Container da lista Sortable não ficou visível após 10 segundos.")
            assert False, "Não foi possível carregar a página Sortable (container da lista não visível)."
        except Exception as e:
            print(f"ERRO NA VERIFICAÇÃO PASSO 1: {e}")
            assert False, f"Erro ao verificar a página Sortable: {e}"

        print("--- Fim do PASSO 1 ---")
        print("-" * 20) # Separador

        # ======================================================================
        # PASSO 2: Organizar Elementos em Ordem Crescente (List Tab)
        # ======================================================================
        print("--- Executando PASSO 2: Organizar Elementos em Ordem Crescente ---")

        sortable_items_locator = (By.CSS_SELECTOR, "#demo-tabpane-list .list-group-item")

        # PASSO 2.1: Identificar os elementos arrastáveis na lista.
        print("PASSO 2.1: Identificando os elementos arrastáveis.")
        try:
             # Espera que pelo menos 6 elementos da lista estejam presentes e visíveis
             WebDriverWait(base_page.driver, 10).until(
                 EC.visibility_of_all_elements_located(sortable_items_locator)
             )
             elements = base_page.driver.find_elements(*sortable_items_locator)
             print(f"PASSO 2.1: {len(elements)} elementos arrastáveis identificados.")
             # Capturar a ordem inicial (geralmente já está ordenada na aba List)
             initial_order = [el.text for el in elements]
             print(f"PASSO 2.1: Ordem inicial dos elementos: {initial_order}")
             base_page.capture_screenshot("Interactions", "test_sortable_list", "2.1_Initial_Order")

        except TimeoutException:
            print("ERRO NO PASSO 2.1: Os elementos arrastáveis não ficaram visíveis ou não foram encontrados.")
            assert False, "Não foi possível encontrar os elementos arrastáveis na lista."
        except Exception as e:
            print(f"ERRO NO PASSO 2.1: {e}")
            assert False, f"Erro ao identificar elementos arrastáveis: {e}"


        # PASSO 2.2: Implementar a lógica de arrastar e soltar (drag and drop)
        # para organizar os elementos em ordem crescente.
        # Na aba "List", os elementos já vêm em ordem crescente.
        # Para demonstrar a funcionalidade, vamos executar uma lógica de ordenação
        # que, se a lista já estiver ordenada, não fará D&D, mas se estiver bagunçada, irá ordenar.
        # Usaremos uma lógica tipo Bubble Sort com ActionChains.
        print("PASSO 2.2: Implementando lógica de Drag and Drop para ordenar (Bubble Sort).")

        n = len(elements)
        # Criar uma cópia dos elementos para usar no loop de ordenação
        # Precisamos re-obter os elementos dentro do loop se ActionChains modificar o DOM
        # No entanto, re-obter tudo N*N vezes é ineficiente. Uma alternativa é usar offsets,
        # mas dropar *em* outro elemento é mais robusto para inserção na lista.
        # Vamos re-obter os elementos no início de cada 'passada' principal do bubble sort.

        try:
            # Loop externo para as passadas do bubble sort
            for i in range(n - 1):
                # Re-obter elementos para ter referências atualizadas
                elements = base_page.driver.find_elements(*sortable_items_locator)
                # Loop interno para comparações e trocas
                for j in range(n - 1 - i):
                    element_j = elements[j]
                    element_j_plus_1 = elements[j+1]

                    text_j = element_j.text
                    text_j_plus_1 = element_j_plus_1.text

                    # Converter para número para comparação (usando o mapa)
                    num_j = TEXT_TO_NUMBER.get(text_j, float('inf')) # Use inf para textos desconhecidos
                    num_j_plus_1 = TEXT_TO_NUMBER.get(text_j_plus_1, float('inf'))

                    # Se o elemento j for 'maior' que o elemento j+1 (fora de ordem crescente)
                    if num_j > num_j_plus_1:
                        print(f"PASSO 2.2: Desordenado encontrado: '{text_j}' (Pos {j}) > '{text_j_plus_1}' (Pos {j+1}). Realizando Drag & Drop.")
                        # Drag element_j_plus_1 and drop on element_j to swap them (insert j+1 before j)
                        ActionChains(base_page.driver)\
                            .drag_and_drop(element_j_plus_1, element_j)\
                            .perform()
                        print(f"PASSO 2.2: Drag & Drop realizado: '{text_j_plus_1}' movido antes de '{text_j}'.")
                        # Pequeno delay para a animação e DOM se estabilizarem
                        time.sleep(0.2)
                        # Não precisamos re-obter elementos DENTRO deste loop interno se a próxima comparação for com j+1+1
                        # Mas para segurança e para o próximo loop externo, re-obter é mais seguro.
                        # O loop interno continua, a próxima comparação será com o novo elemento na posição j+1
                        # O bubble sort compara adjacentes, então isso funciona.

                # Opcional: Capturar screenshot após cada passada externa do bubble sort
                # base_page.capture_screenshot("Interactions", "test_sortable_list", f"2.2_After_Pass_{i}")

            print("PASSO 2.2: Lógica de Drag and Drop concluída.")
            base_page.capture_screenshot("Interactions", "test_sortable_list", "2.2_After_Sorting_Logic")

        except Exception as e:
            print(f"ERRO NO PASSO 2.2: Ocorreu um erro durante a operação de Drag and Drop. Detalhes: {e}")
            assert False, f"Erro durante a operação de Drag and Drop: {e}"


        # PASSO 2.3: Validar que os elementos estão na ordem correta após a manipulação.
        print("PASSO 2.3: Validando a ordem final dos elementos.")
        expected_order = ["One", "Two", "Three", "Four", "Five", "Six"]
        final_order = []

        try:
            # Re-obter os elementos arrastáveis na ordem final
            WebDriverWait(base_page.driver, 10).until(
                 EC.visibility_of_all_elements_located(sortable_items_locator)
             )
            final_elements = base_page.driver.find_elements(*sortable_items_locator)
            final_order = [el.text for el in final_elements]
            print(f"PASSO 2.3: Ordem final observada: {final_order}")

            # Validar usando assert (para que o teste falhe se a ordem estiver errada)
            assert final_order == expected_order, \
                f"VERIFICAÇÃO PASSO 2.3: A ordem final dos elementos está incorreta. Esperado: {expected_order}, Encontrado: {final_order}"
            print("VERIFICAÇÃO PASSO 2.3: A ordem final dos elementos está correta. SUCESSO.")

        except TimeoutException:
             print("ERRO NO PASSO 2.3: Não foi possível re-obter os elementos para validação final.")
             assert False, "Não foi possível obter os elementos para validação final da ordem."
        except Exception as e:
            print(f"ERRO NO PASSO 2.3: {e}")
            assert False, f"Erro durante a validação final da ordem dos elementos: {e}"


        print("--- Fim do PASSO 2 ---")
        print("-" * 20) # Separador

        print("--- Fim do Teste: 2.2.5 Interactions - Sortable (List) ---")


