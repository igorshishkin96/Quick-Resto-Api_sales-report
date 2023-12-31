# Извлечение данных из API QuickResto

Этот скрипт на Python извлекает данные из API QuickResto за заданный период времени и создает отчет По продажам в формате Excel.

## Подготовка

- Python 3.x
- Необходимые пакеты Python: `quick-resto-API`, `openpyxl`, `requests`

## Установка

1. Клонируйте этот репозиторий на ваше локальное устройство.
2. Установите необходимые пакеты, выполнив:

   ```bash
   pip install quick-resto-API openpyxl requests

## Конфигурация

1. Создайте файл `config.json` в корневой директории проекта со следующим содержимым:

```json
{
  "username": "ЛОГИН_ДЛЯ_API",
  "password": "ПАРОЛЬ_ДЛЯ_API"
}
```

Замените значения на свои данные.

## Использование

1. Запустите скрипт `main.py` для извлечения данных из API QuickResto и создания отчетов.

```
python main.py
```

2. Скрипт выполнит следующие действия:
    - Запросит начальную и конечную дату формирования отчета по продажам;
    - Выгрузит список чеков за указанный период;
    - Сформирует "предварительный" отчет по продажам;
    - Отформатирует данные;
    - Сохранит отчет по продажам в excel-файл, с уникальным именем (`sales_report_начальная_дата_конечная_дата.xlsx`)
3. Сгенерированный отчет по продажам будет сохранен в директории проекта.

## Функции для работы с API

### `api.py`

- `get_orders_list(start_datetime_str, end_datetime_str)`: Извлекает список чеков за указанный период, с помощью get-запроса.


### `check_processing.py`

- `process_orders_data(orders_list)`: Проходит по всем чекам, попутно запрашивая подробную информацию о заказе из модуля `quick_resto_API.operations_with_objects.modules.order_info_operations.OrderInfoOperations`

## Лицензия

Этот проект лицензирован в соответствии с лицензией MIT - подробности в файле [LICENSE](LICENSE).
