import requests  # Biblioteca para fazer requisições HTTP
import string  # Biblioteca para manipulação de strings
import random  # Biblioteca para geração de valores aleatórios
import pytest  # Framework para testes em Python
from typing import Any  # Para tipagem de dados (não utilizado diretamente no código)

# ============================
# VARIÁVEIS GLOBAIS
# ============================
base_url = "https://demoqa.com"  # URL base da API que será testada
# Gera um nome de usuário aleatório com 6 caracteres minúsculos
username = "user_" + ''.join(random.choices(string.ascii_lowercase, k=6))
password = "StrongPassword@123"  # Senha fixa para todos os usuários de teste
token: str = ""  # Variável para armazenar o token de autenticação
user_id: str = ""  # Variável para armazenar o ID do usuário criado
isbn_list: list[str] = []  # Lista para armazenar os ISBNs dos livros selecionados


# ============================
# PASSO 2 - CRIAR USUÁRIO
# ============================
def test_create_user():
    global user_id  # Permite modificar a variável global user_id

    # Monta a URL completa para criação de usuário
    url = f"{base_url}/Account/v1/User"
    # Dados do usuário que serão enviados no corpo da requisição
    payload = {"userName": username, "password": password}
    # Cabeçalho indicando que o conteúdo é JSON
    headers = {"Content-Type": "application/json"}

    # Faz a requisição POST para criar o usuário
    response = requests.post(url, json=payload, headers=headers)
    # Exibe o status code e a resposta para debug
    print(f"[CREATE USER] {response.status_code} - {response.text}")

    # Verifica se o usuário foi criado com sucesso (status 201)
    if response.status_code == 201:
        # Extrai o userID da resposta e armazena na variável global
        user_id = response.json().get("userID")
        # Verifica se o userID foi retornado
        assert user_id, "userID não retornado!"
    elif response.status_code == 406:
        # Caso o usuário já exista (status 406)
        print("Usuário já existe.")
    else:
        # Falha no teste caso ocorra outro erro
        pytest.fail(f"Erro ao criar usuário: {response.text}")


# ============================
# PASSO 3 - GERAR TOKEN
# ============================
def test_generate_token():
    global token  # Permite modificar a variável global token

    # Monta a URL completa para geração de token
    url = f"{base_url}/Account/v1/GenerateToken"
    # Credenciais do usuário para gerar o token
    payload = {"userName": username, "password": password}
    headers = {"Content-Type": "application/json"}

    # Faz a requisição POST para gerar o token
    response = requests.post(url, json=payload, headers=headers)
    print(f"[TOKEN] {response.status_code} - {response.text}")

    # Verifica se a requisição foi bem sucedida (status 200)
    assert response.status_code == 200
    # Extrai o token da resposta e armazena na variável global
    token = response.json().get("token")
    # Verifica se o token foi retornado
    assert token, "Token não foi gerado!"


# ============================
# PASSO 4 - CONFIRMAR AUTORIZAÇÃO
# ============================
def test_authorize_user():
    # Monta a URL completa para verificação de autorização
    url = f"{base_url}/Account/v1/Authorized"
    # Credenciais do usuário para verificação
    payload = {"userName": username, "password": password}
    headers = {"Content-Type": "application/json"}

    # Faz a requisição POST para verificar autorização
    response = requests.post(url, json=payload, headers=headers)
    print(f"[AUTH USER] {response.status_code} - {response.text}")

    # Verifica se a requisição foi bem sucedida (status 200)
    assert response.status_code == 200
    # Verifica se o usuário está autorizado (resposta deve ser "true")
    assert response.text == "true"


# ============================
# PASSO 5 - LISTAR LIVROS
# ============================
def test_list_books():
    global isbn_list  # Permite modificar a variável global isbn_list

    # Monta a URL completa para listagem de livros
    url = f"{base_url}/BookStore/v1/Books"
    # Cabeçalho com o token de autorização
    headers = {"Authorization": f"Bearer {token}"}

    # Faz a requisição GET para listar os livros
    response = requests.get(url, headers=headers)
    print(f"[BOOKS] {response.status_code}")

    # Verifica se a requisição foi bem sucedida (status 200)
    assert response.status_code == 200
    # Extrai a lista de livros da resposta
    books = response.json().get("books", [])
    # Verifica se há pelo menos 2 livros disponíveis
    assert len(books) >= 2, "Menos de 2 livros disponíveis"

    # Armazena os ISBNs dos dois primeiros livros na lista global
    isbn_list = [books[0]["isbn"], books[1]["isbn"]]


# ============================
# PASSO 6 - ALUGAR LIVROS
# ============================
def test_rent_books():
    global user_id  # Permite modificar a variável global user_id

    # Verifica se o user_id está vazio (não foi definido anteriormente)
    if not user_id:
        # Se estiver vazio, faz uma requisição GET para obter o userID
        response = requests.get(
            f"{base_url}/Account/v1/User/{username}",
            headers={"Authorization": f"Bearer {token}"}
        )
        user_id = response.json().get("userId")

    # Monta a URL completa para alugar livros
    url = f"{base_url}/BookStore/v1/Books"
    # Cabeçalhos com token de autorização e tipo de conteúdo
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }

    # Monta o payload com o userID e a lista de ISBNs dos livros a serem alugados
    payload = {
        "userId": user_id,
        "collectionOfIsbns": [{"isbn": isbn} for isbn in isbn_list]
    }

    # Faz a requisição POST para alugar os livros
    response = requests.post(url, json=payload, headers=headers)
    print(f"[RENT BOOKS] {response.status_code} - {response.text}")

    # Verifica se os livros foram alugados com sucesso (status 201)
    assert response.status_code == 201


# ============================
# PASSO 7 - DETALHES DO USUÁRIO
# ============================
def test_get_user_details():
    # Monta a URL completa para obter detalhes do usuário
    url = f"{base_url}/Account/v1/User/{user_id}"
    # Cabeçalho com o token de autorização
    headers = {"Authorization": f"Bearer {token}"}

    # Faz a requisição GET para obter os detalhes do usuário
    response = requests.get(url, headers=headers)
    print(f"[USER DETAILS] {response.status_code} - {response.text}")

    # Verifica se a requisição foi bem sucedida (status 200)
    assert response.status_code == 200
    # Extrai os dados do usuário da resposta
    user_data = response.json()
    # Verifica se o userID retornado é o mesmo que foi armazenado
    assert user_data["userId"] == user_id
    # Obtém a lista de livros alugados pelo usuário
    rented_books = user_data.get("books", [])
    # Verifica se o usuário alugou pelo menos 2 livros
    assert len(rented_books) >= 2
