# language: pt
Funcionalidade: Alerts, Frame & Windows
  Como um usuário do sistema
  Eu quero interagir com alertas, frames e janelas
  Para testar diferentes elementos da interface

  Cenário: Navegação para Browser Windows
    Dado que estou na página inicial do DemoQA
    Quando eu clicar no card "Alerts, Frame & Windows"
    E clicar no submenu "Browser Windows"
    Então devo ser redirecionado para a página de Browser Windows

  Cenário: Interagir com nova janela
    Dado que estou na página de Browser Windows
    Quando eu clicar no botão "New Window"
    Então uma nova janela deve ser aberta
    E a nova janela deve conter a mensagem "This is a sample page"
    E ao fechar a nova janela
    E retornar para a janela original
    Então devo estar na página de Browser Windows
