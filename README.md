# Calculadora Python

## Introdução:

  Objetivo do documento: Explicar de forma completa a arquitetura, classes, módulos e funcionamento técnico de todos os aspectos da aplicação calculadora desenvolvida em Python com PySide6. Permitir o total entendimento do código por outros desenvolvedores.
  Visão geral da aplicação: Aplicação desktop com interface gráfica para realizar cálculos básicos. Permite adição, subtração, multiplicação e divisão de números inteiros e decimais. Desenvolvida com Python utilizando o framework Qt via biblioteca PySide6 para interface gráfica. Organizada em módulos separados por responsabilidade.

## Arquitetura:

  Módulos e componentes: main.py, display.py, buttons.py, info.py, utils.py, variables.py. Cada um contém classes e funções relacionadas à sua responsabilidade.
  Fluxo de execução: Inicia em main.py, que importa as classes dos módulos e cria os widgets. Interação entre módulos ocorre por signals e slots.

## Análise dos Módulos:

  main.py: Ponto de entrada, imports, criação da janela e widgets, exibição do app.
  display.py: Classe Display, exibe entrada do usuário e operandos. Métodos para interagir com input e limpar display. Emite sinais para outros módulos.
  buttons.py: Classe ButtonsGrid, cria os botões e lógica por trás deles. Conecta slots aos sinais do Display. Faz contas e emite erros.
  info.py: Classe simples para exibir equação atual.
  utils.py: Funções auxiliares reutilizáveis.
  variables.py: Constantes usadas no projeto.

## Considerações Finais:

  Tecnologias: Python, Qt, PySide6, Qt Material para estilo.
  Padrões de projeto: Signals e slots para desacoplamento.
  Pontos positivos: Código coeso, baixo acoplamento, fácil manutenção.
  Limitações: Apenas calculadora simples, sem recursos avançados.

