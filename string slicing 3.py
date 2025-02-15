#take an input from a user as a string then ,reverse it.
# a=input ("enter anything here:")
# print (a[::-1])
#write a program to check if a string contains only digits.
# a=input ("enter anything here:")
# print(a.isdigit())
 #write a program to heck if a string contains only digits.
# a=input ("enter anything here:")
# b=(a.isdigit())
# if b == True:
#     print ("it contains only digits")
# else:
#     print ("it does not contain only digits")
#
#    write a program to check if a string is palindrome.
a=input ("enter anything here:")
rev = a[::-1]

if a==rev:
    print ("it is palindrome")
else:
    print("it is not palindrome")