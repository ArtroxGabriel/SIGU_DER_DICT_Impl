from psycopg import Cursor, sql
from psycopg import connect
from psycopg.cursor import Cursor

USER_NAME = "postgres"
USER_PWD = "postgres"
DB_HOST = "localhost"  # "200.129.44.249"
DB_NAME = "teste_db"

def call_procedure(cur: Cursor, semester: int) -> None:
    """
    Calls the inc_semestre procedure with the given semester.
    """
    query = sql.SQL("CALL inc_semestre(%s)")
    cur.execute(query, (semester,))  # Use parameterized query
    print(f"Procedure inc_semestre called with semester: {semester}")

if __name__ == "__main__":
    try:
        with connect(
            f"host={DB_HOST} dbname={DB_NAME} user={USER_NAME} password={USER_PWD}",
            autocommit=True,
        ) as conn:  # Type: Connection
            with conn.cursor() as cur:  # Type: Cursor
                semester = 1  # Example semester value
                call_procedure(cur, semester)
    except Exception as e:
        print(f"An error occurred: {e}")