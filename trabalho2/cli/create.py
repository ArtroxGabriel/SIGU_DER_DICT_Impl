from psycopg import Cursor, sql
import psycopg


USER_NAME = "postgres"
USER_PWD = "postgres"
DB_HOST = "localhost"  # "200.129.44.249"
DB_NAME = "teste_db"


def __create_tables(cur: Cursor, table_name: str, attributes) -> None:
    create_table_query = sql.SQL("""
        CREATE TABLE IF NOT EXISTS {table} (
            {columns}
        )
    """).format(table=sql.Identifier(table_name), columns=sql.SQL(attributes))

    try:
        cur.execute(create_table_query)
    except Exception as e:
        print(f"An error occurred: {e}")


def create_tables(cur: Cursor) -> None:
    print("Dropping tables if exists")
    drop_tables_query = sql.SQL("""
        DROP TABLE IF EXISTS aluno_turma CASCADE;
        DROP TABLE IF EXISTS turma CASCADE;
        DROP TABLE IF EXISTS disciplina CASCADE;
        DROP TABLE IF EXISTS professor CASCADE;
        DROP TABLE IF EXISTS aluno CASCADE;
        DROP TABLE IF EXISTS curso CASCADE;
    """)
    try:
        cur.execute(drop_tables_query)
    except Exception as e:
        print(f"An error occurred: {e}")

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

    print("Starting create tables")
    for table_name, attributes in tables:
        __create_tables(cur, table_name, attributes)
    print("Tables Created Successfully!")


if __name__ == "__main__":
    with psycopg.connect(
        f"host={DB_HOST} dbname={DB_NAME} user={USER_NAME} password={USER_PWD}",
        autocommit=True,
    ) as conn:
        with conn.cursor() as cur:
            create_tables(cur)
