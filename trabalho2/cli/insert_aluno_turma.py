from psycopg import Cursor, sql
import psycopg

USER_NAME = "539628"
USER_PWD = "539628"
DB_HOST = "200.129.44.249"
DB_NAME = "antgabriel_539628_ed1"


def __insert_data(cur: Cursor, table_name: str, values_list: list) -> None:
    placeholders = sql.SQL(", ").join(sql.Placeholder() for _ in values_list[0])

    insert_query = sql.SQL("""
        INSERT INTO {table} VALUES ({placeholders})
    """).format(table=sql.Identifier(table_name), placeholders=placeholders)

    for values in values_list:
        cur.execute(insert_query, tuple(values.values()))


def populate_tables(cur: Cursor) -> None:
    data_table = [
        [
            "aluno_turma",
            [
                {
                    "aluno_id": 3,
                    "turma_id": 1,
                },
                {
                    "aluno_id": 5,
                    "turma_id": 1,
                },
                {
                    "aluno_id": 4,
                    "turma_id": 1,
                },
            ],
        ],
        [
            "aluno_turma",
            [
                {
                    "aluno_id": 1,
                    "turma_id": 2,
                },
                {
                    "aluno_id": 1,
                    "turma_id": 3,
                },
                {
                    "aluno_id": 1,
                    "turma_id": 4,
                },
            ],
        ],
    ]

    print("Starting inserting into aluno_turma")

    for data in data_table:
        try:
            __insert_data(cur, data[0], data[1])
        except Exception as e:
            print(f"An error occurred: {e}")
    print("Table populated Succesfully")


if __name__ == "__main__":
    with psycopg.connect(
        f"host={DB_HOST} dbname={DB_NAME} user={USER_NAME} password={USER_PWD}",
        autocommit=True,
    ) as conn:
        with conn.cursor() as cur:
            populate_tables(cur)
