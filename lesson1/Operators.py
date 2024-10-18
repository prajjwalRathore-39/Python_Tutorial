# Operators are used to perform operations on variables and values.
# Python divides the operators in the following groups:

# Arithmetic operators
# Assignment operators
# Comparison operators
# Logical operators
# Identity operators
# Membership operators
# Bitwise operators


#Arithmatic Operators

print(4+5)
print(4-5)
print(4*5)
print(4/5)
print(4//5)
print(4**5)

print("_____________________________________________________________________________________")

print("_____________________________________________________________________________________")

#Comparision Operators

print("COMPARISION STATEMENTS")
print("Greater than, 5>3, : ", 5>3)
print("Smaller than, 3<5, : ", 3<5)
print("Equals to , 3==5, : ", 3==5)
print("Greater than Equals to, 5>=5, : ", 5>=5)
print("Smaller than Equals to , 4<=4, : ",4<=4)

print("_____________________________________________________________________________________")

print("_____________________________________________________________________________________")

# Logcal Operaetors

print("LOGICAL OPERATORS")
print("and operator (5>3)and(3<6): ", (5>3)and(3<6) )
print("or operator : (5>3)or(3<6) : ", (5>3)or(3<6) )
print("not operator: not ((5>3)or(3<6)) : ",not ((5>3)or(3<6)))

print("_____________________________________________________________________________________")

print("_____________________________________________________________________________________")


#Membership Operators

print("MEMBERSHIP OPERATORS")
x = ["apple", "banana"]

print(x)
print('''"banana" in x : ''',"banana" in x)
print('''"banana" not in x : ''',"banana" not in x)

print("_____________________________________________________________________________________")

print("_____________________________________________________________________________________")

#Identity Operators

print("IDENTITY OPERATORS")

x = ["apple", "banana"]
y = ["apple", "banana"]
z = x


print("",x)
print(y)
print(z)
print("x is z : ",x is z)

# returns True because z is the same object as x

print("x is y : ",x is y)

# returns False because x is not the same object as y, even if they have the same content

print("x == y : ",x == y)

# to demonstrate the difference betweeen "is" and "==": this comparison returns True because x is equal to y