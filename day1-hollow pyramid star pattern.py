n=7

for i in range(1,n):
    for j in range(n-i+1):
        print(" ",end=" ")
    for k in range(2*i-1):
        if(i==1 or i==n-1 or k==0 or k==(2*i-1)-1):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
