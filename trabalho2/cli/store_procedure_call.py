from psycopg import Cursor, sql
from psycopg import connect

USER_NAME = "539628"
USER_PWD = "539628"
DB_HOST = "200.129.44.249"
DB_NAME = "antgabriel_539628_ed1"


def call_procedure(cur: Cursor, semester: int) -> None:
    """
    Calls the inc_semestre procedure with the given semester.
    """
    query = sql.SQL("CALL inc_semestre(%s)")

    try:
        cur.execute(query, (semester,))  # Use parameterized query
    except Exception as e:
        print(f"An error occurred: {e}")

    print(f"Procedure inc_semestre called with semester: {semester}")


if __name__ == "__main__":
    with connect(
        f"host={DB_HOST} dbname={DB_NAME} user={USER_NAME} password={USER_PWD}",
        autocommit=True,
    ) as conn:  # Type: Connection
        with conn.cursor() as cur:  # Type: Cursor
            semester = 1  # Example semester value
            call_procedure(cur, semester)
