num = int(input("Enter a positive natural number: "))

print("Number: ", num)

n = num%2

if(n==1):
    print("Number: ", num, "it's prime")
if(n==0):
    print("Number: ", num, "it's not prime")
