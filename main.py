from api import get_orders_list
from check_processing import process_orders_data
from create_exel_file import create_excel_file, forming_data

# Установка периода для запроса данных
start_datetime_str = input("Введите начальную дату(в формате YYYY-MM-DD): ")
end_datetime_str = input("Введите конечную дату(в формате YYYY-MM-DD): ")

# Получаем список чеков за указанный период
orders_list = get_orders_list(start_datetime_str, end_datetime_str)

# Получаем отчет по продажам
product_data = process_orders_data(orders_list)

# Форматируем данные для записи в Excel-файл
headers_report, product_report_data = forming_data(product_data)

# Записываем Отчет по продажам в Excel-файл
create_excel_file(f"sales_report_{start_datetime_str}_{end_datetime_str}.xlsx", headers_report, product_report_data)


