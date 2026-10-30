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
numbers.remove(20)

print(numbers)
numbers.discard(50)

print(numbers)
numbers.pop()

print(numbers)
numbers.clear()

print(numbers)
new_numbers = numbers.copy()

print(new_numbers)
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print(a.union(b))
print(a.intersection(b))
print(a.difference(b))
print(a.symmetric_difference(b))
print(a.issubset(b))
print(a.issuperset(b))
print(a.isdisjoint(b))