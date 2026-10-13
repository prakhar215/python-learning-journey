
maths = 85
science = 90
english = 78
total_subjects = 3

# Arithmetic operators
total = maths + science + english
percentage = total / total_subjects

print("Total Marks:", total)
print("Percentage:", percentage)

# Comparison operators
print("Passed:", percentage >= 40)

# Logical operators
print("Excellent Result:", percentage >= 80 and total <= 300)

# Assignment operators
total += 5
print("Bonus Marks Added:", total)

# Membership operator
grades = ["A", "B", "C"]
print("Grade A Available:", "A" in grades)
