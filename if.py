w=int(input("enter the weight of watermelon:"))
if(w%2!=0 or w==2):
    print("no it is odd")
else:
    x=w/2
    if(x%2==0):
        print("yes brother1 get",x,"yes brother2 get", x)

    else:
        print("yes brother1 get",x-1,"yes brother2 get",x+1)
