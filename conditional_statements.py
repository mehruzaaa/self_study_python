#  CONDITIONAL STATEMENTS
#  Checkpoint that checks a conddition
#  -True? runs the code
#  =False? skip it


#  if statement  standalone
#  defines the first condition, if it's true, do this, therwise, do nothing
#  if rules: 
#  1. only one if
#  2. starts with if
#  3. required
#  4. can standalone

score = 100
if score >= 90:
    print("A")
#  indentation: adding spaces at the beginning of a line to show that the line belongs to a code block




#  if-else  two way decision
#  else statement runs only if all previous conditions are false, if nothing was true, do this instead
#  else rules:
#  1.comes at the end
#  2. no conditions
#  3. optional
#  4. cannot standalone

score = 50
if score >= 90:
    print("A")
else:
    print("F")
#  else cannot be used on its own  # else doees not need a condition




#  elif statement asks a follow-up question, only runs if previous conditions were false, if the first wasn't true, try this one
#  elif rules: 
#  1. comes after if
#  2. multiple elif
#  3. needs condition
#  4. optional
#  5. cannot standalone

score = 85
if score >= 90:
    print("A")
elif score >= 80:
    print("B")
else:
    print("F")




#  branching  if-elif-elif-else

score = 75
if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
else:
    print("F")




#  Nesting   if-else
#  nested if: if statement inside another if, if the first is true, then check the second
#  python evaluates boolean conditions directly, avoid explicit comparisons ==True or ==False

score = 95
submitted_project = True
if score >= 90:
    if submitted_project:
        print("A+")
    else:
        print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
else:
    print("F")




#  Connecting conditions,  logical operators

score = 50
submitted_project = True
if score >= 90 and submitted_project:
        print("A+")
elif score >= 90:
        print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
elif score >= 60 or submitted_project:
    print("D")
else:
    print("F")




#  Independent  if-else
#  independent ifs, each if is checked seperately, all conditions are tested - even if one is already true

score = 50
submitted_project = False

if score >= 90:
    print("High score")
else:
    print("Low score")

if submitted_project:
    print("Project is submitted")
else:
    print("Project is not submitted")


# CHALLENGE:
# email = "mehruza@gmail.com"
# print(email != "" and "." in email and "@" in email and email.endswith(".com" or ".org" or".net") and len(email) <= 254)


email = "mehruza@gmail.com"
#  clean the string
email = email.strip()
#  email must not be empty
if email == "":
    print("Email cannot be empty.")
#  email must contain a '.' and '@'
if not '.' in email and '@' in email:
    print("Email must contain . and @")
#  email must contain exactly one @ symbol
if email.count("@") != 1:
    print("Email must contain exactly one @.")
if not email.endswith('.com' or '.org' or '.net'):
    print("Email must end with .com, .org, .net")
#  email must not be longer than 254 characters
if len(email) > 254:
    print("Email must not be longer than 254 characters")
#  email must start and end with a letter or digit
if not (email[0].isalnum() and email[-1].isalnum()):
    print("Email must start and end with a letter or digit")
else:
    print("Email is valid.")

### ATTENTION!!!
#  isalnum()- checks if the string contains only letters and digits


#  CHALLENGE
password = "Mehruzaaa"
#  clean the strip
password = password.strip()
#  must not be empty
if password == "":
    print("Email must not be empty")
else:
    print("Password is valid")
if len(password) < 8:
    print("Password must be at least 8 characters")
else:
    print("Password is valid")










