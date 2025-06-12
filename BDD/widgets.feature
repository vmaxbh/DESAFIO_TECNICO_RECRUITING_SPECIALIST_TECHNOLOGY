# language: pt
Funcionalidade: Progress Bar
  Como um usuário do sistema
  Eu quero interagir com a barra de progresso
  Para testar sua funcionalidade

  Cenário: Navegação para Progress Bar
    Dado que estou na página inicial do DemoQA
    Quando eu clicar no card "Widgets"
    E clicar no submenu "Progress Bar"
    Então devo ser redirecionado para a página de Progress Bar

  Cenário: Controlar a barra de progresso
    Dado que estou na página de Progress Bar
    Quando eu clicar no botão "Start"
    E aguardar até que o progresso seja menor que 25%
    E clicar no botão "Stop"
    Então a barra deve parar antes de atingir 25%
    Quando eu clicar no botão "Start" novamente
    Então a barra deve continuar de onde parou
    E ao atingir 100%
    E clicar no botão "Reset"
    Então a barra deve voltar para 0%
