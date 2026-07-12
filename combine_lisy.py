#  HOW TO COMBINE LISTS IN PYTHON?

letters = ["a", "b", "c"]
numbers = [1, 2, 3]
comb = letters + numbers
print(comb)

#  * multiplier operator makes multiple copies of the same list.
print(letters * 2)

#  nested list
letters = ["a", "b", "c"]
numbers = [1, 2, 3]
comb = [letters, numbers]
print(comb)

# .extend() method    it doesn't create a new list, it expands the original one
letters = ["a", "b", "c"]
numbers = [1, 2, 3]
numbers.extend(letters)
print(letters)
print(numbers)




#  Combinign using zip():::
letters = ["a", "b", "c"]
numbers = [1, 2, 3]
comb = list(zip(letters, numbers))
print(comb)

#  you can pair with strings too
letters = ["a", "b", "c"]
numbers = [1, 2, 3]
comb = list(zip(letters, numbers, "Hi"))
print(comb)


#  Task::
#  pair customers with their IDs(rebuild the relationship)
ids = [101, 102, 103]
names = ["Ali", "Sara", "John"]
print(list(zip(ids, names)))







