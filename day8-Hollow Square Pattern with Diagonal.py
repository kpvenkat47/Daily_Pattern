n=int(input("Enter Row:"))
for i in range(1,n+1):
    for j in range(1,n+1):
        if(i==1 or j==1 or i==n or j==n or i==j or j==(n-i+1)):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
