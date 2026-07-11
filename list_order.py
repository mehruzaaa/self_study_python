#  HOW TO ORDER LISTS IN PYTHON
#  sorting:::
#  sort the list in ascending order
letters = ["c", "a", "b"]
letters.sort()
print(letters)

letters = ["c", "a", "b"]
letters.sort(reverse = True)
print(letters)



#  sorts by the first item of each inner list
matrix = [
    ["d", "e", "f"],   
    ["g", "h", "i"],
    ["a", "b", "c"]   
]
matrix.sort()
print(matrix)



#  sort the data without changing the original list
letters = ["c", "a", "b"]
new_list = sorted(letters)
print("Original List:", letters)
print("Sorted List:", new_list)




#  Reversing list:::
letters = ["c", "a", "b"]
letters.reverse()
print(letters)

letters = ["c", "a", "b"]
new_list = list(reversed(letters))
print("Original List", letters)
print("Reversed List:", new_list)
#  reversed() creates an iterator object, not a list

