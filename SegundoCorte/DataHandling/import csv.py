import csv
import random
 
# field names
fields = ['Name', 'Branch', 'Year', 'CGPA']
 
# data rows of csv file
rows = [ ['Nikhil', 'COE', '2', '9.0'],
        ['Sanchit', 'COE', '2', '9.1'],
        ['Aditya', 'IT', '2', '9.3'],
        ['Sagar', 'SE', '1', '9.5'],
        ['Prateek', 'MCE', '3', '7.8'],
        ['Sahil', 'EP', '2', '9.1']]
 
# name of csv file
filename = "prueba.csv"
 
# writing to csv file
with open(filename, 'w') as csvfile:
    # creating a csv writer object
    csvwriter = csv.writer(csvfile)
     
    # writing the fields
    csvwriter.writerow(fields)
     
    # writing the data rows
    csvwriter.writerows(rows)

"""
with open("prueba.csv", "r") as csv_file:
    csv_reader = csv.DictReader(csv_file)
    line_count = 0
    
    for row in csv_reader:
        if line_count == 0:
            print(f'Company members')
            line_count += 1
        print(f'\t{row}')
        line_count +=1
    print(f'Proccesed {line_count} lines')
"""