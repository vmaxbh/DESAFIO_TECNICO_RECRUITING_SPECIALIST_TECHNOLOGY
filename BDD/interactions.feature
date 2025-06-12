# language: pt
Funcionalidade: Lista Ordenável
  Como um usuário do sistema
  Eu quero interagir com elementos ordenáveis
  Para organizar itens em uma lista

  Cenário: Navegação para Sortable
    Dado que estou na página inicial do DemoQA
    Quando eu clicar no card "Interactions"
    E clicar no submenu "Sortable"
    Então devo ser redirecionado para a página de Sortable

  Cenário: Ordenar elementos da lista
    Dado que estou na página de Sortable
    E estou na aba "List"
    Quando eu identificar os elementos arrastáveis
    Então devo ver uma lista com os elementos "One" até "Six"
    Quando eu arrastar e soltar os elementos para ordená-los
    Então os elementos devem ficar em ordem crescente
    E a ordem final deve ser "One", "Two", "Three", "Four", "Five", "Six"
