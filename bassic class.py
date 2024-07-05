class student:
    pass
s1=student()
s2=student()
s3=student()
print(s2,s3)
s1.name='bvr'
s1.roono=503
s2.name='sri sai'
s3.roolno=530
print(s1.__dict__)
print(s2.__dict__)
print(s3.__dict__)
print(hasattr(s1,'name'))
print(hasattr(s2,'name'))
print(hasattr(s3,'name'))
print(getattr(s1,'name'))
print(getattr(s2,'name'))
print(getattr(s3,'roolno'))
print(delattr(s1,'name'))
print(s1.__dict__)
      
