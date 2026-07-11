#  HOW TO ADD, REMOVE AND UPDATE LISTS IN PYTHON

#  change your list,  add items

#  add "x" to the end of the list
letters = ["a", "b", "c"]
letters.append("x")
#  add "y" to the end of the list
letters.append("y")
print(letters)

#  add "x" to the start of the list
letters = ["a", "b", "c"]
letters.insert(0, "x")
#  add "y" between "b" and "c"
letters.insert(3, "y")
print(letters)


#  add new row to the end of matrix
matrix = [
    ["a", "b", "c"],   # row 0
    ["d", "e", "f"],   # row 1
    ["g", "h", "i"]    # row 2
]
matrix.append(["x", "y", "z"])
#  add new row at the start of the matrix
matrix.insert(0, ["a", "a", "a"])
print(matrix)


#  add "x" at the end of the second row
matrix = [
    ["a", "b", "c"],   # row 0
    ["d", "e", "f"],   # row 1
    ["g", "h", "i"]    # row 2
]
matrix[1].append("x")
#  add "z" at the start of the first row
matrix[0].insert(0, "z")
print(matrix)




#  Change your list, remove items
letters = ["a", "b", "c"]
letters.clear()
print(letters)

#  revome "a" from the list
letters = ["a", "b", "a"]
letters.remove("a")
print(letters)

#  remove the last item
letters = ["a", "b", "c"]
removed = letters.pop()
print(letters)
print("Removed Ittem:", removed)

#  remove the first item 
letters = ["a", "b", "c"]
removed = letters.pop(0)
print(letters)
print("Removed Ittem:", removed)




#  Removing from matrix
matrix = [
    ["a", "b", "c"],   # row 0
    ["d", "e", "f"],   # row 1
    ["g", "h", "i"]    # row 2
]
matrix.remove(["a", "b", "c"])
#  remove the last row
matrix.pop()
print(matrix)

#  remove "e" from the matrix
matrix = [
    ["a", "b", "c"],   # row 0
    ["d", "e", "f"],   # row 1
    ["g", "h", "i"]    # row 2
]
matrix[1].remove("e")
#  remove the first item from the last row
matrix[-1].pop(0)
#  remove the last item of the first list
matrix[0].pop()
print(matrix)




#  Change your data,  update items
#  update the first item to the value "x"
letters = ["a", "b", "c"]
letters[0] = "x"
#  update the second item to the value "y"
letters[1] = "y"
print(letters)



# practice with matrix
matrix = [
    ["a", "b", "c"],   # row 0
    ["d", "e", "f"],   # row 1
    ["g", "h", "i"]    # row 2
]
#  update the content of the last list
matrix[-1] = ["x", "y", "z"]
#  update the first item of the first row
matrix[0][0] = "-"
print(matrix)



