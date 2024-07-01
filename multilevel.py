class a:
    def sum(self,n):
        for i in range(1,n+1):
            for j in range(i):
                print("*",end="")
            print()
class b(a):
    def add(self,n1,n2):
        print("b child")
        c=n1+n2
        print(c)
class c(b):
    def mul(m1,m2):
        print(m1*m2)
obj=c()
obj.sum(5)
obj.add(10,20)
        
