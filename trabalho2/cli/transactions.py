from psycopg import Cursor, Connection, sql
import psycopg

USER_NAME = "539628"
USER_PWD = "539628"
DB_HOST = "200.129.44.249"
DB_NAME = "antgabriel_539628_ed1"


def close_classroom(conn: Connection, cur: Cursor, class_code: str) -> None:
    with conn.transaction():
        # close classroom
        close_query = sql.SQL("""
        UPDATE turma
        SET estado = 'Fechado'
        WHERE codigo = {};
        """).format(class_code)

        cur.execute(close_query)

        # remove students
        clean_query = sql.SQL("""
            DELETE FROM aluno_turma
            WHERE turma_id IN (
                    SELECT id
                    FROM turma
                    WHERE codigo = {}
                );
        """).format(class_code)

        cur.execute(clean_query)


if __name__ == "__main__":
    with psycopg.connect(
        f"host={DB_HOST} dbname={DB_NAME} user={USER_NAME} password={USER_PWD}",
        autocommit=True,
    ) as conn:
        with conn.cursor() as cur:
            classroom = "CC2024DS1"
            print(f"Iniciando a transacao para fechar a turma com codigo {classroom}")
            try:
                close_classroom(conn, cur, classroom)
            except Exception as e:
                print(f"an error occurred: {e}")
            finally:
                print("Transacao concluida")
