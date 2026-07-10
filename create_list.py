#  CREATE LIST

#  create empty list
empty = []
print(empty)
print(type(empty))

#  create a list by adding items manually
letters = ["a", "b", "c"]
print(letters)
print(type(letters))

#  you can mix data types in the same list
mixed = [1, "b", True, None]
print(mixed)
print(type(mixed))


#  list(value) built-in function, output: list, converts an iterable(sequence) into a list
empty = list()
print(empty)

letters = list("Python")
print(letters)

numbers = list(range(5))
print(numbers)




#  Nested list(matrix)
matrix = [["a", "b", "c"], 
          ["d", "e", "f"]]
print(matrix)
print(type(matrix))

mixed_matrix = [["a", "b"], 
          [1, 2, 3],
          [True]]
print(mixed_matrix)
print(type(mixed_matrix))




#  How to create a list?
#  emprt list
#  manual creation
#  nested lists
#  create by convert
