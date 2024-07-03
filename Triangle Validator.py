a,b,c=map(int,input().split())
if(a+b>c):
    if(b+c>a):
        if(c+a>b):
            print("Yes")
        else:
            print("No")
