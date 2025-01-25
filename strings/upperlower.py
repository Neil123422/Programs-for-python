string= input("Enter any string:")
lowercount=uppercount=0 
digitcount=alphacount=symcount=0
for a in string:
    if a.islower():
        lowercount+=1
    elif a.isalpha():
      alphacount+=1
    elif a.isdigit():
       digitcount+=1
    elif a.isupper():
       uppercount+=1
    elif a.isalnum() != True and a != " ":
       symcount+=1
print("alphabets count:",alphacount)              
print("digit count:",digitcount)
print("lowercase count:",lowercount)
print("uppercase count:",uppercount)
print("symbol count:",symcount)

