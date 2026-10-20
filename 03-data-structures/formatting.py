a=50
b=20
c=30
sum=b+c
difference=c-b
#normal formatting
print("the language is {}".format("python"))
print("The sum of b and c is {}".format(sum))
print("The sum of {} and {} is {}".format(b,c,sum))
#index based formatting
print("The sum is {2} of {0} and {1}".format(b,c,sum))
#value based formatting
print("The sum of {a} and {b} is {sum}".format(a=10,b=25,sum=10+25))
