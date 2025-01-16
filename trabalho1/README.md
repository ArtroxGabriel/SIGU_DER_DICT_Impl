# Trabalho Pratico I

<!--toc:start-->

- [Trabalho Pratico I](#trabalho-pratico-i)
  - [Especificação de Requisitos](#especificação-de-requisitos)
  - [Entregaveis](#entregaveis)
  <!--toc:end-->

## Especificação de Requisitos

Imagine que você foi escolhido para projetar um banco de dados para um sistema
de gestão universitária (SIGU) com disciplinas, turmas e aulas. Após fazer um
levantamento, consultando diferentes

especialistas da área, você identificou os seguintes requisitos:

1. Cada **Curso**:
   1. Possui um código identificador, nome, coordenador e regime (semestral ou
      anual) e duração total.
2. Cada **Professor**:
   1. Possui um código identificador, nome, área de especialização, curso e contato.
   2. Pertence a um curso, participa de projetos de pesquisa e é responsável por
      turmas.
3. Cada **Disciplina**:
   1. Possui um código identificador composto pelo dois caracteres iniciais da
      área de especialização e um número, nome, área de especialização, carga
      horária e ementa.
   2. Possui materiais didáticos obrigatórios e opcionais e é associada a turmas.
4. Cada **Turma**:
   1. possui um código identificador composto pelos dois caracteres inicias do
      curso para o qual é ofertado e o número da disciplina, nome, curso, semestre,
      capacidade máxima e estado (aberta, fechada, em andamento, concluída).
   2. é ministrada por professores e composta por alunos.
   3. possui uma e somente uma sala de aula.
5. Cada **Aluno**:
   1. possui um código identificador, matrícula, nome, curso, idade, ano de entrada
      e o ano provável de conclusão.
   2. participa de turmas.
6. Cada **Avaliação**:
   1. possui um código identificador, tipo (Prova ou Trabalho), data da aplicação
      e o peso na nota.
   2. é aplicada a turmas e possuem notas ponderadas.
7. Cada **Nota**:
   1. possui um código identificador, avaliação associada, valor numérico da
      avaliação e o aluno relacionado.
8. Cada **Sala de Aula**:
   1. possui um código identificador, tipo de estrutura (normal ou auditório),
      tipo de lousa (giz, branca ou vidro), capacidade e localização.
9. Cada **Material Didático**:
   1. possui um código identificador, título, descrição, formato (PDF, vídeo,
      áudio, material, externo e outros).
   2. é associado a professores e turmas.
10. Cada Projeto de Pesquisa:
    1. possui um código identificador, título, professor-coordenador, área de
       especialização, descrição, orçamento-planejado, orçamento-disponível,
       orçamento-realizado, estado (planejado, em andamento e finalizado).
    2. possui vários professores e vários alunos envolvidos sendo que cada um
       possui uma função diferente.

## Entregaveis

- [ ] Diagrama de Entidade-Relacionamento
      [link](https://drive.google.com/file/d/1d5QVytJ5FTKQcfxB-y4UmwTDte_qbcFN/view?usp=sharing)
- [ ] Dicionário de Dados
      [link](https://docs.google.com/document/d/1Nac5SGUzuzNW0clQiOZ88Pjdayu9FqIlY678wP7v-E8/edit?usp=sharing)
- [ ] Implementação do Banco de Dados
      [Query de Criaçao](./src/create)
- [ ] Inserção de dados
      [Query de Inserção](./src/insertions)
- [ ] Documento de descrição do trabalho
