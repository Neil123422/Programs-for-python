str= input("Enter a string")
print("The string", str ,"in reverse order is: ")
length= len(str)
for a in range(-1,(-length-1),-1):  
    print(str[a],end="")