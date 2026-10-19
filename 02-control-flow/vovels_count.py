word=input(str("Enter the word:"))
count=0
for char in word:
    if(char=='a' or char=='e' or char == 'i' or char =='o' or char=='u'):
        count+=1
print("vovels count in word is ",count)