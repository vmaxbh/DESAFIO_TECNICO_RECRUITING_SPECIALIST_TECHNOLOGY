# language: pt
Funcionalidade: Formulário de Prática
  Como um usuário do sistema
  Eu quero preencher um formulário de prática
  Para testar diferentes tipos de campos

  Cenário: Navegação para o formulário de prática
    Dado que estou na página inicial do DemoQA
    Quando eu clicar no card "Forms"
    E clicar no submenu "Practice Form"
    Então devo ser redirecionado para a página do formulário de prática

  Cenário: Preencher formulário com dados válidos
    Dado que estou na página do formulário de prática
    Quando eu preencher o campo "First Name" com um nome válido
    E preencher o campo "Last Name" com um sobrenome válido
    E preencher o campo "Email" com um email válido
    E selecionar um gênero
    E preencher o campo "Mobile" com um número válido
    E preencher o campo "Current Address" com um endereço válido
    E selecionar um hobby
    E selecionar uma matéria
    E selecionar um estado
    E selecionar uma cidade
    E clicar no botão "Submit"
    Então devo ver a mensagem "Thanks for submitting the form"
    E os dados submetidos devem ser exibidos corretamente
