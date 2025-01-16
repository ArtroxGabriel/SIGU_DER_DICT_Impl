# Trabalho Pratico II

<!--toc:start-->

- [Trabalho Pratico II](#trabalho-pratico-ii)
  - [1 Atividade](#1-atividade)
  - [2 Instruções](#2-instruções)
    - [2.1 Conectando ao BD](#21-conectando-ao-bd)
    - [2.2 Criação de Tabelas](#22-criação-de-tabelas)
    - [2.3 Inserção de Dados](#23-inserção-de-dados)
    - [2.4 Consulta](#24-consulta)
    - [2.5 Transação](#25-transação)
    - [2.6 Store Procedure](#26-store-procedure)
    - [2.7 Triggers](#27-triggers)
    <!--toc:end-->

## 1 Atividade

A atividade consiste em introduzir para os alunos o desenvolvimento de aplicações
para bancos de dados. Nessa atividade, os alunos irão utilizar Python para desenvolver
uma aplicação cliente que consome o serviço de banco de dados (PostgreSQL) a fim
de realizar consultas, criar tabelas, inserir/deletar dados e fazer chamadas a
procedimentos armazenados.

## 2 Instruções

### 2.1 Conectando ao BD

Necessario: `psycopg3`

- _host:_ 200.129.44.249
- _database:_ O mesmo usado para o Trabalho Pr ́atico I
- _user:_ suaMatricula
- _Senha:_ suaMatricula

### 2.2 Criação de Tabelas

- `Curso (id INT PRIMARY KEY, nome VARCHAR(100), regime VARCHAR(20), duracao INT)`
- `Aluno (id INT PRIMARY KEY, nome VARCHAR(100), curso id INT REFERENCES Curso(id)
,semestre INT)`
- `Professor (id INT PRIMARY KEY, nome VARCHAR(100), area especializacao VARCHAR(100),
contato VARCHAR(100), curso id INT REFERENCES Curso(id))`
- `Disciplina (id INT PRIMARY KEY, codigo VARCHAR(10) UNIQUE, nome VARCHAR(100),
area especializacao VARCHAR(100), carga horaria INT, curso id INT REFERENCES Curso(id))`
- `Turma (id INT PRIMARY KEY, codigo VARCHAR(10) UNIQUE, disciplina id INT REFERENCES
Disciplina(id), semestre VARCHAR(20), capacidade maxima INT, estado VARCHAR(20),
prof id INT REFERENCES Professor(id))`
- `Aluno Turma (aluno id INT REFERENCES Aluno(id), turma id INT REFERENCES Turma(id)),
PRIMARY KEY (aluno id, turma id)`

### 2.3 Inserção de Dados

- Curso
- Aluno
- Professor
- Disciplina
- Turma
- ALuno_Turma

### 2.4 Consulta

- Retorne todas as turmas e a quantidade de alunos participantes de cada turma.
- Retorne os alunos matriculados na disciplina de “Fundamentos de Bancos de Dados”.
- Retorne a quantidade de professores do curso de “Ciências da Computação”.

### 2.5 Transação

Escreva um novo script em Python que realize as seguintes operações em uma ́unica
transaçao:

1. Atualize o estado da turma “CC2024DS1”para “Fechado”.
2. Remova todas as matr ́ıculas de alunos na turma “CC2024DS1”na tabela Aluno Turma.

### 2.6 Store Procedure

1. Usando PL/pgSQL, crie um procedimento armazenado no banco de dados de nome inc
   semestre que recebe como parâmetro um semestre e para todos os alunos que estão
   naquele semestre, o semestre ́e incrementado em 1;
2. Escreve um script Python que chama o procedimento armazenado criado no item
   anterior passando como parâmetro o valor 1 (i.e., quem está no primeiro semestre
   agora vai para o segundo).

### 2.7 Triggers

1. Usando PL/pgSQL, implemente um gatilho no banco de dados que dispara toda vez
   que um aluno ́e adicionado a uma turma. O gatilho deve garantir que o número de
   alunos matriculados em uma turma não exceda a capacidade m ́axima da mesma.
2. Usando PL/pgSQL, crie um segundo gatilho que restrinja um aluno a não cursar
   mais do que 4 disciplinas em um semestre. 3.
3. Escreva um script em Python que tenta inserir as tuplas na Tabela “Aluno Turma”
   como descrito na Tabela 7
4. Escreva um script em Python que tenta inserir as tuplas na Tabela “Aluno Turma”
   como descrito na Tabela 8
