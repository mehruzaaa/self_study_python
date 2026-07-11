#  HOW TO COPY PYTHON LISTS SAFELY

#  Copying list, assignement = 
#  create a copy of the list in a new variable
letters = ["a", "b", "c"]
letters_copy = letters
print("Original:", letters)
print("Copy:", letters_copy)

# both variables reference the same list in memory
letters = ["a", "b", "c"]
letters_copy = letters
letters.pop()
letters_copy.append("z")
print("Original:", letters)
print("Copy:", letters_copy)




#  Copying list,  shallow copy:::
#  copy() creates a separate list in memory
letters = ["a", "b", "c"]
letters_copy = letters.copy()
letters.pop()
letters_copy.append("z")
print("Original:", letters)
print("Copy:", letters_copy)




#  Copying list,  deep copy:::
matrix = [
    ["a", "b"],   # row 0
    ["c", "d"]    # row 1
]
matrix_copy = matrix.copy()
matrix.pop()
print("Original:", matrix)
print("Copy:    ", matrix_copy)

# the copy() method creates a shallow copy
matrix = [
    ["a", "b"],   # row 0
    ["c", "d"]    # row 1
]
matrix_copy = matrix.copy()
matrix.pop()
matrix_copy[0].append("z")
print("Original:", matrix)
print("Copy:    ", matrix_copy)




import copy
#  copy.deepcopy() creates a true, independent copy for all level
matrix = [
    ["a", "b"],   # row 0
    ["c", "d"]    # row 1
]
matrix_copy = copy.deepcopy(matrix)
matrix.pop()
matrix_copy[0].append("z")
print("Original:", matrix)
print("Copy:    ", matrix_copy)

#  copy.copy() creates a shallow copy just like the method copy()
matrix = [
    ["a", "b"],   # row 0
    ["c", "d"]    # row 1
]
matrix_copy = copy.copy(matrix)
matrix.pop()
matrix_copy[0].append("z")
print("Original:", matrix)
print("Copy:    ", matrix_copy)




#  Testing  is operator:::
#  is operator checks if two vaariables refer to the same object
import copy
original = [
    ["a", "b"],   # row 0
    ["c", "d"]    # row 1
]
#  Assigment
copy1 = original
print("Same object?", original is copy1, "\n")

#  shallow copy
copy2 = original.copy()
print("Same object?", original is copy2, "\n")
print("Shared Lists?", original[0] is copy2[0], "\n")

#  deep copy
copy3 = copy.deepcopy(original)
print("Same object?", original is copy3, "\n")
print("Shared Lists?", original[0] is copy3[0], "\n")

#  use the is operator to check if the copies are truly independent



