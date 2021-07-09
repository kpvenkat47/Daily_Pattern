n=int(input("Enter row size:"))
for i in range(n):
    for j in range(n-i):
        print("*",end=" ")
    print()
