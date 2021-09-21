#Calculate return value based on amount and interest rate in python
P = float(input("Enter the principal amount : "))
N = float(input("Enter the number of years : "))
R = float(input("Enter the rate of interest : "))
SI = (P * N * R)/100
print("Simple interest : {}".format(SI))
