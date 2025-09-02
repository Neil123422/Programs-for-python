def SI(p,t=2,r=0.10 ):
    return(p*r*t)/100
principle=float(input("Enter the principle amount: "))
time=float(input("Enter the time in years: "))
rate=float(input("Enter the rate of interest: "))
print("The simple interest is: ",SI(principle,time,rate))
print("The simple interest is with default values: ",SI(principle))