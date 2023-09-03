from pathlib import Path

USE_LOCAL_DATA = True
ROOT_PATH = Path(__file__).resolve().parent
CSV_FILE_PATH_1 = Path.joinpath(ROOT_PATH, 'north_data', 'employees_data.csv')
CSV_FILE_PATH_2 = Path.joinpath(ROOT_PATH, 'north_data', 'customers_data.csv')
CSV_FILE_PATH_3 = Path.joinpath(ROOT_PATH, 'north_data', 'orders_data.csv')