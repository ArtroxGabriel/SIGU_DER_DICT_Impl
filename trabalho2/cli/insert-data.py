import psycopg

USER_NAME = "postgres"
USER_PWD = "postgres"
DB_HOST = "localhost"  # "200.129.44.249"
DB_NAME = "teste_db"


def insert_data(table, data) -> None:
    with psycopg.connect(
        f"postgres://{USER_NAME}:{USER_PWD}@{DB_HOST}/{DB_NAME}"
    ) as conn:
        # Open a cursor to perform database operations
        with conn.cursor() as cur:
            print(f"Inserting data in table {table}")
            cur.execute(data)

            conn.commit()


if __name__ == "__main__":
    datas = [
        [
            "Curso",
            """
INSERT INTO
	Curso
VALUES
	(1, 'Ciências da Computação', 'Semestral', 8),
	(2, 'Engenharia de Software', 'Anual', 10),
	(3, 'Sistemas de Informação', 'Semestral', 8)
    """,
        ],
        [
            "Aluno",
            """
INSERT INTO
	Aluno
VALUES
	(1, 'João Silva', 1, 1),
	(2, 'Maria Costa', 1, 1),
	(3, 'Ana Souza', 3, 5),
	(4, 'Pedro Almeida', 2, 3),
	(5, 'Lucas Santos', 2, 3)
    """,
        ],
        [
            "Professor",
            """
INSERT INTO
	professor
VALUES
	(1, 'Maria Oliveira', 'Banco de Dados', 'maria@ufc.br', 1),
	(2, 'João Pereira', 'Redes de Computadores', 'joao@ufc.br', 2),
	(3, 'Ana Silva', 'Inteligência Artificial', 'ana@ufc.br', 3),
	(4, 'Paulo Santos', 'Engenharia de Software', 'paulo@ufc.br', 2),
	(5, 'Carla Mendes', 'Redes de Computadores', 'carla@ufc.br', 1)
    """,
        ],
        [
            "Disciplina",
            """
INSERT INTO
	disciplina
VALUES
	(1, 'BD001', 'Fundamentos de Bancos de Dados', 'Banco de Dados', 60, 1),
	(2, 'IA002', 'Inteligência Computacional Aplicada', 'Inteligência Artificial', 80, 3),
	(3, 'RS003', 'Seguran ̧ca da Informação', 'Redes de Computadores', 40, 2),
	(4, 'BD004', 'Introdução a Ciência de Dados', 'Banco de Dados', 60, 1),
	(5, 'ES005', 'Qualidade de Software', 'Engenharia de Software', 50, 2)
    """,
        ],
        [
            "Turma",
            """
INSERT INTO
	Turma
VALUES
	(1, 'CC2024BD1', 1, '2024.2', 4, 'Aberta', 1),
	(2, 'CC2024IA1', 2, '2024.2', 4, 'Aberta', 3),
	(3, 'CC2024RS1', 3, '2024.1', 8, 'Aberta', 2),
	(4, 'CC2024DS1', 4, '2024.2', 4, 'Aberta', 1),
	(5, 'CC2024ES1', 5, '2024.2', 8, 'Aberta', 4)
            """,
        ],
        [
            "Aluno_Turma",
            """
INSERT INTO
	aluno_turma
VALUES
	(1, 1),
	(2, 1),
	(3, 2),
	(4, 3),
	(5, 4),
	(1, 5),
	(2, 4),
	(3, 5),
	(4, 2),
	(5, 3)
            """,
        ],
    ]
    for data in datas:
        insert_data(data[0], data[1])
