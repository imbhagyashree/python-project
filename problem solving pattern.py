for i in range(1, 6):  # rows
    for j in range(1,i+1):  # columns
        print("j", end=" ")
    print()
 #write a program to display this pattern
for i in range(1, 6):  # rows
    for j in range(1, i + 1):  # columns
        print(i, end=" ")
    print()
#write a program to display this pattern
for i in range(1, 6):  # rows
    for j in range(6,i,-1):  # columns
        print(i, end=" ")
    print()
 # write a program to display this pattern
for i in range(1, 6):
    for j in range(4, i - 1, -1):
        print(" ", end=" ")
    for k in range(i):
        print("*", end=" ")
    print()
#write a program to display this pattern
for i in range(1, 6):
    for j in range(i, 0, -1):
        print(j, end=" ")
    print()
    # write a program to display this pattern
    # Ascending part of the pattern
    for i in range(1, 6):
        for j in range(1, i + 1):
            print("*", end=" ")
        print()

    # Descending part of the pattern
    for i in range(5, 0, -1):
        for k in range(1, i):
            print("*", end=" ")
        print()
    # write a program to dispaly this pattern
    for i in range(1, 11):
        for j in range(1, i + 1):
            print(i * j, end=" ")
        print()


