from api_db import api_data_base as db
import random

[print(f"One time commads -> {data['asea_cmd']} \n") for data in db if data['type'] == 'one-time']

[print(f"Keep alive commads -> {data['asea_cmd']} \n") for data in db if data['type'] == 'keep-alive']