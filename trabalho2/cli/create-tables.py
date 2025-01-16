import psycopg

USER_NAME = "539628"
USER_PWD = "539628"
DB_HOST = "200.129.44.249"
DB_NAME = "antgabriel_539628_ed1"


def create_tables() -> None:
    with psycopg.connect(
        f"postgres://{USER_NAME}:{USER_PWD}@{DB_HOST}/{DB_NAME}"
    ) as conn:
        # Open a cursor to perform database operations
        with conn.cursor() as cur:
            # Execute a command: this creates a new table
            cur.execute("""
                CREATE TABLE IF NOT EXISTS test (
                    id serial PRIMARY KEY,
                    num integer,
                    data text)
                """)

            # Pass data to fill a query placeholders and let Psycopg perform
            # the correct conversion (no SQL injections!)
            cur.execute(
                "INSERT INTO test (num, data) VALUES (%s, %s)", (100, "abc'def")
            )

            # Query the database and obtain data as Python objects.
            cur.execute("SELECT * FROM test")
            cur.fetchone()
            # will return (1, 100, "abc'def")

            # You can use `cur.fetchmany()`, `cur.fetchall()` to return a list
            # of several records, or even iterate on the cursor
            for record in cur:
                print(record)

            # Make the changes to the database persistent
            conn.commit()


if __name__ == "__main__":
    create_tables()
