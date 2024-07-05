T=int(input())
for i in range(T):
    X,Y=map(int,input().split())
    percent=(X/100)*(107/1)
    if(Y<=percent):
        print("Yes")
    elif(Y>percent):
        print("No")
