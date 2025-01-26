from logging import Logger
from psycopg import Cursor, sql


def __create_tables(cur: Cursor, table_name: str, attributes) -> None:
    create_table_query = sql.SQL("""
        CREATE TABLE IF NOT EXISTS {table} (
            {columns}
        )
    """).format(table=sql.Identifier(table_name), columns=sql.SQL(attributes))

    cur.execute(create_table_query)


def create_tables(logger: Logger, cur: Cursor) -> None:
    logger.info("Starting to delete tables if they exist")
    drop_tables_query = sql.SQL("""
        DROP TABLE IF EXISTS Aluno_Turma CASCADE;
        DROP TABLE IF EXISTS Turma CASCADE;
        DROP TABLE IF EXISTS Disciplina CASCADE;
        DROP TABLE IF EXISTS Professor CASCADE;
        DROP TABLE IF EXISTS Aluno CASCADE;
        DROP TABLE IF EXISTS Curso CASCADE;
    """)
    cur.execute(drop_tables_query)

    tables = [
        (
            "curso",
            """
            id INT PRIMARY KEY,
            nome VARCHAR(100) NOT NULL CHECK (nome <> ''),
            regime VARCHAR(20) NOT NULL CHECK (regime <> ''),
            duracao INT NOT NULL CHECK (duracao > 0)
            """,
        ),
        (
            "aluno",
            """
            id INT PRIMARY KEY,
            nome VARCHAR(100) NOT NULL CHECK (nome <> ''),
            curso_id INT NOT NULL REFERENCES curso (id),
            semestre INT NOT NULL CHECK (semestre > 0)
            """,
        ),
        (
            "professor",
            """
            id INT PRIMARY KEY,
            nome VARCHAR(100) NOT NULL CHECK (nome <> ''),
            area_especializacao VARCHAR(100) NOT NULL CHECK (area_especializacao <> ''),
            contato VARCHAR(100) NOT NULL CHECK (contato <> ''),
            curso_id INT NOT NULL REFERENCES curso (id)
            """,
        ),
        (
            "disciplina",
            """
            id INT PRIMARY KEY,
            codigo VARCHAR(10) UNIQUE NOT NULL CHECK (codigo <> ''),
            nome VARCHAR(100) NOT NULL CHECK (nome <> ''),
            area_especializacao VARCHAR(100) NOT NULL CHECK (area_especializacao <> ''),
            carga_horaria INT NOT NULL CHECK (carga_horaria > 0),
            curso_id INT NOT NULL REFERENCES curso (id)
            """,
        ),
        (
            "turma",
            """
            id INT PRIMARY KEY,
            codigo VARCHAR(10) UNIQUE NOT NULL CHECK (codigo <> ''),
            disciplina_id INT NOT NULL REFERENCES disciplina (id),
            semestre VARCHAR(20) NOT NULL CHECK (semestre <> ''),
            capacidade_maxima INT NOT NULL CHECK (capacidade_maxima > 0),
            estado VARCHAR(20) NOT NULL CHECK (estado <> ''),
            prof_id INT REFERENCES professor (id)
            """,
        ),
        (
            "aluno_turma",
            """
            aluno_id INT NOT NULL REFERENCES aluno (id),
            turma_id INT NOT NULL REFERENCES turma (id),
            PRIMARY KEY (aluno_id, turma_id)
            """,
        ),
    ]

    logger.info("Starting creation of {} tables".format(len(tables)))
    for table_name, attributes in tables:
        logger.info("Creating the '{}' table".format(table_name))
        __create_tables(cur, table_name, attributes)

    # Commitando uma única transação
    logger.info("Tables Created succesfully")
