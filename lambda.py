#  PYTHON LAMBDA FUNCTIONS

#  variable (multiple) - stores a lambda function which doubles as a number
multiple = lambda x: x*2
print(multiple(2))

#  when a lambda has two parameters, you must pass two values when calling it
add = lambda x, y: x + y
print(add(1, 2))

#  my turn):::
smth = lambda m: m + 18
print(smth(2))
nice = lambda y: y / 2
print(nice(8))


#  a lambda can contain any expression, including conditions
check = lambda i: i in "python"
print(check("n"))




#  lambda + map
#  prices are stored as messy strings and need cleaning to floats
prices = ["$12.50", "9.99", "$100.00"]
print(list(map(lambda p: float(p.replace("$", "")), prices)))




#  lambda + filter
#  remove all prices lower than 100
prices = [120, 30, 300, 80]
print(list(filter(lambda p: p >= 100, prices)))

#  matrix iteration happens one row at a time
students = [["Maria", 85],
            ["Kumar", 90],
            ["Max", 60]]
print(list(filter(lambda row: row[1] > 70, students)))



#  CHALLENGE::
students = [["Maria", 85],
            ["Kumar", 90],
            ["Max", 60]]
print(list(filter(lambda row: row[0].startswith("M"), students)))



#  SUMMARY:
#  1. create quick and custom logic
#  2. one-line function
#  3. assist others
#  4. add dynamic and flexibility




