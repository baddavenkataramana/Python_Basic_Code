d={}
n =int(input("enter the vales:"))
for i in range(n):
    k=input("key:")
    v=input("values")
    d[k]=v
print(d)
key=input("enter the key:")
if key  in d:
    print("key is present")
else:
    print("key is not present")
    
