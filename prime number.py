#Python program to check if the number is an prime number or not

n=int(input("enter the trhe number:"))
flag=False
if(n==1):
    print("1 is not a number.")
elif(n>1):
    for i in range(2,n):
        if(n%i==0):
            flag=True
            break
    if flag:
        print(n,"is a not a prime number.")
    else:
        print(n,"is prime number.")
