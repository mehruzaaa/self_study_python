#  BREAK, CONTINUE, PASS
#  Break statement:::
#  it stops the loop immediately, jumps out and ends the loop right away

names = ['john', 'maria', '', 'kumar']
for name in names:
    if name == '':
        print("Empty value detected!")
        break
    print(f"Name = {name}")




#  Continue statement:::
#  it skips one loop cycle without stopping the loop,  skip this one and go next

names = ['john', 'maria', '', 'kumar']
for name in names:
    if name == '':
        print("Empty value detected!")
        continue
    print(f"Name = {name}")
#  use continue to skip bad or empty data without stopping the whole loop




#  Pass statement:::
#  it is like a place holder where nothing happens, for now.. just keep going, do nothing

names = ['john', 'maria', '', 'kumar']
for name in names:
    if name == '':
        pass # todo: handle the empty value
    print(f"Name = {name}")

names = ['john', 'maria', '', 'kumar']
for name in names:
    if name == '':
        name = name.replace('', 'unknown')
    print(f"Name = {name}")




#  Break vs continue    real-world applications:::
 
# skip weekens in calendar loop
days = ['Mon', 'Sun', 'Wed', 'Tue']
for day in days:
    if day in ['Sat', 'Sun']:
        continue
    print(f"Workday: {day}")

# avoid hardcoding values inside for or if. instead, define them as variables
days = ['Mon', 'Sun', 'Wed', 'Tue']
weekends = ['Sat', 'Sun']
for day in days:
    if day in weekends:
        continue
    print(f"Workday: {day}")


# checking for sql injection:
emails = [
    "data@gmail.com", 
    "baraa@outlook.de",
    "DROP TABLE USERS;",
    "maria@gmail.com"
]
for email in emails:
    if ";" in email:
        print("SQL Injection: Hacker Attack!")
        break
    print(f"Processing Email: {email}")




#  Comparison    break vs cintinue vs pass:::


