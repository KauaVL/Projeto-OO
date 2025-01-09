Sistema de Gerenciamento de Alunos e Matérias

Este é um projeto simples/mini projeto desenvolvido em Python para gerenciar alunos e matérias, utilizando entrada e saída de dados via terminal. O sistema permite realizar operações como cadastro, remoção, listagem e visualização do último item cadastrado, aplicando princípios básicos de POO (Programação Orientada a Objetos).Futuramente pretendo incrementar mais funcionalidades e a parte visual do projeto(front-end)

Funcionalidades

Gerenciamento de Alunos

Cadastrar Aluno: Permite adicionar um novo aluno, gerando automaticamente uma matrícula única.

Remover Aluno: Remove um aluno do sistema com base na matrícula.

Listar Alunos: Exibe todos os alunos cadastrados, incluindo matrícula, nome e email.

Exibir Último Aluno Cadastrado: Mostra os detalhes do último aluno registrado.

Gerenciamento de Matérias

Cadastrar Matéria: Permite adicionar uma nova matéria ao sistema.

Remover Matéria: Remove uma matéria com base no código fornecido.

Listar Matérias: Exibe todas as matérias cadastradas com código e nome.

Exibir Última Matéria Cadastrada: Mostra os detalhes da última matéria registrada.

Estrutura do Projeto

O projeto é dividido em dois arquivos principais:

1. functions.py

Este arquivo contém:

Classes Pessoa, Aluno e Matéria, que modelam os dados.

Funções para realizar as operações de gerenciamento, como cadastro, remoção e listagem.

2. index.py

Este arquivo é o ponto de entrada do programa. Ele:

Importa as funções do arquivo functions.py.

Inicializa as estruturas de dados (dicionários para armazenar alunos e matérias).

Apresenta o menu principal e chama as funções conforme a escolha do usuário.

Tecnologias Utilizadas

Linguagem: Python 3

Exemplo de Uso

Cadastro de Aluno

----------Sistema de Gerenciamento------------
1 - Gerenciar Alunos
2 - Gerenciar Matérias
3 - Sair
--> 1

----------------------
1 - Cadastrar Aluno
2 - Remover Aluno
3 - Listar Alunos
4 - Exibir Último Aluno Cadastrado
--> 1

Nome completo do Aluno: João Silva
Gmail do Aluno: joao.silva@gmail.com
Aluno Cadastrado com Sucesso! Matrícula: 250000000

Principais Conceitos de POO Aplicados

Encapsulamento: Uso de atributos privados e métodos de acesso (getters).

Herança: Classe Aluno herda da classe Pessoa.

Polimorfismo: Método exibir implementado tanto na classe Aluno quanto na classe Materia, permitindo comportamento diferente com base no objeto.


Kauã Vale Leão
