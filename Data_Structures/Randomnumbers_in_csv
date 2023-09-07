import csv
import random

with open("prueba.csv", mode = "r") as csv_file:
    csv_reader = csv.DictReader(csv_file)
    line_count = 0
    
    for row in csv_reader:
        if line_count == 0:
            print(f'Random numbers')
            line_count += 1
        print(f'\t{row}')
        line_count +=1
    print(f'Proccesed {line_count} lines')
    
