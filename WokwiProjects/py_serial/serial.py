import time, serial

esp = serial.Serial("COM3", 9600)

esp.write(input().encode())

time.sleep(0.1)

esp.close()
