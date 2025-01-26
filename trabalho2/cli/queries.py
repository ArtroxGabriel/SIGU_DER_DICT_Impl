from psycopg import Cursor
from psycopg import sql
import psycopg

USER_NAME = "postgres"
USER_PWD = "postgres"
DB_HOST = "localhost"  # "200.129.44.249"
DB_NAME = "teste_db"


def __get_classroom_and_quantity_participants(cur: Cursor) -> None:
    select_query = """
SELECT
	t.codigo,
	COUNT(*) AS quant_participantes
FROM
	turma AS t
	JOIN aluno_turma AS at ON t.id = at.turma_id
GROUP BY
	t.id
    """

    cur.execute(select_query)
    record = cur.fetchall()

    header = ["cod_turma", "num_participantes"]

    col_widths = [max(len(str(row[i])) for row in record + [header]) for i in range(2)]

    def format_row(row):
        return " | ".join(
            f"{str(cell).ljust(col_widths[i])}" for i, cell in enumerate(row)
        )

    print(format_row(header))
    print("-+-".join("-" * width for width in col_widths))
    for row in record:
        print(format_row(row))


def __get_students_from_discipline(cur: Cursor, discipline: str) -> None:
    select_query = sql.SQL("""
SELECT
	a.id,
	a.nome
FROM
	aluno a
	JOIN aluno_turma alt ON alt.aluno_id = a.id
	JOIN turma t ON t.id = alt.turma_id
	JOIN disciplina d ON d.id = t.disciplina_id
WHERE
	d.nome LIKE {}
    """).format(discipline)

    cur.execute(select_query)
    record = cur.fetchall()

    header = ["id", "nome"]

    col_widths = [max(len(str(row[i])) for row in record + [header]) for i in range(2)]

    def format_row(row):
        return " | ".join(
            f"{str(cell).ljust(col_widths[i])}" for i, cell in enumerate(row)
        )

    print(format_row(header))
    print("-+-".join("-" * width for width in col_widths))
    for row in record:
        print(format_row(row))


def __num_of_teachers_by_course(cur: Cursor, course: str) -> None:
    select_query = sql.SQL("""
SELECT
	COUNT(*)
FROM
	professor p
	JOIN curso c ON p.curso_id = c.id
WHERE
	c.nome LIKE {}
    """).format(course)

    cur.execute(select_query)
    record = cur.fetchall()

    header = ["numero_professores"]

    col_widths = [
        max(len(str(row[i])) for row in record + [header]) for i in range(len(header))
    ]

    def format_row(row):
        return " | ".join(
            f"{str(cell).ljust(col_widths[i])}" for i, cell in enumerate(row)
        )

    print(format_row(header))
    print("-+-".join("-" * width for width in col_widths))
    for row in record:
        print(format_row(row))


def run_queries(cur: Cursor) -> None:
    print("Running query to get classroom and their number of participants")
    __get_classroom_and_quantity_participants(cur)

    print("Running query to get students of Discipline 'Fundamentos de Banco de Dados'")
    __get_students_from_discipline(cur, "Fundamentos de Bancos de Dados")

    print(
        "Running query to get number of teachers of the course 'Ciências da Computação'"
    )
    __num_of_teachers_by_course(cur, "Ciências da Computação")


if __name__ == "__main__":
    with psycopg.connect(
        f"host={DB_HOST} dbname={DB_NAME} user={USER_NAME} password={USER_PWD}",
        autocommit=True,
    ) as conn:
        with conn.cursor() as cur:
            run_queries(cur)
