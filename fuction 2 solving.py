a = "hello"
b = "Hello123"
c = "123456"
d = "HELLO"
e = " "
f = "Hello 123"
g = "1.234"




#isalnum - Returns true if all characters in the string are alphanumeric
print(a,a.isalnum())
print(b,b.isalnum())
print(c,c.isalpha())
print(f,f.isalnum())
print(g,g.isalnum())

#isalpha -Return True if all characters in the string are in the alphabet
print(a,a.isalpha())
print(b,b.isalpha())


#isdecimal - REturns True if all characters in the string are decimals
print(a,a.isdecimal())
print(b,b.isdecimal())
print(c,c.isdecimal())


#isdigit - Returns True if all characters in the string are digits
print(g,g.isdigit())
print(c,c.isdigit())
print(b,b.isdigit())

#isnumeric - Returns True if all characters in the string are numeric
print(b,b.isnumeric())
print(c,c.isnumeric())
print(e,e.isnumeric())

#islower - Converts a string into lower case
print(a,a.islower())
print(d,d.islower())
print(b,b.islower())

#isuuper - Returns True if all characters in the string are upper case
print(a,a.isupper())
print(b,b.isupper())
print(d,d.isupper())

#isspace -  Returns True if all characters in the string are whitespaces

print(e,e.isspace())
print(f,f.isspace())

#istitle - Returns True if the string foolows the rules of atitle
print(d,d.istitle())
print(f,f.istitle())
