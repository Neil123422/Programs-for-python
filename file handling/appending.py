with open("demo1.txt","w") as f:
    f.write("Hello, World!")

with open("demo1.txt","a") as f:
    f.write("\nWelcome to File Handling in Python.")
with open("demo1.txt","r") as f:
    print(f.read())