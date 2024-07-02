x=[[12,1],
   [3,5],
   [3,4]]
result=[[0,0,0],
        [0,0,0]]
for i in range(len(x)):
    for j in range(len(x[0])):
        result[j][i]=x[i][j]
for i in result:
    print("matrix",result)
