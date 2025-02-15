a = "Harry Potter and the Goblet of fire"
print(a)
#to find the length of thr string
print(len(a))

# to find the number of times  a character is occuring
print(a.count('H'))

# to convert each letter into upper case
print(a.upper())

#to convert each letter into lower case
print(a.lower())

##to find the index of any character
print(a.index("o",15,34))

#to convert the first letter to capital
print(a.capitalize())

#to convert a string into lower case
print (a.casefold())

#to find the index number of acharacter
print(a.find("o",15,34))

#to write variables inside a string
name ="John"
age = 24
b = "my name is {}"
print(b.format(name,age))
#it fills the given characters and centralizes a string
print(name.center(20,"*"))




