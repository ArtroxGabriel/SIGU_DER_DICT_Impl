CREATE TABLE curso
  (
     id             BIGINT PRIMARY KEY,
     nome           VARCHAR(30) UNIQUE NOT NULL,
     id_coordenador BIGINT NOT NULL,
     regime         VARCHAR(9) NOT NULL,
     duracao        INTEGER NOT NULL
  );

CREATE TABLE professor
  (
     id             BIGINT PRIMARY KEY,
     nome           VARCHAR(60) NOT NULL,
     area_professor VARCHAR(60) NOT NULL,
     id_curso       BIGINT,
     contato        VARCHAR(60),
     FOREIGN KEY (id_curso) REFERENCES curso (id)
  );

ALTER TABLE curso
  ADD CONSTRAINT fk_id_coordenador FOREIGN KEY (id_coordenador) REFERENCES
  professor (id);

CREATE TABLE turma
  (
     id         BIGINT PRIMARY KEY,
     nome       VARCHAR(60) NOT NULL,
     id_curso   BIGINT NOT NULL,
     semestre   INTEGER NOT NULL,
     cap_maxima INTEGER NOT NULL,
     estado     VARCHAR(15) NOT NULL,
     FOREIGN KEY (id_curso) REFERENCES curso (id)
  );

CREATE TABLE aluno
  (
     id         BIGINT PRIMARY KEY,
     matricula  BIGINT UNIQUE NOT NULL,
     nome       VARCHAR(60) NOT NULL,
     id_curso   BIGINT NOT NULL,
     idade      INTEGER NOT NULL,
     nascimento DATE NOT NULL,
     entrada    INTEGER NOT NULL,
     conclusao  INTEGER NOT NULL,
     CHECK (entrada <= conclusao),
     FOREIGN KEY (id_curso) REFERENCES curso (id)
  );

CREATE TABLE avaliacao
  (
     id             BIGINT PRIMARY KEY,
     tipo           VARCHAR(20) NOT NULL,
     data_aplicacao TIMESTAMP NOT NULL,
     peso           INTEGER NOT NULL
  );

CREATE TABLE nota
  (
     id           BIGINT PRIMARY KEY,
     id_avaliacao BIGINT NOT NULL,
     valor        REAL NOT NULL CHECK ( valor >= 0 AND valor <= 10 ),
     id_aluno     BIGINT NOT NULL,
     FOREIGN KEY (id_avaliacao) REFERENCES avaliacao (id),
     FOREIGN KEY (id_aluno) REFERENCES aluno (id)
  );

CREATE TABLE sala_de_aula
  (
     id             BIGINT PRIMARY KEY,
     tipo_estrutura SMALLINT NOT NULL,
     tipo_lousa     SMALLINT NOT NULL,
     capacidade     INTEGER NOT NULL,
     localizacao    VARCHAR(255) NOT NULL
  );

CREATE TABLE material_didatico
  (
     id        BIGINT PRIMARY KEY,
     titulo    VARCHAR(40) NOT NULL,
     descricao VARCHAR(255) NOT NULL,
     formato   SMALLINT NOT NULL
  );

CREATE TABLE projeto_pesquisa
  (
     id             BIGINT PRIMARY KEY,
     titulo         VARCHAR(40) NOT NULL,
     id_coordenador BIGINT NOT NULL,
     area           VARCHAR(60) NOT NULL,
     descricao      VARCHAR(255) NOT NULL,
     orc_planejado  REAL NOT NULL,
     orc_realizado  REAL,
     estado         SMALLINT NOT NULL,
     FOREIGN KEY (id_coordenador) REFERENCES professor (id)
  );
-- Relations
