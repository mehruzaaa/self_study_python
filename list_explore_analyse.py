#  HOW TO EXPLORE AND ANALYZE LISTS

#  max()  function, output: list item, find tyhe highest
numbers = [1, 5, 2, 4, 3]
print("Max:", max(numbers))

#  min()  function, output: list item, find the lowest value
numbers = [1, 5, 2, 4, 3]
print("Min:", min(numbers))

#  sum()  function, output: number, finds the total by summing all values
numbers = [1, 5, 2, 4, 3]
print("Sum:", sum(numbers))

#  len()  function, output: number, finds the length of a list(number of items)
numbers = [1, 5, 2, 4, 3]
print("Length:", len(numbers))

#  all()  function, output: True/False, returns True if all values are True
numbers = [1, 5, 2, 4, 3]
print("All:", all(numbers))
print("All:", all(["a", "", "b"]))

#  any
numbers = [1, 5, 2, 4, 3]
print("Any:", any(numbers))
print("Any:", any(["a", "", "b"]))
print("Any:", any([0, 0, 0]))


#  .count()  returns how many timees a value appears in the list
numbers = [1, 5, 5, 2, 4, 3]
print("Count:", numbers.count(5))

#  .index()  returns the position of the first occurence of a value
numbers = [1, 5, 5, 2, 4, 3]
print("Index:", numbers.index(5))      #  .index() returns the position of the first occurence


#  in,  operator, output: True/False,  checks if a value exists in a sequence
numbers = [1, 5, 5, 4, 3]
print(4 in numbers)
print(8 not in numbers)

list1 = [1, 2, 3, 4]
list2 = [1, 2, 3]
print(list1 == list2)

#  the first elements are compared, if they're equal, Python moves to the next element
list1 = [1, 2, 3]
list2 = [5, 2, 3]
print(list1 < list2)

#  is
list1 = [5, 8, 3]
list2 = [5, 8, 3]
print(list1 is list2)

