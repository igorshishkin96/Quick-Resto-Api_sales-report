import json

with open('config.json') as config_data:
    config_data = json.load(config_data)
    username = config_data["username"]
    password = config_data["password"]