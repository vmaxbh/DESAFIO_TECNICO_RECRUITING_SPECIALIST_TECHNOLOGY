# 🧪 Desafio Técnico de QA - Automação de Testes

[![Python](https://img.shields.io/badge/Python-3.x-blue.svg)](https://www.python.org/)
[![Pytest](https://img.shields.io/badge/Pytest-Latest-green.svg)](https://docs.pytest.org/)
[![Selenium](https://img.shields.io/badge/Selenium-Latest-orange.svg)](https://www.selenium.dev/)

> Projeto de automação de testes para API REST e Frontend utilizando o site de demonstração [DemoQA](https://demoqa.com)

## 📋 Índice

- [Tecnologias Utilizadas](#-tecnologias-utilizadas)
- [Estrutura do Projeto](#-estrutura-do-projeto)
- [Como Executar](#-como-executar)
- [Execução dos Testes](#-execução-dos-testes)
- [Arquitetura dos Testes](#-arquitetura-dos-testes)
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
pytest --html=report.html
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

## ✅ Boas Práticas Adotadas

- 📁 Organização modular com pastas separadas
- 🧪 Estrutura de testes simples e reutilizável
- 🔒 Manipulação segura de dados e tratamento de erros
- 💡 Comentários explicativos no código
- ⏱️ Uso de waits explícitos no Selenium
- 📐 Page Object Model (POM) sugerido para crescimento do projeto

## 📌 Considerações Finais

Este projeto foi desenvolvido com foco em demonstrar habilidades práticas em automação de testes de software, cobrindo desde testes de API até interações complexas com a interface do usuário.

---

<div align="center">
  <sub>
  * Desenvolvido por Maxwell Viana
  * email: vmaxbh@gmail.com
  * telefone: (31)99494-7380
  </sub>
</div>
