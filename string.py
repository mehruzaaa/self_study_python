#  STRING
#  Types:::
#  type(value) built-in function, output:type, returns the data type of a value, so you know what kind of object it is
name = "Mehruza"
print(type(name))

age = 24
print(type(age))
print("Your Age is:" + str(age)) # can't combine a string with an integer using + operator
#  str(value) built-in function, output: string, converts any value into string value




#  Math:::
#  use case - check password quality, make sure the password meets minimum length requirements
password = "123a"
#  len(value) built-in function, output:int, returns the number of items in a value returns the number of characters in a string
print(len(password))

if len(password) < 8:
    print("Your Password is too short!")
#  len() counts everything even spaces
#  use case - validate input length, prevent values that are too short or too long


text = """
Python is easy to learn.
Python is powerful.
Many people love python.
"""
#  use case - word frequency check, counts how many times a specific word appear
#  count(substring) str method, output:int, returns how often a word appears in the string
print(text.count("Python"))
#  Python is case-sensitive, means uppercase and lowercase letters are treated as different
#  use case - detect quality issues, count how many unwanted characters in my data
text = """
Python is easy to learn.
Python is powerful$.
Many people love python.
"""
print(text.count("$"))




#  Transformations:::
#  replace(old, new) str method, output: string, swaps part of the text with something new
#  use case - replace commas with dots in European-style decimal numbers
price = "1234,56"
print(price.replace(",", "."))

#  use case - change phone number format, replace special characters with something else
phone = "176-1234-56"
print(phone.replace("-", "/"))

#  replace() is not just for changing values, you can also remove unwanted parts by replacing them with an empty string("")
phone = "176-1234-56"
print(phone.replace("-", ""))

#  use case - clean numeric formats, remove symbols and commas to prepare for numeric conversion
#  chained methods are executed in order from left to right. Each replace() runs onthe result of the one before it.
price = "$1,299.99"
print(price.replace("$", "").replace(",", ""))

#  CHALLENGE
#  "+49 (176) 123-4567" -> 00491761234567
number = "+49 (176) 123-4567"
print(number.replace("+", "00").replace(" ", "").replace("(", "").replace(")", "").replace("-", ""))


#  'string' + 'string'  operator, output: string, joins(concatinates) two strings into one.
first_name = "Micheal"
last_name = "Scott"
last_name = first_name + " " +  last_name
print(last_name)

#  use case - build file paths, build dynamic paths using folder and file variables
folder = "C:/Users/Baraa/"
file = "reports.cvs"
full_file_path = folder + file
print(full_file_path)


#  f-string  - modern, super-easy way to format and build strings, "f" stands for "formatted", lets you easily put variables and expressions directly inside string value
#  e.g. print(f"My name is {name} and I am {age} years old.")
name = "Sam"
age = 34
is_student = False
print("My name is " + name + ", I am " + str(age) + " years old, and student status is " + str(is_student) + ".")
print(f"My name is {name}, I am {age} years old, and student status is {is_student}.")

print(f"2 + 3 = {2 + 3}")

print(f"{{This is me}}")


#  split(seperator) str method, output: list of strings, breaks a string into smaller parts
stamp = "2026-09-20 14:30"
print(stamp.split(" "))

stamp = "2026-09-20"
print(stamp.split("-"))

cvs_file = "1234,Max,USA,1970-10-05,M"
print(cvs_file.split(","))


#  'string' * number   operator, output:string, repeats the string multiple times
print("ha" * 3)
#  use case - style your logs, use repeated characters to create clear sections in output
print("#" * 30)
print("=" * 30)




#  Extraction:::
#  'string'[index]  operator, output: string, Indexing: extracts one chaaracter by position
text = "Python"
#  extract the first character
print(text[0])
print(text[-6])

#  extract the last character
print(text[5])
print(text[-1])

#  extract h
print(text[3])
print(text[-3])


# 'string'[start:end:step]  operator, output: string, slicing extracts a part of the string
date = "2026-09-20"
#  extract the date
print(date[0:4])
#  open-ended slicing   if you leave the start index empty, Python starts from index 0
print(date[:4])

#  extract the month
print(date[5:7])

#  extract the day
print(date[8:])
print(date[-2:])




#  Data cleaning:::
#  whitespace cleanup
#  lstrip() str method, output:string, removes spaces from the left side of a string
text = " Engineering".lstrip()
print(text)

#  rstrip() str method, output: string, removes spaces from the right side of a string
text = "Engineering ".rstrip()
print(text)

#  strip() str method, output: string, removes spaces from both ends
text = " Engineering ".strip()
print(text)

#  best practise - trim spaces from user input, you never know where users might add spaces use  .strip() to remove all extra spaces from both ends
#  strip() does not remoove spaces in the middle!

#  it removes any characters you want from start to end - not just spaces
text = "###Abc###".strip("#")
print(text)

# use case - detect extra spaces, check the length before and affter strip() to find unwanted spaces
text = "  Engineering"
print(len(text))
print(len(text.strip()))

nr_of_spaces = len(text) - len(text.strip())
is_clean = len(text) == len(text.strip())
print("Nr of spaces:", nr_of_spaces)
print("Is my data clean?", is_clean)


#  case conversions
text = "python PROGRAMMING"
#  lower() str method, output: string, makes all letters lowercase
print(text.lower())

#  upper() str method, output: string, makes all letters uppercase
print(text.upper())

#  use case - clean data for matching, lowercase all text to prevent case-based mismatches during search or comparison
search = "Email".lower()
data = "email".lower()
print(search == data)

#  best practice - clean beforee search, always trimm spaces and lowercase your data and search term before matching
search = "Email ".lower().strip()
data = " email".lower().strip()
print(search == data)


#  CHALLENGE 
text = "968-Maria, (D@t@ Engineer );; 27y  "
print(text.lower().replace("968-", "name: ").replace(",", "").replace("(", " | role: ").replace("@", "a"). replace(");; ", " | age: "). replace("y  ", ""))




#  Searching:::
#  startswith(substring) str method, output: boolean, checks if the string begins with a specific word
phone = "+49-176-12345"
print(phone.startswith("+49"))

#  endswith(substring) str method, output: boolean, checks if the string ends with a specific word
email = "baraa@gmail.com"
print(email.endswith("gmail.com"))

#  'substring' in 'string'  operator, output: int, checks if a word exists in the string
print("@" in email)

#  find() is great when combined with other methods to add dynamics
#  find(substring) str method, output: number, returns the starting position of a word in the string
phone1 = "+48-176-12345"
phone2 = "48-654-16548"
print(phone1[4:])
print(phone2[3:])

print(phone1[phone1.find("-")+1:])
print(phone2[phone2.find("-")+1:])




#  Validation:::
#  isalpha() str method, output: boolean, checks if the string has only letters
country = "USA"
print(country.isalpha())

#  isnumeric() str method, output: boolean, checks if the string has only numbers
phone = "01761234587"
print(phone.isnumeric())




