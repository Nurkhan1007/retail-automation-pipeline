import configparser
import psycopg2
import os
import logging
from psycopg2.extras import execute_values

dirname = os.path.dirname(__file__)
parent_dir = os.path.dirname(dirname)

class DBManager:
    def __init__(self, host, port, database, user, password):
        self.host = host
        self.port = port
        self.database = database
        self.user = user
        self.password = password

        self.connection = psycopg2.connect(
            host=host, port=port, database=database, user=user, password=password
        )
        self.cursor = self.connection.cursor()
        self.connection.autocommit = False

    def insert_data(self, records):
        if not records:
            logging.info("Нет данных для загрузки в БД")
            return
        query = """
        INSERT INTO sales (
        doc_id, shop_num, cash_num, item, category, 
        amount, price, discount, total_sum, source_file
        ) VALUES %s
        ON CONFLICT ON CONSTRAINT sales_unique DO NOTHING;
        """
        try:
            execute_values(self.cursor, query, records)
            logging.info(f"Успешно обработано записей: {len(records)}")
            self.connection.commit()
        except Exception as e:
            logging.error(f"Ошибка при массовой вставке данных: {e}")
            self.connection.rollback()
            raise e

    def close_connection(self):
        self.cursor.close()
        self.connection.close()
