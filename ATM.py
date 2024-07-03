x=int(input())
y=int(input())
if x%5==0:
    if x>y:
        print("insuffient funds")
        print(y)
    else:
        print("Balance is  %0.2f "%((y-x)-0.50))
else:
    print("Incorrect Withdrawal Amount ")
    print(y)
