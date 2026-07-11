#  UNPACKING

person = ["Maria", 29, "Data Engineer", "Spain"]
name = person[0]
age = person[1]
role = person[2]
country = person[3]
#  using only indexes makes code long and hard to extend

#  Unpacking: list of variables, seperated by commas
#  Rule: variable order must match the list values order

person = ["Maria", 29, "Data Engineer", "Spain"]
name, age, role, country = person
print(name)




#  Rest collector:  ASTERISK *
person = ["Maria", 29, "Data Engineer", "Spain"]
name, *details, country = person
print(name)
print(details)
print(country)


person = ["Maria", 29, "Data Engineer", "city", "Spain"]
name, *details = person
print(name)
print(details)


person = ["Maria", 29, "Data Engineer", "Spain"]
*details, country = person
print(details)
print(country)


person = ["Maria", 29, "Data Engineer", "city", "Spain"]
*details, city, country = person
print(details)
print(city)
print(country)




#  Unpacking rules:::
#  1.only one asterisk(*) is allowed in unpacking
#  2.number of variables must match the values exactly(if you're not using asterisk) - not less, not more
#  3.asterisk collect leftovers, and it's fine if there are none
#  4.you can unpack any sequence(lists, tuples, strings, etc)




# Skipping items,  underscore_  :::
person = ["Maria", 29, "Data Engineer", "Spain"]
name, _, role, _ = person
print(name)
print(role)


person = ["Maria", 29, "Data Engineer", "Spain"]
name, *_, country = person
print(name)
print(country)







