from api_db import api_data_base as db
import random
import minimalmodbus
import time

from marpower_simulator import Marpower

class ASEALayer:
    def __init__(self):
        self.table = []
        self.db = db
        self.module =  Marpower()

    def read_spc(self, value):
        return self.module.query_register(value)

    def run_puller(self):
        temp = [{'name': data['name'], 'asea_cmd': data['asea_cmd'], 'value': self.read_spc(data['spc_register']), 'spc_register': data['spc_register']} for data in self.db] 
        self.db = temp  

    def toString(self):
        [print(f"Name: {data['name']}, Value: {data['value']}") for data in self.db]        

conv = ASEALayer()
conv.run_puller()     
conv.toString()