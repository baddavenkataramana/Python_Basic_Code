n=5
fact=1
if(n<0):
    print('sorry not negitive fact.')
elif(n==0):
    print('it 0 is a fact1')
else:
    for i in range(1,n+1):
        fact=fact*i
    print("fact of n {0} is {1}".format(n,fact))
          
