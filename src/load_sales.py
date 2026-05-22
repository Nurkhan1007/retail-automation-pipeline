import os
import re
import pandas as pd
from db import DBManager
import configparser
from logger import setup_logging, cleanup_logs
from dotenv import load_dotenv

load_dotenv()

logger = setup_logging()
cleanup_logs()

parent_dir = os.path.dirname(os.path.dirname(__file__))
data_path = os.path.join(parent_dir, "data")

if not os.path.exists(data_path):
    logger.error(f'Папка data не найдена: {data_path}')
    raise FileNotFoundError(f'Папка data не найдена: {data_path}')

logger.info('Старт загрузки файлов в БД')

database = DBManager(
    host = os.getenv('host'),
    port = os.getenv('port'),
    database = os.getenv('dbname'),
    user = os.getenv('user'),
    password = os.getenv('password')
)

files = os.listdir(data_path)

pattern = r"^\d+_\d+\.csv$"
try:
    for file in files:
        if re.match(pattern, file):
            file_path = os.path.join(data_path, file)
            df = pd.read_csv(file_path, encoding="utf-8-sig")
            filename = file.replace(".csv", "")
            parts = filename.split("_")
            shop_num = int(parts[0])
            cash_num = int(parts[1])
            df["shop_num"] = shop_num
            df["cash_num"] = cash_num
            df["total_sum"] = df["amount"] * df["price"] - df["discount"]
            df["source_file"] = file
            df = df[['doc_id', 'shop_num', 'cash_num', 'item', 'category', 'amount',
                    'price', 'discount', 'total_sum', 'source_file']]
            records = list(df.itertuples(index=False, name=None))
            database.insert_data(records)
            logger.info(f'Файл {file} обработан. Строк: {len(records)}')
        else:
            logger.info(f'Файл пропущен, так как не соответствует шаблону: {file}')
finally:
    database.close_connection()
    logger.info('Загрузка файлов завершена')


