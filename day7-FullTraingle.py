n=int(input("Enter Row:"))
for i in range(1,n):
    for k in range(n-i+1):
        print("",end=" ")
    for j in range(1,i+1):
        print(j ,end=" ")
    print()
