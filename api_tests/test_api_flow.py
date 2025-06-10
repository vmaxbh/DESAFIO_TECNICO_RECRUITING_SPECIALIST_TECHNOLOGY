import requests
import string
import random
import pytest
from typing import Any

# ============================
# VARIÁVEIS GLOBAIS
# ============================
base_url = "https://demoqa.com"
username = "user_" + ''.join(random.choices(string.ascii_lowercase, k=6))
password = "StrongPassword@123"
token: str = ""
user_id: str = ""
isbn_list: list[str] = []


# ============================
# PASSO 2 - CRIAR USUÁRIO
# ============================
def test_create_user():
    global user_id

    url = f"{base_url}/Account/v1/User"
    payload = {"userName": username, "password": password}
    headers = {"Content-Type": "application/json"}

    response = requests.post(url, json=payload, headers=headers)
    print(f"[CREATE USER] {response.status_code} - {response.text}")

    if response.status_code == 201:
        user_id = response.json().get("userID")
        assert user_id, "userID não retornado!"
    elif response.status_code == 406:
        print("Usuário já existe.")
    else:
        pytest.fail(f"Erro ao criar usuário: {response.text}")


# ============================
# PASSO 3 - GERAR TOKEN
# ============================
def test_generate_token():
    global token

    url = f"{base_url}/Account/v1/GenerateToken"
    payload = {"userName": username, "password": password}
    headers = {"Content-Type": "application/json"}

    response = requests.post(url, json=payload, headers=headers)
    print(f"[TOKEN] {response.status_code} - {response.text}")

    assert response.status_code == 200
    token = response.json().get("token")
    assert token, "Token não foi gerado!"


# ============================
# PASSO 4 - CONFIRMAR AUTORIZAÇÃO
# ============================
def test_authorize_user():
    url = f"{base_url}/Account/v1/Authorized"
    payload = {"userName": username, "password": password}
    headers = {"Content-Type": "application/json"}

    response = requests.post(url, json=payload, headers=headers)
    print(f"[AUTH USER] {response.status_code} - {response.text}")

    assert response.status_code == 200
    assert response.text == "true"


# ============================
# PASSO 5 - LISTAR LIVROS
# ============================
def test_list_books():
    global isbn_list

    url = f"{base_url}/BookStore/v1/Books"
    headers = {"Authorization": f"Bearer {token}"}

    response = requests.get(url, headers=headers)
    print(f"[BOOKS] {response.status_code}")

    assert response.status_code == 200
    books = response.json().get("books", [])
    assert len(books) >= 2, "Menos de 2 livros disponíveis"

    isbn_list = [books[0]["isbn"], books[1]["isbn"]]


# ============================
# PASSO 6 - ALUGAR LIVROS
# ============================
def test_rent_books():
    global user_id

    if not user_id:
        # Buscar userId via GET
        response = requests.get(
            f"{base_url}/Account/v1/User/{username}",
            headers={"Authorization": f"Bearer {token}"}
        )
        user_id = response.json().get("userId")

    url = f"{base_url}/BookStore/v1/Books"
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }

    payload = {
        "userId": user_id,
        "collectionOfIsbns": [{"isbn": isbn} for isbn in isbn_list]
    }

    response = requests.post(url, json=payload, headers=headers)
    print(f"[RENT BOOKS] {response.status_code} - {response.text}")

    assert response.status_code == 201


# ============================
# PASSO 7 - DETALHES DO USUÁRIO
# ============================
def test_get_user_details():
    url = f"{base_url}/Account/v1/User/{user_id}"
    headers = {"Authorization": f"Bearer {token}"}

    response = requests.get(url, headers=headers)
    print(f"[USER DETAILS] {response.status_code} - {response.text}")

    assert response.status_code == 200
    user_data = response.json()
    assert user_data["userId"] == user_id
    rented_books = user_data.get("books", [])
    assert len(rented_books) >= 2
