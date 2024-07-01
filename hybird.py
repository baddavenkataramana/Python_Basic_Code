class a:
    def sum(self,n):
        for i in range(1,n+1):
            for j in range(i):
                print("*",end="")
            print()
class b:
    def add(self,n1,n2):
        print("b child")
        print(n1+n2)
class c:
    def div(self,d):
        for i in range(d):
            for j in range(i+1):
                print(end=" ")
            for j in range(i):
                print("*",end=" ")
            print()
class d(a,b,c):
    def sub(self,v,e):
        print(v-e)
obj=d()
obj.sum(5)
obj.add(10,20)
obj.div(5)
obj.sub(2,4)
