import random

random_numbers = [random.random() for x in range(0,10)]

with open("randomnum.txt", "w") as file:
    for number in random_numbers:
        file.write(str(number) + "\n")
