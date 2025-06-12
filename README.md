# 🧪 Desafio Técnico de QA - Automação de Testes

[![Python](https://img.shields.io/badge/Python-3.x-blue.svg)](https://www.python.org/)
[![Pytest](https://img.shields.io/badge/Pytest-Latest-green.svg)](https://docs.pytest.org/)
[![Selenium](https://img.shields.io/badge/Selenium-Latest-orange.svg)](https://www.selenium.dev/)
[![GitHub Actions](https://img.shields.io/badge/GitHub%20Actions-Enabled-blue.svg)](https://github.com/features/actions)

> Projeto de automação de testes para API REST e Frontend utilizando o site de demonstração [DemoQA](https://demoqa.com)

## 📋 Índice

- [Tecnologias Utilizadas](#-tecnologias-utilizadas)
- [Estrutura do Projeto](#-estrutura-do-projeto)
- [Como Executar](#-como-executar)
- [Execução dos Testes](#-execução-dos-testes)
- [CI/CD com GitHub Actions](#cicd-com-github-actions)
- [Arquitetura dos Testes](#-arquitetura-dos-testes)
- [Especificações BDD](#-especificações-bdd)
- [Boas Práticas](#-boas-práticas)
- [Considerações Finais](#-considerações-finais)

## 🔧 Tecnologias Utilizadas

### 📡 API
- **Linguagem:** Python 3.x
- **Framework de Testes:** Pytest
- **HTTP Client:** requests
- **Manipulação JSON:** json

### 🌐 Frontend (UI)
- **Framework de Testes:** Pytest
- **Automação Web:** Selenium WebDriver
- **Gerenciador de Driver:** WebDriver Manager

### 📊 Relatórios
- pytest-html ou allure-pytest (opcional, recomendável)

## 📁 Estrutura do Projeto

```
.
├── api_tests/                 # Testes automatizados de API
│   └── test_api_flow.py
│
├── frontend_tests/           # Testes automatizados de frontend
│   ├── test_forms.py
│   ├── test_alerts.py
│   ├── test_progress_bar.py
│   └── test_sortable.py
│
├── BDD/                      # Especificações BDD
│   ├── api_flow.feature
│   ├── forms.feature
│   ├── alerts_frame_windows.feature
│   ├── widgets.feature
│   └── interactions.feature
│
├── utils/                    # Funções auxiliares e dados
│   └── helpers.py
│
├── requirements.txt          # Dependências do projeto
├── README.md                 # Este arquivo
└── pytest.ini                # Configurações do Pytest (opcional)
```

## 🚀 Como Executar

### 1. Clone o Repositório
```bash
git clone https://github.com/seu-usuario/desafio-qa.git
cd desafio-qa
```

### 2. Crie e Ative o Ambiente Virtual
```bash
# Criar ambiente virtual
python -m venv venv

# Ativar ambiente virtual
# Linux/Mac
source venv/bin/activate
# Windows
venv\Scripts\activate
```

### 3. Instale as Dependências
```bash
pip install -r requirements.txt
```

## 🧪 Execução dos Testes

### Testes de API
```bash
pytest api_tests/
```

### Testes de Frontend
```bash
pytest frontend_tests/
```

### Gerar Relatório HTML (opcional)
```bash
pytest --html=relatorio_teste.html
```

## 🔄 CI/CD com GitHub Actions

O projeto está configurado com GitHub Actions para execução automática dos testes. O pipeline é executado em cada push e pull request.

### Estrutura do Pipeline

O pipeline está configurado no arquivo `.github/workflows/cicd.yml` e inclui:

1. **Configuração do Ambiente**
   - Instalação do Python 3.9
   - Instalação do Chrome e WebDriver
   - Instalação das dependências do projeto

2. **Execução dos Testes**
   - Testes de API
   - Testes de Frontend
   - Geração de relatórios HTML

3. **Configurações Especiais**
   - Modo headless para o Chrome
   - Retry automático em caso de falhas
   - Tratamento de anúncios e popups

### Como Executar no GitHub Actions

1. **Fork do Repositório**
   - Faça um fork deste repositório para sua conta GitHub

2. **Configuração do GitHub Actions**
   - O pipeline já está configurado no arquivo `.github/workflows/cicd.yml`
   - Não é necessária nenhuma configuração adicional

3. **Execução Automática**
   - Os testes serão executados automaticamente em:
     - Push para qualquer branch
     - Criação de Pull Request
     - Push para Pull Request existente

4. **Visualização dos Resultados**
   - Acesse a aba "Actions" no seu repositório
   - Clique na execução desejada
   - Visualize os logs e relatórios de teste
   - Baixe os relatórios HTML gerados

### Configurações do Pipeline

O pipeline inclui várias configurações para garantir a estabilidade dos testes:

```yaml
# Configurações do Chrome
options.add_argument('--headless')
options.add_argument('--disable-notifications')
options.add_argument('--disable-popup-blocking')

# Configurações do Pytest
reruns = 3
reruns_delay = 1
```

## 🧱 Arquitetura dos Testes

### 🔹 API - Fluxo Principal
1. Criar usuário
2. Gerar token
3. Autorizar usuário
4. Listar livros disponíveis
5. Alugar dois livros
6. Consultar dados do usuário com livros alugados

### 🔹 Frontend - Casos Automatizados
1. Preenchimento e envio do Formulário de Prática
2. Interação com Alerts, Frames e Novas Janelas
3. Testes de Barra de Progresso
4. Ordenação de elementos com Sortable

## 📝 Especificações BDD

O projeto inclui especificações BDD (Behavior Driven Development) para documentar os cenários de teste em formato Gherkin. Os arquivos estão localizados na pasta `BDD/`:

### 🔹 API Flow (`api_flow.feature`)
- Criação de usuário
- Geração de token
- Verificação de autorização
- Listagem de livros
- Aluguel de livros
- Obtenção de detalhes do usuário

### 🔹 Forms (`forms.feature`)
- Navegação para o formulário
- Preenchimento do formulário com dados válidos

### 🔹 Alerts, Frame & Windows (`alerts_frame_windows.feature`)
- Navegação para Browser Windows
- Interação com nova janela

### 🔹 Widgets (`widgets.feature`)
- Navegação para Progress Bar
- Controle da barra de progresso (start, stop, continue, reset)

### 🔹 Interactions (`interactions.feature`)
- Navegação para Sortable
- Ordenação de elementos da lista

## ✅ Boas Práticas Adotadas

- 📁 Organização modular com pastas separadas
- 🧪 Estrutura de testes simples e reutilizável
- 🔒 Manipulação segura de dados e tratamento de erros
- 💡 Comentários explicativos no código
- ⏱️ Uso de waits explícitos no Selenium
- 📐 Page Object Model (POM) sugerido para crescimento do projeto
- 📝 Documentação BDD para melhor compreensão dos cenários

## 📌 Considerações Finais

Este projeto foi desenvolvido com foco em demonstrar habilidades práticas em automação de testes de software, cobrindo desde testes de API até interações complexas com a interface do usuário. A inclusão de especificações BDD ajuda na documentação e compreensão dos cenários de teste.

---

<div align="center">
  <sub>
  * Desenvolvido por Maxwell Viana
  * email: vmaxbh@gmail.com
  * telefone: (31)99494-7380
  </sub>
</div>
