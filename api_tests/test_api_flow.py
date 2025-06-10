# api_tests/test_api_flow.py
import requests
import pytest
import string
import random

# Gera um username aleatório para evitar conflitos
def generate_username():
    return "user_" + ''.join(random.choices(string.ascii_lowercase + string.digits, k=6))

# Dados compartilhados entre os testes
username = generate_username()
password = "StrongPassword@123"
token = None

def test_create_user():
    url = "https://demoqa.com/Account/v1/User"
    payload = {
        "userName": username,
        "password": password
    }
    headers = {
        "Content-Type": "application/json"
    }

    response = requests.post(url, json=payload, headers=headers)

    print(f"[CREATE USER] Status Code: {response.status_code}")
    print(f"[CREATE USER] Response: {response.text}")

    assert response.status_code in [201, 406], "Código de status inesperado"

def test_generate_token():
    url = "https://demoqa.com/Account/v1/GenerateToken"
    payload = {
        "userName": username,
        "password": password
    }
    headers = {
        "Content-Type": "application/json"
    }

    response = requests.post(url, json=payload, headers=headers)

    print(f"[GENERATE TOKEN] Status Code: {response.status_code}")
    print(f"[GENERATE TOKEN] Response: {response.text}")

    assert response.status_code == 200, "Falha ao gerar token"

    json_data = response.json()
    global token
    token = json_data.get("token")
    print(f"[GENERATE TOKEN] Token gerado: {token}")
    assert token is not None, "Token não encontrado na resposta"

def test_authorize_user():
    url = "https://demoqa.com/Account/v1/Authorized"
    payload = {"userName": username, "password": password}
    headers = {"Content-Type": "application/json"}

    response = requests.post(url, json=payload, headers=headers)
    print(f"[AUTHORIZE USER] {response.status_code} - {response.text}")

    assert response.status_code == 200
    assert response.text == "true"

def test_list_books():
    global isbn_list
    url = "https://demoqa.com/BookStore/v1/Books"
    headers = {"Authorization": f"Bearer {token}"}

    response = requests.get(url, headers=headers)
    print(f"[LIST BOOKS] {response.status_code}")
    print(response.json())

    assert response.status_code == 200

    books = response.json().get("books", [])
    assert len(books) >= 2, "Menos de 2 livros disponíveis"

    # Armazena dois ISBNs
    isbn_list = [books[0]["isbn"], books[1]["isbn"]]
