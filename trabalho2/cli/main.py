import logging
import psycopg

from create_tables import create_tables
from insert_data import insert_data

USER_NAME = "postgres"
USER_PWD = "postgres"
DB_HOST = "localhost"  # "200.129.44.249"
DB_NAME = "teste_db"

if __name__ == "__main__":
    logger = logging.getLogger("Logger")
    logger.setLevel(logging.INFO)
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    formatter = logging.Formatter("%(name)s - %(levelname)s - %(message)s")
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    with psycopg.connect(
        f"host={DB_HOST} dbname={DB_NAME} user={USER_NAME} password={USER_PWD}"
    ) as conn:
        with conn.cursor() as cur:
            create_tables(logger, conn, cur)
            insert_data(logger, conn, cur)
