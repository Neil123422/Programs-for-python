def fibonacci_series(n):
    a,b= 0,1 
    print("Fibonnaci series:")
    
    for _ in range(n):
        print(a, end="")
        a,b= b,a+b  
terms= int(input("Enter the maximum digit till which you want to print the fibonnaci series:"))
fibonacci_series(terms)



