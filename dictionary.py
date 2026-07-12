my_dict = {
    "a": 10,
    "b": 20,
    "c": 30
}
print(my_dict)    # ordered
#  keys are unique,  but values allow duplicates
#  not indexed

#  you access values by using their keys, not indexes
print(my_dict["b"])

#  is mutable
my_dict["c"] = 80
print(my_dict)




#  dict methods:::
user  = {"id":1, "age":30, "city": "berlin"}
#  access
print(user["city"])
#  if the key is not found, Python throws a KeyError


#  .get()    returns the value safely, gives None if missing, you can also choose what to see in the output
user  = {"id":1, "age":30, "city": "berlin"}
print(user.get("name"))
print(user.get("name", "Unknown"))



#  checks
#  in operator checks if the key in inside the dictionary
print("age" in user)
print("name" not in user)



#  View objects,    give you a live view of the dictionary's keys, values, or key value pairs

#  keys()  returns all the KEYS in your dictionary
print(user.keys())

#  values()  returns all the VALUES in your dictionary
print(user.values())

#  items()  returns all (key, value)  pairs of your dictionary
print(user.items())

#  items() perfect when you need key and value together for looping, transforming data, building new dicts, comparing, and more
for u in user:
    print(u, user[u])

for key, value in user.items():
    print(key, value)



# add, remove, update
user["name"] = "John"  # add
print(user)

user["age"] = 35  # update
print(user)

#  assign key      updates the value if the key exists, or inserts a new key value pair if it doesn't


#  update()  adds keys and updates existing ones using another dictionary
user.update({"age": 40, "city": "Paris"})
print(user)


#  pop()  removes a keyy from the dictionary and returns its value
age = user.pop("age")
print(user)
print("Removed Item:", age)

#  if the key is not found, Python throws a KeyError
#  pop()  removes the key and returns its value, or returns your defauly if the key is missing
age = user.pop("salary", "Not Found")
print(user)
print("Removed Item:", age)


#  popitem()  returns and deletes the most recent key value pair from the dictionary
user.popitem()
print(user)



#  Creation
user = {"id": None,
        "name": None,
        "age": None,
        "city": None
        }
#  fromkeys()  builds a new dictionary where all keys get the same default value
user = dict.fromkeys(["id", "name", "age", "city"], None)
print(user)




# CHALLENGE::  keep only string values and convert them to uppercase
user = {"id": 1, "name": "John", "age": 30, "city": "Berlin"}

#  dict comprehensions 3 components: key value expression, a loop, and an optional condition
user_str = {
    k: v.upper()  # expression
    for k, v in user.items() # loop
    if isinstance(v, str)  # filter
}
print(user_str)




#  real world applications:::

# 1.use case: database or API records
#  returned records are stored as dictionaries where column names are keys and the row ralues are the dictionary values
row = {
    "id": "John",
    "country": "DE",
    "age": 29,
    "status": "active"
}

#  2.use case: mapping to friendly values
#  great for converting technical codes into friendly labels
status_map = {
    "01": "Open",
    "02": "In Progress",
    "03": "Done"
}

# 3.use case: mapping abbrevations
#  turning short abbrevations intoo full readable names
country_map = {
    "DE": "Germany",
    "Fr": "France",
    "IN": "India"
}

# 4.use case: config and environment data
#  store system settings like host, port, and usernames in one clean place
system_conn = {
    "DB_HOST": "prod-db.company.com",
    "DB_PORT": 5432,
    "DB_USER": "admin_user",
    "DB_NAME": "analytics_warehouse"
}

# 5.use case: ETL and Pipeline Settings
#  great for storing run parameters and controlling how your ETL pipeline loads data

# 6.use case: metadata
#  data about your data


