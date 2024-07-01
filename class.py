class studentdata:
    def __init__ (self,name,rollno,cmark,jmark,pmarks):
        self.name=name
        self.rollno=rollno
        self.cmarks=cmark
        self.engmarks=jmark
        self.pymarks=pmarks
    
    def printalldetails(self):
        print(self.name)
        print(self.rollno)
        print(self.cmarks)
        print(self.engmarks)
        print(self.pymarks)
obj1=studentdata("bvr","503",80,98,67)
print(obj1.printalldetails())
obj2=studentdata("sai","204",90,80,86)
print(obj2.printalldetails())
