T=int(input())
for i in range(T):
    N,X=map(int,input().split())
    quo=(N*X)//4
    if((N*X)%4==0):
        print(quo)
    elif((N*X)%4!=0):
        print(quo+1)
