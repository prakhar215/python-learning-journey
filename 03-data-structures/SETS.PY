# Creating a set
numbers = {10, 20, 30, 40, 50}

print(numbers)

# Duplicate values are automatically removed
numbers = {10, 20, 20, 30, 30, 40}

print(numbers)
#SETS METHOD
numbers.add(10)
print(numbers)
numbers.update([20,30,40,50])
print(numbers)