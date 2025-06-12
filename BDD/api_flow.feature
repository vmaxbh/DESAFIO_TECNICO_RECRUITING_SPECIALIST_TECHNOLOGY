# language: pt
Funcionalidade: Fluxo de API do Book Store
  Como um usuário do sistema
  Eu quero interagir com a API do Book Store
  Para gerenciar minha conta e livros

  Cenário: Criar novo usuário
    Dado que estou na API do Book Store
    Quando eu enviar uma requisição POST para "/Account/v1/User"
    E fornecer um nome de usuário e senha válidos
    Então devo receber um status code 201
    E um userID válido na resposta

  Cenário: Gerar token de autenticação
    Dado que tenho um usuário criado
    Quando eu enviar uma requisição POST para "/Account/v1/GenerateToken"
    E fornecer minhas credenciais
    Então devo receber um status code 200
    E um token de autenticação válido

  Cenário: Verificar autorização do usuário
    Dado que tenho um usuário criado
    Quando eu enviar uma requisição POST para "/Account/v1/Authorized"
    E fornecer minhas credenciais
    Então devo receber um status code 200
    E a resposta deve ser "true"

  Cenário: Listar livros disponíveis
    Dado que estou autenticado com um token válido
    Quando eu enviar uma requisição GET para "/BookStore/v1/Books"
    Então devo receber um status code 200
    E uma lista com pelo menos 2 livros

  Cenário: Alugar livros
    Dado que estou autenticado com um token válido
    E tenho um userID válido
    Quando eu enviar uma requisição POST para "/BookStore/v1/Books"
    E fornecer o userID e os ISBNs dos livros
    Então devo receber um status code 201
    E os livros devem ser adicionados à minha coleção

  Cenário: Obter detalhes do usuário
    Dado que estou autenticado com um token válido
    E tenho um userID válido
    Quando eu enviar uma requisição GET para "/Account/v1/User/{userID}"
    Então devo receber um status code 200
    E os detalhes do meu usuário
    E a lista dos livros que aluguei
