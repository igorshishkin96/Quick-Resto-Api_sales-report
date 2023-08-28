import json
from quick_resto_API.quick_resto_api import QuickRestoApi
from config import username, password


def get_orders_list(start_datetime_str, end_datetime_str):
    # Хотел использовать Filter из модуля quick_resto_API.operations_with_objects.list_request.filter
    # Но в таком случае value может принять только строку, а нам необходим словарь, так как operation-range
    # Либо я недостаточно изучил API
    data = {
        "filters": [{
            "field": "serverRegisterTime",
            "operation": "range",
            "value": {
                "since": start_datetime_str,
                "till": end_datetime_str
            }
        }]
    }

    params = {
        "moduleName": "front.orders",
        "className": "ru.edgex.quickresto.modules.front.orders.OrderInfo"
    }

    response = api.get(
        url="api/list",
        parameters=params,
        json_data=data,
    )

    return json.loads(response.text)


api = QuickRestoApi(
    login=username,
    password=password,
)
