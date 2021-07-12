n=int(input("Enter Row Value:"))
for row in range(n):
    for space in range(n-row):
        print(" ",end="")
    for column in range(row):
        print("*",end=" ")
    print()
