import serial
import time

port = "COM4"
baud = 19200

ser = serial.Serial(port, baud, timeout=1)
# open the serial port
if ser.isOpen():
    print(ser.name + ' is open...')


cmds = [{'Frecuency': ':MEASure:SP1:FREQuency'}, {'L1 voltage': ':MEASure:SP1:VLL1 '}, {'L2 voltage': ':MEASure:SP1:VLL2'}, {'l3 voltage': ':MEASure:SP1:VLL3'}];
values = []

while True:
    for cmd in cmds:
        for key in cmd.keys():
            ser.write(cmd[key].encode('ascii') + '\r\n'.encode())
            res = ser.readline()
            res = res.decode('ascii').split("\r")[0]
            values.append({f"{key}: {res}"})

        # ser.write(cmd.encode('ascii') + '\r\n'.encode())
        # res = ser.readline()
        # values.append(res.decode('ascii').split("\r")[0])

    print(values)
    values = []
    time.sleep(3)