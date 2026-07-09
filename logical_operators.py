#  LOGICAL OPERATORS
#  used to combine multiple boolean expressions
print(3 > 1 and 5 < 1)
print(3 > 1 or 5 < 1)

cpu_usage = 70
memory_usage = 95
print(cpu_usage > 90 or memory_usage > 90)

#  checking user credentials before login
email = True
password = False
print(email and password)

#  not
print(not 3 > 2)
print(not True)
print(not False)
print(not not False)

name = ""
print(not name)
print(not 0)


#  "and" has higher priority than "or"
is_logged_in = True
is_guest = False
is_banned = True
print((is_logged_in or is_guest) and not is_banned)


# CHALLENGE
username = "delicioso"
age = 19
print(username and age >= 18)

password = "12345678"
print(int(password) >= 8 and " " not in password)

email = "baby@gmail.com"
print("@" in email and email.endswith(".com"))

username = "delicioso"
print(isinstance(username, str) is not None and len(username) > 5)

admin = True
moderator = False
banned = False
verified = True
print((admin or moderator) and (banned or verified))



