class a:
    def sum(self,n):
        for i in range(1,n+1):
            for j in range(i):
                print("*",end="")
            print()
class b(a):
    def add(self,n1,n2):
        print("b child")
        print(n1+n2)
class c(a):
    def div(self,d):
        for i in range(d):
            for j in range(i):
                print(end=" ")
            for j in range(i):
                print("*",end=" ")
            print()
obj=c()
obj1=b()
obj.sum(5)
obj1.add(10,20)
obj.div(5)
