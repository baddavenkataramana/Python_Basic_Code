#factorial logic
n=int(input())
count=1
while n>0:
    count*=n
    n-=1
print(count)
