INSERT INTO
	CURSO (ID, NOME, REGIME, DURACAO)
VALUES
	(1, 'Engenharia de Software', 'semestre', 8),
	(2, 'Ciência da Computação', 'semestre', 8),
	(3, 'Física', 'semestre', 8),
	(4, 'Engenharia Civil', 'anual', 10),
	(5, 'Matemática', 'semestre', 6);

INSERT INTO
	PROFESSOR (ID, NOME, AREA_PROFESSOR, ID_CURSO, CONTATO)
VALUES
	(
		1,
		'Prof. João Silva',
		'Algoritmos',
		1,
		'joao.silva@email.com'
	),
	(
		2,
		'Prof. Maria Oliveira',
		'Álgebra',
		2,
		'maria.oliveira@email.com'
	),
	(
		3,
		'Prof. Pedro Costa',
		'Física Experimental',
		3,
		'pedro.costa@email.com'
	),
	(
		4,
		'Prof. Ana Souza',
		'Estruturas de Concreto',
		4,
		'ana.souza@email.com'
	),
	(
		5,
		'Prof. Carlos Pinto',
		'Cálculo Diferencial',
		5,
		'carlos.pinto@email.com'
	);

INSERT INTO
	DISCIPLINA (
		NUMERO_DISCIPLINA,
		AREA_DISCIPLINA,
		NOME,
		CARGA_HORARIA,
		EMENTA
	)
VALUES
	(
		1,
		'Algoritmos',
		'Algoritmos e Estruturas de Dados',
		60,
		'Estudo de algoritmos clássicos, ordenação e estruturas de dados.'
	),
	(
		2,
		'Matemática',
		'Cálculo I',
		60,
		'Funções, limites, derivadas e integrais.'
	),
	(
		3,
		'Física',
		'Mecânica Clássica',
		80,
		'Leis de Newton, energia e trabalho, dinâmica.'
	),
	(
		4,
		'Engenharia Civil',
		'Estruturas de Concreto',
		60,
		'Análise e projeto de estruturas de concreto armado.'
	),
	(
		5,
		'Física',
		'Física Moderna',
		60,
		'Teorias relativísticas e mecânica quântica.'
	);

INSERT INTO
	TURMA (
		ID_DISCIPLINA,
		ID_CURSO,
		NOME_CURSO,
		NUMERO_DISCIPLINA,
		NOME,
		SEMESTRE,
		CAP_MAXIMA,
		ESTADO
	)
VALUES
	(
		'Al1',
		1,
		'Engenharia de Software',
		1,
		'Algoritmos 2025/1',
		1,
		30,
		'ativo'
	),
	(
		'Ma2',
		2,
		'Ciência da Computação',
		2,
		'Cálculo I 2025/1',
		1,
		25,
		'ativo'
	),
	(
		'Fí3',
		3,
		'Física',
		3,
		'Mecânica Clássica 2025/1',
		1,
		40,
		'ativo'
	),
	(
		'En4',
		4,
		'Engenharia Civil',
		4,
		'Estruturas de Concreto 2025/1',
		1,
		35,
		'ativo'
	),
	(
		'Fí5',
		5,
		'Física',
		5,
		'Física Moderna 2025/1',
		1,
		30,
		'ativo'
	);

INSERT INTO
	ALUNO (
		ID,
		MATRICULA,
		NOME,
		ID_CURSO,
		NASCIMENTO,
		ENTRADA,
		CONCLUSAO
	)
VALUES
	(
		1,
		'123456',
		'Lucas Pereira',
		1,
		'2001-03-15',
		2019,
		2023
	),
	(
		2,
		'234567',
		'Julia Fernandes',
		2,
		'2000-07-22',
		2018,
		2022
	),
	(
		3,
		'345678',
		'Pedro Costa',
		3,
		'1999-10-11',
		2017,
		2021
	),
	(
		4,
		'456789',
		'Ana Souza',
		4,
		'2001-01-28',
		2020,
		2024
	),
	(
		5,
		'567890',
		'Carlos Silva',
		5,
		'2000-05-05',
		2019,
		2023
	);

INSERT INTO
	AVALIACAO (ID, TIPO, DATA_APLICACAO, PESO)
VALUES
	(1, 'prova', '2025-06-15 09:00:00', 50),
	(2, 'trabalho', '2025-06-20 14:00:00', 30),
	(3, 'prova', '2025-06-22 09:00:00', 60),
	(4, 'trabalho', '2025-06-25 14:00:00', 40),
	(5, 'prova', '2025-06-30 09:00:00', 70);

INSERT INTO
	NOTA (ID, ID_AVALIACAO, VALOR, ID_ALUNO)
VALUES
	(1, 1, 8.5, 1),
	(2, 2, 7.0, 2),
	(3, 3, 9.0, 3),
	(4, 4, 6.5, 4),
	(5, 5, 10.0, 5);

INSERT INTO
	SALA_DE_AULA (
		ID,
		TIPO_ESTRUTURA,
		TIPO_LOUSA,
		CAPACIDADE,
		LOCALIZACAO
	)
VALUES
	(
		1,
		'anfiteatro',
		'branca',
		100,
		'Bloco A - Sala 101'
	),
	(
		2,
		'laboratorio',
		'preta',
		30,
		'Bloco B - Sala 201'
	),
	(
		3,
		'sala_comum',
		'digital',
		50,
		'Bloco C - Sala 303'
	),
	(
		4,
		'anfiteatro',
		'branca',
		150,
		'Bloco A - Sala 102'
	),
	(
		5,
		'laboratorio',
		'preta',
		40,
		'Bloco D - Sala 404'
	);

INSERT INTO
	MATERIAL_DIDATICO (ID, TITULO, DESCRICAO, FORMATO)
VALUES
	(
		1,
		'Livro de Algoritmos',
		'Texto básico sobre estruturas de dados',
		'pdf'
	),
	(
		2,
		'Vídeo de Física',
		'Aulas gravadas sobre mecânica clássica',
		'video'
	),
	(
		3,
		'Áudio de Matemática',
		'Explicações em áudio sobre cálculo diferencial',
		'audio'
	),
	(
		4,
		'Livro de Estruturas de Concreto',
		'Material teórico sobre concreto armado',
		'livro'
	),
	(
		5,
		'Vídeo de Cálculo',
		'Aulas sobre integrais e derivadas',
		'video'
	);

INSERT INTO
	PROJETO_PESQUISA (
		ID,
		TITULO,
		ID_COORDENADOR,
		AREA,
		DESCRICAO,
		ORC_PLANEJADO,
		ORC_REALIZADO,
		ORC_DISPONIVEL,
		ESTADO
	)
VALUES
	(
		1,
		'Desenvolvimento de Algoritmos para IA',
		1,
		'Inteligência Artificial',
		'Desenvolvimento de novos algoritmos para otimização de IA.',
		50000,
		20000,
		30000,
		'planejado'
	),
	(
		2,
		'Estudo da Física Quântica',
		2,
		'Física Quântica',
		'Pesquisa em fenômenos de mecânica quântica aplicada.',
		60000,
		25000,
		35000,
		'em_andamento'
	),
	(
		3,
		'Inovação em Energias Renováveis',
		3,
		'Engenharia Ambiental',
		'Estudo de fontes renováveis de energia e seus impactos ambientais.',
		70000,
		30000,
		40000,
		'em_andamento'
	),
	(
		4,
		'Cálculo de Estruturas de Concreto',
		4,
		'Engenharia Civil',
		'Pesquisa sobre novos métodos de cálculo para estruturas de concreto.',
		45000,
		10000,
		35000,
		'planejado'
	),
	(
		5,
		'Aplicações de Big Data em Medicina',
		5,
		'Ciência de Dados',
		'Exploração de Big Data para diagnósticos médicos mais precisos.',
		80000,
		50000,
		30000,
		'finalizado'
	);

INSERT INTO
	PROFESSOR_CURSO_COORDENA (ID_CURSO, ID_PROFESSOR)
VALUES
	(1, 1),
	(2, 2),
	(3, 3),
	(4, 4),
	(5, 5);

INSERT INTO
	PROFESSOR_TURMA (ID_PROFESSOR, ID_TURMA)
VALUES
	(1, 'Ci2'),
	(2, 'En1'),
	(3, 'En4'),
	(4, 'Fí3'),
	(5, 'Fí5');

INSERT INTO
	PROFESSOR_CURSO_PERTENCE (ID_PROFESSOR, ID_CURSO)
VALUES
	(1, 1),
	(2, 2),
	(3, 3),
	(4, 4),
	(5, 5);

INSERT INTO
	DISCIPLINA_MATERIAL (ID_DISCIPLINA, ID_MATERIAL, OPCIONAL)
VALUES
	('Al1', 1, TRUE),
	('Ma2', 2, FALSE),
	('Fí3', 3, TRUE),
	('En4', 4, FALSE),
	('Fí5', 5, TRUE);

INSERT INTO
	ALUNO_TURMA (ID_ALUNO, ID_TURMA)
VALUES
	(1, 'Ci2'),
	(2, 'En1'),
	(3, 'En4'),
	(4, 'Fí3'),
	(5, 'Fí5');

INSERT INTO
	SALA_TURMA (ID_TURMA, ID_SALA)
VALUES
	('Ci2', 2),
	('En1', 1),
	('En4', 4),
	('Fí3', 3),
	('Fí5', 5);

INSERT INTO
	AVALIACAO_TURMA (ID_AVALIACAO, ID_TURMA)
VALUES
	(1, 'Ci2'),
	(2, 'En1'),
	(3, 'En4'),
	(4, 'Fí3'),
	(5, 'Fí5');

INSERT INTO
	AVALIACAO_NOTA (ID_AVALIACAO, ID_NOTA)
VALUES
	(1, 1),
	(2, 2),
	(3, 3),
	(4, 4),
	(5, 5);

INSERT INTO
	MATERIAL_PROFESSOR (ID_MATERIAL, ID_PROFESSOR)
VALUES
	(1, 1),
	(2, 2),
	(3, 3),
	(4, 4),
	(5, 5);

INSERT INTO
	MATERIAL_TURMA (ID_MATERIAL, ID_TURMA)
VALUES
	(1, 'Ci2'),
	(2, 'En1'),
	(3, 'En4'),
	(4, 'Fí3'),
	(5, 'Fí5');

INSERT INTO
	PROFESSOR_PROJETO (ID_PROFESSOR, ID_PROJETO, FUNCAO)
VALUES
	(1, 1, 'Coordenador'),
	(2, 2, 'Pesquisador'),
	(3, 3, 'Tesoureiro'),
	(4, 4, 'Gerente'),
	(5, 5, 'Pesquisador2');

INSERT INTO
	ALUNO_PROJETO (ID_ALUNO, ID_PROJETO, FUNCAO)
VALUES
	(1, 1, 'Pesquisador Banco de Dados'),
	(2, 2, 'Pesquisador Teoria dos Grafos'),
	(3, 3, 'Pesquisador Algoritmos Probabilísticos'),
	(4, 4, 'Pesquisador Otimização'),
	(5, 5, 'Pesquisador IA');