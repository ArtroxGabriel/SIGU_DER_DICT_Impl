from logging import Logger
from psycopg import Cursor, sql


def __insert_data(cur: Cursor, table_name: str, values_list: list) -> None:
    placeholders = sql.SQL(", ").join(sql.Placeholder() for _ in values_list[0])

    insert_query = sql.SQL("""
        INSERT INTO {table} VALUES ({placeholders})
    """).format(table=sql.Identifier(table_name), placeholders=placeholders)

    for values in values_list:
        cur.execute(insert_query, tuple(values.values()))


def insert_data(logger: Logger, cur: Cursor) -> None:
    data_table = [
        [
            "curso",
            [
                {
                    "id": 1,
                    "nome": "Ciências da Computação",
                    "regime": "Semestral",
                    "duracao": 8,
                },
                {
                    "id": 2,
                    "nome": "Engenharia de Software",
                    "regime": "Anual",
                    "duracao": 10,
                },
                {
                    "id": 3,
                    "nome": "Sistemas de Informação",
                    "regime": "Semestral",
                    "duracao": 8,
                },
            ],
        ],
        [
            "aluno",
            [
                {
                    "id": 1,
                    "nome": "João Silva",
                    "curso_id": 1,
                    "semestrel": 1,
                },
                {
                    "id": 2,
                    "nome": "Maria Costa",
                    "curso_id": 1,
                    "semestrel": 1,
                },
                {
                    "id": 3,
                    "nome": "Ana Souza",
                    "curso_id": 3,
                    "semestrel": 5,
                },
                {
                    "id": 4,
                    "nome": "Pedro Almeida",
                    "curso_id": 2,
                    "semestrel": 3,
                },
                {
                    "id": 5,
                    "nome": "Lucas Santos",
                    "curso_id": 2,
                    "semestrel": 3,
                },
            ],
        ],
        [
            "professor",
            [
                {
                    "id": 1,
                    "nome": "Maria Oliveira",
                    "area especializacao": "Banco de Dados",
                    "contato": "maria@ufc.br",
                    "curso_id": 1,
                },
                {
                    "id": 2,
                    "nome": "João Pereira",
                    "area especializacao": "Redes de Computadores",
                    "contato": "joao@ufc.br",
                    "curso_id": 2,
                },
                {
                    "id": 3,
                    "nome": "Ana Silva",
                    "area especializacao": "Inteligência Artificial",
                    "contato": "ana@ufc.br",
                    "curso_id": 3,
                },
                {
                    "id": 4,
                    "nome": "Paulo Santos",
                    "area especializacao": "Engenharia de Software",
                    "contato": "paulo@ufc.br",
                    "curso_id": 2,
                },
                {
                    "id": 5,
                    "nome": "Carla Mendes",
                    "area especializacao": "Redes de Computadores",
                    "contato": "carla@ufc.br",
                    "curso_id": 1,
                },
            ],
        ],
        [
            "disciplina",
            [
                {
                    "id": 1,
                    "codigo": "BD001",
                    "nome": "Fundamentos de Bancos de Dados",
                    "area especializacao": "Banco de Dados",
                    "carga_horaria": 60,
                    "curso_id": 1,
                },
                {
                    "id": 2,
                    "codigo": "IA002",
                    "nome": "Inteligência Computacional Aplicada",
                    "area especializacao": "Inteligência Artificial",
                    "carga_horaria": 80,
                    "curso_id": 3,
                },
                {
                    "id": 3,
                    "codigo": "RS003",
                    "nome": "Segurança da Informação",
                    "area especializacao": "Redes de Computadores",
                    "carga_horaria": 40,
                    "curso_id": 2,
                },
                {
                    "id": 4,
                    "codigo": "BD004",
                    "nome": "Introdução a Ciência de Dados",
                    "area especializacao": "Banco de Dados",
                    "carga_horaria": 60,
                    "curso_id": 1,
                },
                {
                    "id": 5,
                    "codigo": "ES005",
                    "nome": "Qualidade de Software",
                    "area especializacao": "Engenharia de Software",
                    "carga_horaria": 50,
                    "curso_id": 2,
                },
            ],
        ],
        [
            "turma",
            [
                {
                    "id": 1,
                    "codigo": "CC2024BD1",
                    "disciplina_id": 1,
                    "semestre": "2024.2",
                    "capacidade_maxima": 4,
                    "estado": "Aberta",
                    "prof_id": 1,
                },
                {
                    "id": 2,
                    "codigo": "CC2024IA1",
                    "disciplina_id": 2,
                    "semestre": "2024.2",
                    "capacidade_maxima": 4,
                    "estado": "Aberta",
                    "prof_id": 3,
                },
                {
                    "id": 3,
                    "codigo": "CC2024RS1",
                    "disciplina_id": 3,
                    "semestre": "2024.1",
                    "capacidade_maxima": 8,
                    "estado": "Aberta",
                    "prof_id": 2,
                },
                {
                    "id": 4,
                    "codigo": "CC2024DS1",
                    "disciplina_id": 4,
                    "semestre": "2024.2",
                    "capacidade_maxima": 4,
                    "estado": "Aberta",
                    "prof_id": 1,
                },
                {
                    "id": 5,
                    "codigo": "CC2024ES1",
                    "disciplina_id": 5,
                    "semestre": "2024.2",
                    "capacidade_maxima": 8,
                    "estado": "Aberta",
                    "prof_id": 4,
                },
            ],
        ],
        [
            "aluno_turma",
            [
                {
                    "aluno_id": 1,
                    "turma_id": 1,
                },
                {
                    "aluno_id": 2,
                    "turma_id": 1,
                },
                {
                    "aluno_id": 3,
                    "turma_id": 2,
                },
                {
                    "aluno_id": 4,
                    "turma_id": 3,
                },
                {
                    "aluno_id": 5,
                    "turma_id": 4,
                },
                {
                    "aluno_id": 1,
                    "turma_id": 5,
                },
                {
                    "aluno_id": 2,
                    "turma_id": 4,
                },
                {
                    "aluno_id": 3,
                    "turma_id": 5,
                },
                {
                    "aluno_id": 4,
                    "turma_id": 2,
                },
                {
                    "aluno_id": 5,
                    "turma_id": 3,
                },
            ],
        ],
    ]
    logger.info("Starting data insertion")
    for data in data_table:
        logger.info(
            "Inserting {} record(s) into the '{}' table".format(len(data[1]), data[0])
        )
        __insert_data(cur, data[0], data[1])
