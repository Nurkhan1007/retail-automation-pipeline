import random
import os
import pandas as pd
from logger import setup_logging, cleanup_logs
import configparser
import uuid

parent_dir = os.path.dirname(os.path.dirname(__file__))
save_path = os.path.join(parent_dir, 'data')

config = configparser.ConfigParser()
config.read(os.path.join(parent_dir, 'config.ini'))
generate_creds = config['generator']

shops_count = int(generate_creds['shops_count'])
cashboxes_per_shop = int(generate_creds['cashboxes_per_shop'])
min_receipts = int(generate_creds['min_receipts'])
max_receipts = int(generate_creds['max_receipts'])

logger = setup_logging()
cleanup_logs()

products = [
    {
        'item': 'Fairy',
        'category': 'Бытовая химия',
        'min_price': 700,
        'max_price': 1200
    },
    {
        'item': 'Domestos',
        'category': 'Бытовая химия',
        'min_price': 1200,
        'max_price': 2500
    },
    {
        'item': 'Ariel',
        'category': 'Бытовая химия',
        'min_price': 3500,
        'max_price': 7000
    },
    {
        'item': 'Lenor',
        'category': 'Бытовая химия',
        'min_price': 1800,
        'max_price': 4000
    },
    {
        'item': 'Mr Proper',
        'category': 'Бытовая химия',
        'min_price': 1000,
        'max_price': 2500
    },
    {
        'item': 'Полотенце',
        'category': 'Текстиль',
        'min_price': 2500,
        'max_price': 6000
    },
    {
        'item': 'Постельное белье',
        'category': 'Текстиль',
        'min_price': 12000,
        'max_price': 35000
    },
    {
        'item': 'Плед',
        'category': 'Текстиль',
        'min_price': 7000,
        'max_price': 20000
    },
    {
        'item': 'Шторы',
        'category': 'Текстиль',
        'min_price': 15000,
        'max_price': 50000
    },
    {
        'item': 'Сковорода',
        'category': 'Посуда',
        'min_price': 6000,
        'max_price': 18000
    },
    {
        'item': 'Кастрюля',
        'category': 'Посуда',
        'min_price': 8000,
        'max_price': 25000
    },
    {
        'item': 'Набор тарелок',
        'category': 'Посуда',
        'min_price': 5000,
        'max_price': 15000
    },
    {
        'item': 'Кружка',
        'category': 'Посуда',
        'min_price': 1200,
        'max_price': 4000
    },
    {
        'item': 'Контейнер для еды',
        'category': 'Кухонная утварь',
        'min_price': 800,
        'max_price': 3000
    },
    {
        'item': 'Разделочная доска',
        'category': 'Кухонная утварь',
        'min_price': 1500,
        'max_price': 5000
    },
    {
        'item': 'Нож кухонный',
        'category': 'Кухонная утварь',
        'min_price': 3000,
        'max_price': 12000
    },
    {
        'item': 'Губка для посуды',
        'category': 'Хозтовары',
        'min_price': 300,
        'max_price': 900
    },
    {
        'item': 'Мусорные пакеты',
        'category': 'Хозтовары',
        'min_price': 500,
        'max_price': 2000
    },
    {
        'item': 'Швабра',
        'category': 'Хозтовары',
        'min_price': 4000,
        'max_price': 12000
    },
    {
        'item': 'Ведро',
        'category': 'Хозтовары',
        'min_price': 2000,
        'max_price': 7000
    }
]
os.makedirs(save_path, exist_ok=True)
#генерируем данные
logger.info('Старт генерации файлов продаж.')
for shop in range(1, shops_count+1):
    for cash in range(1, cashboxes_per_shop+1):
        logger.info(f'Генерация файла для магазина {shop}, кассы {cash}')
        records = []
        receipt_count = random.randint(min_receipts, max_receipts)
        for receipts in range(receipt_count):
            doc_id = uuid.uuid4().hex[:12]
            items_count = random.randint(1, 7)
            for item_num in range(items_count):
                product = random.choice(products)
                amount = random.randint(1, 5)
                price = random.randint(product['min_price'], product['max_price'])
                if random.random() < 0.3:
                    discount = round(price*amount*random.uniform(0.05, 0.2), 2)
                else:
                    discount = 0
                records.append({
                    'doc_id':doc_id,
                    'item':product['item'],
                    'category':product['category'],
                    'amount':amount,
                    'price':price,
                    'discount':discount
                })
        df = pd.DataFrame(records)
        file_name = f'{shop}_{cash}.csv'
        file_path = os.path.join(save_path, file_name)
        df.to_csv(file_path, index=False, encoding='utf-8-sig')
        logger.info(f'Файл создан: {file_name}, строк: {len(df)}')
logger.info('Генерация файлов завершена')