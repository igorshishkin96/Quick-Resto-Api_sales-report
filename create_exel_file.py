import openpyxl
from openpyxl.styles import Border, Side, Alignment


# Функция для создания Excel файла с заголовками и данными
def create_excel_file(filename, headers, data):
    """
    Создает Excel файл и заполняет его данными.

    :param filename: Имя файла для сохранения.
    :param headers: Заголовки столбцов.
    :param data: Данные для заполнения таблицы.
    """
    # Создание нового Excel-файла и активного листа
    workbook = openpyxl.Workbook()
    sheet = workbook.active
    sheet.title = 'Sheet'

    # Заполнение заголовков столбцов
    sheet.append(headers)

    # Заполнение таблицы данными
    for item in data:
        sheet.append(item)

    # Настройка границ ячеек и выравнивания текста
    thin_border = Border(left=Side(style='thin'),
                         right=Side(style='thin'),
                         top=Side(style='thin'),
                         bottom=Side(style='thin'))
    header_left_alignment = Alignment(horizontal='left', vertical='center')
    value_right_alignment = Alignment(horizontal='right', vertical='center')

    # Применение стилей к ячейкам
    for row in sheet.iter_rows(min_row=1, max_row=len(data) + 1, max_col=len(headers)):
        for cell in row:
            cell.border = thin_border
            if cell == row[0]:
                cell.alignment = header_left_alignment  # Выравнивание для заголовков
            else:
                cell.alignment = value_right_alignment  # Выравнивание для данных
            max_length = max(len(str(cell.value)) for cell in row)
            adjusted_width = (max_length + 2) * 1.2
            sheet.column_dimensions[cell.column_letter].width = adjusted_width

    # Сохранение файла
    workbook.save(filename)


def forming_data(product_data):
    # Формируем данные для записи в отчет
    product_report_data = []
    headers_report = ["Дата первой продажи", "Дата последней продажи",
                      "Продукт", "Количество", "Цена, ₽", "Скидка, ₽",
                      "Возвраты, ₽", "Общая прибыль, ₽"]

    for product_name, data in product_data.items():
        product_report_data.append(
            [
                data["first_sale_date"],
                data["last_sale_date"],
                product_name,
                data["amount"],
                data["price"],
                data["total_discount"],
                data["total_returned"],
                data["total_profit"],
            ]
        )

    return headers_report, product_report_data