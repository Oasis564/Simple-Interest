# Find the formula for simple interest

# SI = (Principal × Rate × Time)/100

# Write the code to find the simple interest

principle = float(input("Enter the principle"))
rate = float(input("Enter the rate"))
time = float(input("Enter the time"))

si = (principle*rate*time)/100
print("The total amount is £",si,".")

# Convert the above into a function