#write a program to find a sum of al even numbers up to 50
sum=0
for i in range(1,51):
    if i% 2==0:
        sum+=i


    print("the sum of all the even number up to 50 is",sum)
    #write a program to write first 20 numbers and their
    #squared numbers.
    for i in range (1,21):
        print (i,i**2)
   # write a program to check if a number is divisible by
   #8 and 12,up to 100 number
   #for i in range (1,100):

           #write a program to create a billing system at supermarket

        while True:
            name = input("Enter customer's name: ")
            total = 0

            while True:
                print("Enter the amount and quantity")
                amount = float(input("Enter amount: "))
                quantity = float(input("Enter quantity: "))
                total += amount * quantity

                repeat = input('Do you want to add more items? (yes/no): ')
                if repeat.lower() == "no":
                    break

            print("-" * 40)
            print("Name:", name)
            print("Amount to be paid:", total)
            print("-" * 40)
            print("******* Happy Shopping! *******")

            repeat = input("Do you want to go to the next customer? (yes/no): ")
            if repeat.lower() == "no":
                break
