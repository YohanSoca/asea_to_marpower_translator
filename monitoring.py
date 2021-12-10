import pandas as pd

from api_db import api_data_base as db

cmds = [cmd['asea_cmd'] for cmd in db]

table = pd.DataFrame(cmds)

print(table)