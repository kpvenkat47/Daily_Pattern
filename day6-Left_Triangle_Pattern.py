n=int(input())
m=n//2-1
v=m+1
for i in range(n):
    for j in range(i):
        if(i<=m):
            print("*",end=" ")
    for k in range(n,i,-1):
        if(i>=v ):
            print("*",end=" ")                      
    print()

