t=int(input())
for i in range(t):
    #No of students
    #M capacity of the course
    #already regested in course
    N,M,K=map(int,input().split())
    if(N<=(M-K)):
        print("Yes")
    else:
        print("No")
