#Second Largest
A,B,C=map(int,input().split())
if(A>B and A>C):
    if(B>C):
        print(B)
    else:
        print(C)
else:
    if(B<C and B<A):
        print(B)
    else:
        print(C)
    
