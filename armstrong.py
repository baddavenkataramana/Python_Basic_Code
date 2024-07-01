import math
n=int(input("Enter the number: "))
m=math.sqrt(n)
if(m.is_integer()):
    print(n," is a perfect square")
else:
    print(n," is not a perfect square")
    

