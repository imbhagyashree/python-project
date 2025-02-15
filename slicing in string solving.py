#fiboacci series
#a = 0
#b = 1
#n = int(input("Enter a number here: "))

#if n == 1:
 #   print(1)
#else:
 #   print(a)
  #  print(b)
   # for i in range(2, n):
    #    c = a + b
     #   a = b
      #  b = c
       # print(c)
# if number is prime or not
#num=int (input("enter a number here:"))
#if num<=1:
 #   print ("it is not a prime number ")
#else :
 #   for i in range (2,num):
  #      if num% i== 0:
   #         print ("number is not a prime number")
    #    else:
#
 #           print ("it is a prime number")

# check for palindrome
num = int(input("Enter a number here: "))
temp = num
rev = 0

while num > 0:
    dig = num % 10
    rev = rev * 10 + dig
    num = num // 10
 #area calculator
print("********AREA CALCULATOR*****")
while True:
    print("""Press 1 to get the area of square
 Press 2 to get the area of rectangle
 Press 3 to get the area of circle
 Press 4 to get the area of triangle""")

    choice = int(input("Enter a number between 1-4: "))

    if choice == 1:
        while True:
            side = float(input("Enter the length of one side: "))
            area = side ** 2
            print("The area of the square is", area)
            repeat = input("Do you want to try again with square? (yes/no): ")
            if repeat.lower() == "no":
                break

    elif choice == 2:
        while True:
            length = float(input("Enter the length of the rectangle: "))
            width = float(input("Enter the width of the rectangle: "))
            area = length * width
            print("The area of the rectangle is", area)
            repeat = input("Do you want to try again with rectangle? (yes/no): ")
            if repeat.lower() == "no":
                break

    elif choice == 3:
        while True:
            radius = float(input("Enter the radius of the circle: "))
            area = (22 / 7) * (radius ** 2)
            print("The area of the circle is", area)
            repeat = input("Do you want to try again with circle? (yes/no): ")
            if repeat.lower() == "no":
                break

    elif choice == 4:
        while True:
            base = float(input("Enter the base of the triangle: "))
            height = float(input("Enter the height of the triangle: "))
            area = 0.5 * base * height
            print("The area of the triangle is", area)
            repeat = input("Do you want to try again with triangle? (yes/no): ")
            if repeat.lower() == "no":
                break

    else:
        print("Invalid choice. Please enter a number between 1-4.")
