#  ACCES LIST

lst = ["a", "b", "c", "d"]
print(lst)

#  get the first item from the list
lst = ["a", "b", "c", "d"]
print(lst[0])

#  get the last item from the list
#  use negative ixdexes to acces items from the end of a list
lst = ["a", "b", "c", "d"]
print(lst[-1])

#  get the "c" from the list
lst = ["a", "b", "c", "d"]
print(lst[-2])




#  Acces and read   nested list(matrix):::

matrix = [
    ["a", "b", "c"],  # row 0
    ["d", "e", "f"],  # row 1
    ["g", "h", "i"]  # row 2
]
#  get the whole matrix
print(matrix)

#  get the last row of the matrix
print(matrix[2])
print(matrix[-1])

#  get the last item of the last row
print(matrix[-1][2])
print(matrix[-1][-1])

#  get the first item of the first row
print(matrix[0][0])

# get the "e"
print(matrix[1][1])





#  Slicing:::

#  get the first two items from the list
lst = ["a", "b", "c", "d"]
print(lst[:2])

#  get the last two items from the list
lst = ["a", "b", "c", "d"]
print(lst[2:])



#  Slicing matrix

matrix = [
    ["a", "b", "c"],  # row 0
    ["d", "e", "f"],  # row 1
    ["g", "h", "i"]  # row 2
]
#  get the first two rows(lists) from a list
print(matrix[:2])

#  get the last two rows(lists) from a list
print(matrix[1:])

#  get items from a specific row
print(matrix[2][:2])





