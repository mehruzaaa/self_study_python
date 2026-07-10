#  IN LINE IF (TERNARY)
score = 100
if score >= 90:
    print("A")
else:
    print("F")

print("A" if score >= 90 else "F")


score = 85
if score >= 90:
    print("A")
elif score >= 80:
    print("B")
else:
    print("F")

grade = "A" if score >= 90 else "B" if score >= 80 else "F"
print(grade)




#  Match case:::
#  Evaluate a value against multiple values, runs the code of the first match

country = "India"
if country == "United States":
    print("US")
elif country == "India":
    print("IN")
elif country == "Egypt":
    print("EG")
else:
    print("Unknown Country")

#  can be only used for matching values
match country:
    case "United states":
        print("US")
    case "India":
        print("IN")
    case "Egypt":
        print("EG")
    case _:
        print("Unknown ountry")




#  Conditional statements summary:::
#  if - starts the first condition
#  elif - adds a follow-up condition if the previous is false
#  else - "fallback" if none of the conditions are met

#  standalone if statement:: used for just checking, if this is true, do this, otherwise do nothing
#  if-else statement:: this or that
#  if-elif-else statement:: branching, choose one from many
#  nested if:: layered tree, step-by-step decisions
#  independent if statements:: checklist mode, test all conditions
#  in-line if statement:: quick, short, simple check
#  case-match:: pattern matcher, match one exact value to multiple options

