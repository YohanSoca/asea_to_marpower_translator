from api_db import api_data_base as db
import random
import minimalmodbus
import time

class ASEALayer:
    def __init__(self):
        self.table = []
        self.db = db
        #self.module =  minimalmodbus.Instrument('COM5', 1)

    def read_spc(self, value):
        time.sleep(0.5)
        print(f"Inserting value: {value} into database")
        try:
           if value != '':
              return value
           else: 
            return '00' 
        except:
            return 0     

    def run_puller(self):
        temp = [{'name': data['name'], 'asea_cmd': data['asea_cmd'], 'value': self.read_spc(data['spc_register']), 'spc_register': data['spc_register']} for data in self.db] 
        self.db = temp  

    def toString(self):
        [print(f"Name: {data['name']}, Value: {data['value']}") for data in self.db]        

conv = ASEALayer()
conv.run_puller()     
conv.toString()