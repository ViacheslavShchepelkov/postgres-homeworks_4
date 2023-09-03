"""Скрипт для заполнения данными таблиц в БД Postgres."""
import csv

import psycopg2

from settings import CSV_FILE_PATH_1, CSV_FILE_PATH_2, CSV_FILE_PATH_3

csv_path_list = [CSV_FILE_PATH_1, CSV_FILE_PATH_2, CSV_FILE_PATH_3]
pg_tables = ['employees', 'customers', 'orders']
csv_data_list = []

conn_params = {
    "host": "localhost",
    "database": "north",
    "user": "postgres",
    "password": "154Dfg"
}

conn = psycopg2.connect(**conn_params)

try:
    with conn:
        for index, path in enumerate(csv_path_list):
            try:
                with open(path) as csvfile:
                    reader = csv.DictReader(csvfile)

                    with conn.cursor() as cur:
                        row: dict
                        for row in reader:
                            values = tuple(row.values())
                            values_str = '%s, ' * len(values)
                            cur.execute(f"INSERT INTO {pg_tables[index]} VALUES ({values_str[:len(values_str) - 2]})",
                                        values)
            except FileNotFoundError:
                raise FileNotFoundError(f"Отсутствует файл {path}")
finally:
    conn.close()