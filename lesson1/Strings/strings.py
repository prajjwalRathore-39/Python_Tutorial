# Strings in python are surrounded by either single quotation marks, or double quotation marks.
# 'hello' is the same as "hello".

# You can display a string literal with the print() function:


print("Hello")
print('Hello')


# Quotes inside any String

print("It's alright")
print("He is called 'Johnny'")
print('He is called "Johnny"')


# Assign String to a variable

a = "Hello"
print(a)

# Multiline String 

# You can assign multiple line string using three quotes
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)



# Strings are Arrays

# Like many other popular programming languages, strings in Python are arrays of bytes representing unicode characters.

# However, Python does not have a character data type, a single character is simply a string with a length of 1.

# Square brackets can be used to access elements of the string.


a = "Hello, World!"
print(a[1])


# Looping through a String.

for x in "banana":
  print(x)


# String Length

a = "Hello, World!"
print(len(a))


# Check String

txt = "The best things in life are free!"
print("free" in txt)


txt = "The best things in life are free!"
print("expensive" not in txt)