#  PYTHON DATA TYPES
#  no value: NoneType
#  single value(primitive data types): int, float, str, bool, complex
#  multi values(data structures/collections/containers): list, set, dict, tuple


a = 10 #int
b = 3.15 #float
c = "Hello" #str
d = 'Hi' #str
e = "1234" #str
f = True #bool
g = False #bool
h = None #NoneType
i = "" #str - blank
j = " " #str - Empty Space

#  int - whole numbers without decimals
#  float - numbers with decimal points
#  str - represent text or a sequence of characters wrotten inside single or double quotes
#  bool - can be either True or False, used to handle logic and decision making
#  True and False are case-sensitive; so they must start with a capital letter
#  None - means "no value", "nothing" or "unknown"; used to show the absence of any data
#  blank "" is a string value with no characters inside, it is not the same as None!
#  white space " " is a string value with 1 or more spaces, it is not same as None!


#  Value->Function->New value
#  1.Standalone functions: print(), type() and etc.
#  2.Methods of class: upper(), replace()
#  3. Operations: +, /, >, <, ==, in, or


#  Functions - independent block of code
#  syntax: function_name(value)| print("hello"), type(50)

#  Methods - functions belong to objects/classes
#  symtax: value.method_name()| "hello".upper(), 50.bit_length()

text = "hi"
number = 10
print(text)
print(number)

#  type() built-in function, returns the data type of a value, so you know what kind of object it is.
text = "hi"
number = 10
print(type(text))
print(type(number))

#  len() built-in function, gives you the totaal count of items inside a value, helping you measure its length
text = "hi"
number = 10
print(len(text))

#  upper() method of <class str>, converts all letters in a string to uppercase
print(text.upper())

#  bit_length() method of <class int>, returns the length of a number in binary.
print(number.bit_length())


# CHALLENGE
age = 19
height = 1.58
name = "Mehruza"
job = "student"
children = None

print(age)
print(height)
print(name)
print(job)
print(children)

print(type(age))
print(type(height))
print(type(name))
print(type(job))
print(type(children))

print(age.bit_length())
print(len(name))
print(len(job))

