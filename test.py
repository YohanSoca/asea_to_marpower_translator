from api_db import api_data_base as db
import random

def get_data(value):
    return random.randint(value, 100)

data = [{'name': cmd['name'], 'asea_cmd': cmd['asea_cmd'], 'register': '', 'value': get_data(90)} for cmd in db]

[print(f"Name: {chunck['name']}, Value: {chunck['value']}") for chunck in data]