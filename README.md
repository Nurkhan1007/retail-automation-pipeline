# Retail Automation Pipeline

## Описание проекта

Проект автоматизирует процесс генерации CSV-выгрузок продаж торговой сети, их обработку и загрузку в базу данных PostgreSQL.

Функционал проекта:

- генерация CSV-файлов продаж;
- автоматическая загрузка данных в PostgreSQL;
- защита от дублирования данных;
- логирование работы скриптов;
- автоматизация через cron.

---

# Используемый стек

- Python 3.10
- Pandas
- PostgreSQL
- psycopg2-binary
- python-dotenv
- Git/GitHub
- cron (Linux)

---

# Структура проекта

```text
retail-automation-pipeline/
├── data/              # CSV-файлы продаж
├── img/               # Скриншоты cron и PostgreSQL
├── logs/              # Логи работы проекта
├── sql/               # SQL-скрипты
├── src/               # Исходный код
├── .env.example       # Пример переменных окружения
├── .gitignore
├── config.ini         # Настройки генерации данных
├── requirements.txt
└── README.md
```

---

# Клонирование проекта

```bash
git clone https://github.com/Nurkhan1007/retail-automation-pipeline.git
cd retail-automation-pipeline
```

---

# Создание виртуального окружения

## Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

## Windows

```powershell
py -3.10 -m venv venv
venv\Scripts\activate
```

---

# Установка зависимостей

```bash
pip install -r requirements.txt
```

---

# Настройка переменных окружения

Создайте файл `.env` в корне проекта.

Пример содержимого:

```env
DB_HOST=localhost
DB_PORT=5432
DB_NAME=retail_db
DB_USER=postgres
DB_PASSWORD=your_password
```

---

# Создание базы данных PostgreSQL

Подключитесь к PostgreSQL:

```bash
sudo -u postgres psql
```

Создайте базу данных:

```sql
CREATE DATABASE retail_db;
```

Выйдите из PostgreSQL:

```sql
\q
```

---

# Создание таблицы

Выполните SQL-скрипт:

```bash
sudo -u postgres psql -d retail_db -f sql/ddl.sql
```

---

# Генерация CSV-файлов

Запуск генератора:

```bash
python src/generate_sales.py
```

После выполнения CSV-файлы появятся в папке:

```text
data/
```

---

# Загрузка данных в PostgreSQL

Запуск загрузчика:

```bash
python src/load_sales.py
```

---

# Проверка данных

Проверка количества строк:

```bash
sudo -u postgres psql -d retail_db -c "SELECT COUNT(*) FROM sales;"
```

Просмотр данных:

```bash
sudo -u postgres psql -d retail_db
```

```sql
SELECT * FROM sales LIMIT 10;
```

---

# Автоматизация через cron

Открыть cron:

```bash
crontab -e
```

Добавить следующие задачи:

```cron
0 8 * * 1-6 /home/USERNAME/retail-automation-pipeline/venv/bin/python /home/USERNAME/retail-automation-pipeline/src/generate_sales.py >> /home/USERNAME/retail-automation-pipeline/logs/cron.log 2>&1

10 8 * * * /home/USERNAME/retail-automation-pipeline/venv/bin/python /home/USERNAME/retail-automation-pipeline/src/load_sales.py >> /home/USERNAME/retail-automation-pipeline/logs/cron.log 2>&1
```

---

# Логирование

Логи сохраняются в папке:

```text
logs/
```

---

# Скриншоты

Скриншоты работы cron и PostgreSQL находятся в папке:

```text
img/
```