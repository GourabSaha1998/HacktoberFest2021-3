# Star printing
num = int(input("Enter the number of rows:\n"))
boolean = input("Enter 1 or 0:\n")
i = 1
if boolean == "1":
    while i <= num:
        j = 1
        while j <= i:
            print("*", end=" ")
            j = j + 1
        print(" ")
        i = i + 1
else:
    while i <= num:
        j = num
        while j >= i:
            print("*", end=" ")
            j = j - 1
        print(" ")
        i = i + 1
