CREATE TABLE curso (
    id bigint PRIMARY KEY,
    nome varchar(30) UNIQUE NOT NULL, 
    id_coordenador BIGINT NOT NULL,
    regime varchar(9) NOT NULL, 
    duracao integer NOT NULL
); 

CREATE TABLE professor (
	id bigint PRIMARY KEY, 
	nome varchar(60) NOT NULL, 
	area_professor varchar(60) NOT NULL, 
	id_curso bigint, 
	contato varchar(60), 
	FOREIGN KEY (id_curso) REFERENCES curso(id)
); 

ALTER TABLE curso 
ADD CONSTRAINT fk_id_coordenador FOREIGN KEY (id_coordenador) REFERENCES professor(id); 

CREATE TABLE turma (
	id bigint PRIMARY KEY, 
	nome varchar(60) NOT NULL, 
	id_curso bigint NOT NULL, 
	semestre integer NOT NULL,
	cap_maxima integer NOT NULL, 
	estado varchar(15) NOT NULL, 
	FOREIGN KEY (id_curso) REFERENCES curso(id)
);

CREATE TABLE aluno (
	id bigint PRIMARY KEY, 
	matricula bigint UNIQUE NOT NULL,
	nome varchar(60) NOT NULL, 
	id_curso bigint NOT NULL,
	idade integer NOT NULL, 
	nascimento date NOT NULL, 
	entrada integer NOT NULL, 
	conclusao integer NOT NULL, 
	CHECK (entrada <= conclusao),
	FOREIGN KEY (id_curso) REFERENCES curso(id)
); 

CREATE TABLE avaliacao (
	id bigint PRIMARY KEY, 
	tipo varchar(20) NOT NULL, 
	data_aplicacao timestamp NOT NULL, 
	peso integer NOT NULL
); 

CREATE TABLE nota (
	id bigint PRIMARY KEY, 
	id_avaliacao bigint NOT NULL, 
	valor real NOT NULL CHECK (valor >= 0 AND valor <= 10), 
	id_aluno bigint NOT NULL, 
	FOREIGN KEY(id_avaliacao) REFERENCES avaliacao(id), 
	FOREIGN KEY(id_aluno) REFERENCES aluno(id) 
); 

CREATE TABLE sala_de_aula (
	id bigint PRIMARY KEY, 
	tipo_estrutura smallint NOT NULL, 
	tipo_lousa smallint NOT NULL, 
	capacidade integer NOT NULL, 
	localizacao varchar(255) NOT NULL 
); 

CREATE TABLE material_didatico (
	id bigint PRIMARY KEY, 
	titulo varchar(40) NOT NULL, 
	descricao varchar(255) NOT NULL, 
	formato smallint NOT NULL
); 

CREATE TABLE projeto_pesquisa (
	id bigint PRIMARY KEY, 
	titulo varchar(40) NOT NULL,
	id_coordenador bigint NOT NULL, 
	area varchar(60) NOT NULL, 
	descricao varchar(255) NOT NULL, 
	orc_planejado real NOT NULL, 
	orc_realizado real, 
	estado smallint NOT NULL, 
	FOREIGN KEY (id_coordenador) REFERENCES professor(id) 
); 

-- Relations 


