from operator import add
import random
import time

class Marpower:
    def __init__(self):
        self.table = []
        self.update_table

    def update_table(self):
        self.table = [(x / 100) for x in range(0, 10000)]

   

    def query_register(self, address):
        if address == '':
            address = '0'
        print(self.table[int('0x' + str(address), 16)])
        time.sleep(1)
        return self.table[int('0x' + str(address), 16)]

