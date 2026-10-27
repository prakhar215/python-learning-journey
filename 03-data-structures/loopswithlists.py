numbers=[1,2,3,4,5,6,7]
x=4
idx=0
for val in numbers:
    if(val==x):
        print(f"x found at index= {idx}")
        break
    idx+=1