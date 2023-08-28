from datetime import datetime
from quick_resto_API.operations_with_objects.modules.order_info_operations import OrderInfoOperations
from api import api


def process_orders_data(orders_list):
    product_data = {}

    # Проходим по всем чекам для вычисления статистики и получения подробной информации
    for order in orders_list:
        order_operations = OrderInfoOperations(api=api)

        # Получаем objectId для запроса подробной информации о чеке
        if order.get("id") is not None:
            check = order_operations.get_order_info_with_subobjects(
                objectId=order.get("id"),
            )
            returned = check.returned
            sale_date = datetime.strptime(check.create_date, '%Y-%m-%dT%H:%M:%S.%fZ')

            # Проходим по всем позициям чека
            for el in check.order_item_list:
                # Обновляем данные, если продукт уже ранее продавался, иначе создаем новую запись
                if el.name in product_data:
                    if not product_data[el.name]["first_sale_date"] or sale_date < product_data[el.name]["first_sale_date"]:
                        product_data[el.name]["first_sale_date"] = sale_date
                    if not product_data[el.name]["last_sale_date"] or sale_date > product_data[el.name]["last_sale_date"]:
                        product_data[el.name]["last_sale_date"] = sale_date

                    if returned:
                        product_data[el.name]["total_returned"] += el.total_amount
                    else:
                        product_data[el.name]["amount"] += el.amount
                        product_data[el.name]["total_profit"] += (el.total_amount - el.cost_price * el.amount)
                    product_data[el.name]["total_discount"] += (el.total_absolute_discount - el.total_absolute_charge)
                    product_data[el.name]["price"] = el.price
                else:
                    product_data[el.name] = {}
                    if not returned:
                        product_data[el.name]["first_sale_date"] = sale_date
                        product_data[el.name]["last_sale_date"] = sale_date
                        product_data[el.name]["amount"] = el.amount
                        product_data[el.name]["total_returned"] = 0
                        product_data[el.name]["total_profit"] = (el.total_amount - el.cost_price * el.amount)
                        product_data[el.name]["total_discount"] = (
                                    el.total_absolute_discount - el.total_absolute_charge)
                    else:
                        product_data[el.name]["first_sale_date"] = None
                        product_data[el.name]["last_sale_date"] = None
                        product_data[el.name]["amount"] = 0
                        product_data[el.name]["total_returned"] = el.total_amount
                        product_data[el.name]["total_profit"] = 0
                        product_data[el.name]["total_discount"] = 0
                    product_data[el.name]["price"] = el.price

    return product_data
