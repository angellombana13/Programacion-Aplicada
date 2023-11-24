import time, serial

esp = serial.Serial("COM3", 9600)

command = '0'

while command!='q':
    esp.write(command.encode())
    command = str(input())

esp.close()
