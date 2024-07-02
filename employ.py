# Create an employee class
class employee:
    def __init__(self,name,empid):
        self.name=name
        self.empid=empid
    def printed(self):
        print("my class")
emp1=employee("sai",7989)
print('name:',emp1.name)
print('empid',emp1.empid)
emp1.printed()
emp1.name='gayatri'
print(emp1.name)
emp1.empid=503
print(emp1.empid)
