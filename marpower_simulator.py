from operator import add
import random
import time

import minimalmodbus
import serial

class Marpower:
    def __init__(self):
        self.unit = minimalmodbus.Instrument('COM4', 2)                   
        self.unit.serial.baudrate = 19200         
        self.unit.serial.bytesize = 8
        self.unit.serial.parity   = serial.PARITY_NONE
        self.unit.serial.stopbits = 1                        
        self.unit.mode = minimalmodbus.MODE_RTU   
        self.table = []
        self.update_table

    def query_register(self, address):
        try:
            unit = minimalmodbus.Instrument('COM4', 2)
            unit.serial.baudrate = 19200
            unit.serial.bytesize = 8
            unit.serial.parity   = serial.PARITY_EVEN
            unit.serial.stopbits = 1
            unit.mode = minimalmodbus.MODE_RTU

            val = unit.read_register(address)
            return val
        except:
            return '0'        

    def update_table(self):        
        self.table = [{'register': reg, 'value': self.query_register(reg)} for reg in range(4096, 4218)]   
        print(self.table)

    def query_table(self, address):
        print(f"Register {address}, is been interogating")
        if address == '':
            address = '0'
        print(self.table[int('0x' + str(address), 16)])
        time.sleep(1)
        return self.table[int('0x' + str(address), 16)]

