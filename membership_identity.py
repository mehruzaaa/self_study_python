#  MEMBERSHIP OPERATORS
#  membership (in) operator checks if value inside another value, like a string, list, tuple, or other sequence
print("o" in "python")
print("f" not in "python")
print(3 in [1, 2, 3])
print(3 not in [1, 2, 3])

 
#  security check: ensure the domain is not banned
domain = "gmail.com"
banned_domains = ["spam.com", "fake.org", "bot.net"]
print(domain not in banned_domains)




#  IDENTITY OPERATORS
#  identity (is) operator checks if two variables refer to the same object in memory
x = ['a', 'b', 'c']
y = ['a', 'b', 'c']
print(x == y)
print(x is y)

x = 10
y = 10
print(x == y)
print(x is y)

#  = between two variables assigns one variable to the same object that another variable is referring to
x = ['a', 'b', 'c']
y = x
print(x == y)
print(x is y)


#  Make sure the email exists, and it's not empty.
email = None
print(email != None and email != "")

#  use is instead of == when checking for None
email = None
print(email is not None and email != "")




