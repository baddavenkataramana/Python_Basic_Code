class a:
    def sum(self,n):
        for i in range(1,n+1):
            for j in range(i):
                print("*",end="")
            print()
class b:
    def add(self,n1,n2):
        print("b child")
        c=n1+n2
        print(c)
class c(a,b):
    def div(self,d):
        for i in range(d):
            for j in range(i):
                print(end=" ")
            for j in range(i):
                print("*",end=" ")
            print()
obj=c()
obj.sum(5)
obj.add(10,20)
obj.div(5)
        
