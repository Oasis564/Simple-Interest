def Sum(num1, num2):
    result = num1 + num2
    return result

def double(num1):
    x = num1*2
    return x

result = Sum(5,8)
x = double(6)

print(result)

print(x)

names = ["James", "Alexandra", "Kevin"]

print(names)

# Add Osaeid's name in the list.

names.append("Osaeid")

print(names)

# Change the position of Osaeid so it comes at the beginning.

new_order = [3, 0, 2, 1]
reordered_list = [names[i] for i in new_order]
print(reordered_list)

# Remove Alexandra from the list

names.pop(1)

print(names)

# Remove Kevin from the list without Pop


names.remove("Kevin")
print(names)

# Add three new names in the list

names.extend(["Robbie", "David", "Julia"])
print(names)