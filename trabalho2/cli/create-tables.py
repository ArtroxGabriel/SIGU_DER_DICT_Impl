import psycopg

USER_NAME = "postgres"
USER_PWD = "postgres"
DB_HOST = "localhost"  # "200.129.44.249"
DB_NAME = "teste_db"

CREATE_QUERY = """
CREATE TABLE IF NOT EXISTS Curso (
	id INTEGER PRIMARY KEY,
	nome VARCHAR(100) NOT NULL CHECK (nome <> ''),
	regime VARCHAR(20) NOT NULL CHECK (regime <> ''),
	duracao INT NOT NULL CHECK (duracao > 0)
);

CREATE TABLE IF NOT EXISTS Aluno (
	id INT PRIMARY KEY,
	nome VARCHAR(100) NOT NULL CHECK (nome <> ''),
	curso_id INT NOT NULL REFERENCES Curso (id),
	semestre INT NOT NULL CHECK (semestre > 0)
);

CREATE TABLE IF NOT EXISTS Professor (
	id INT PRIMARY KEY,
	nome VARCHAR(100) NOT NULL CHECK (nome <> ''),
	area_especializacao VARCHAR(100) NOT NULL CHECK (area_especializacao <> ''),
	contato VARCHAR(100) NOT NULL CHECK (contato <> ''),
	curso_id INT NOT NULL REFERENCES Curso (id)
);

CREATE TABLE IF NOT EXISTS Disciplina (
	id INT PRIMARY KEY,
	codigo VARCHAR(10) UNIQUE NOT NULL CHECK (codigo <> ''),
	nome VARCHAR(100) NOT NULL CHECK (nome <> ''),
	area_especializacao VARCHAR(100) NOT NULL CHECK (area_especializacao <> ''),
	carga_horaria INT NOT NULL CHECK (carga_horaria > 0),
	curso_id INT NOT NULL REFERENCES Curso (id)
);

CREATE TABLE IF NOT EXISTS Turma (
	id INT PRIMARY KEY,
	codigo VARCHAR(10) UNIQUE NOT NULL CHECK (codigo <> ''),
	disciplina_id INT NOT NULL REFERENCES Disciplina (id),
	semestre INT NOT NULL CHECK (semestre > 0),
	capacidade_maxima INT NOT NULL CHECK (capacidade_maxima > 0),
	estado VARCHAR(20) NOT NULL CHECK (estado <> ''),
	prof_id INT REFERENCES Professor (id)
);

CREATE TABLE IF NOT EXISTS Aluno_Turma (
	aluno_id INT NOT NULL REFERENCES Aluno (id),
	turma_id INT NOT NULL REFERENCES Turma (id),
	PRIMARY KEY (aluno_id, turma_id)
);
"""


def create_tables() -> None:
    with psycopg.connect(
        f"postgres://{USER_NAME}:{USER_PWD}@{DB_HOST}/{DB_NAME}"
    ) as conn:
        # Open a cursor to perform database operations
        with conn.cursor() as cur:
            cur.execute(CREATE_QUERY)

            conn.commit()


if __name__ == "__main__":
    create_tables()
