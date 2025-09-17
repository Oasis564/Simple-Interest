# # Find the formula for simple interest

# # SI = (Principal × Rate × Time)/100

# # Write the code to find the simple interest

# principle = float(input("Enter the principle"))
# rate = float(input("Enter the rate"))
# time = float(input("Enter the time"))

# si = (principle*rate*time)/100
# print("The total amount is £",si,".")

# # Convert the above into a function





# # Find the formula for Compound Interest

# # A = P(1 + r/n)^(nt)
# # Where:
# # A = the final amount (principal + interest)
# # P = the principal amount (initial investment)
# # r = annual interest rate (as a decimal)
# # n = number of times interest is compounded per year
# # t = number of years the money is invested or borrowed. 

# # This formula allows you to calculate the total amount after interest has been applied over a specified period.


# # Write the code to get the compound interest

# p = float(input("Enter the principle"))
# r = float(input("Enter the rate"))
# n = float(input("Enter the number of times the interest has been compound"))
# t = float(input("Enter the time"))

# a = p * (1 + r / n) ** (n * t)


# print("The result of the compound interest is: £", a)

# Make the above into a function

def Sinterest(principle, rate, time):
    principle = float(input("Enter the principle"))
    rate = float(input("Enter the rate"))
    time = float(input("Enter the time"))
    si = (principle*rate*time)/100
    return si

principle = float(input("Enter the principle"))
rate = float(input("Enter the rate"))
time = float(input("Enter the time"))

si = Sinterest(principle,rate,time)
print("The resulted simple interest amount is £", si)

print("========================================================")


def CDinterest(p, r, n, t):
    a = p * (1 + (r / n)) ** (n * t)
    return a


p = float(input("Enter the principle"))
r1 = float(input("Enter the rate"))
r = r1/100
n = float(input("Enter the number of times the interest has been compound"))
t = float(input("Enter the time"))
a = CDinterest(p,r,n,t)
print("The resulted compound interest amount is £", a)



if(a > si):
    print("Compound interest is better.")
    print("You have saved: ", a-si)
else:
    print("Simple interest is better.")
    print("You have saved: ", si-a)

# Write a program to check if the simple interest or compound interest is better.