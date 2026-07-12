#  ITERATOR VS ITERABLE
#  Why we need iterator?
#  A: 1. for loops
#     2. to save memory
#     3. for speed and flexibility

letters = ["a", "b", "c"]
for l in letters:
    print(l)

#  we use iteration to transform data
letters = ["a", "b", "c"]
new_list = []
for l in letters:
    new_list.append(l.upper())
    print(new_list)




#  ITERATORS: enumerate, reversed, zip

#  enumerate
letters = ["a", "b", "c"]
print(list(enumerate(letters)))

# you can choose which index to start
letters = ["a", "b", "c"]
print(list(enumerate(letters, start = 1)))


letters = ["a", "b", "c"]
for index, value in enumerate(letters):
    print(index, value)


#  enumerate use case - find the exact position of the bad data in your list




#  reversed - returns an iterator that flips the data order
letters = ["a", "b", "c"]
print(list(reversed(letters)))

letters = ["a", "b", "c"]
for l in reversed(letters):
    print(l)




#  zip - combines two or more sequencees into pairs(tuples)
letters = ["a", "b", "c"]
numbers = [1, 2, 3]
print(list(zip(letters, numbers)))


letters = ["a", "b", "c"]
numbers = [1, 2, 3]
for l, n in zip(letters, numbers):
    print(l, n)




#  iterator map:::
#  make every letter uppercase
letters = ["a", "b", "c"]
print(list(map(str.upper, letters)))

#  convert list items to integers
numbers = ["1", "2", "3"]
print(list(map(int, numbers)))


#  clean up the list by removing all unwanted spaces
names = [" Maria ", "John ", " Kumar"]
print(list(map(str.strip, names)))

#  map is fast, clean wy to do data transformations
names = [" Maria ", "John ", " Kumar"]
for n in map(str.strip, names):
    print(n)




#  iterator filter:::
#  clean up the list by removing unvalid data
letters = ["a", "", "b", None, "c", False]
#  None removes all falsy values like 0, "", or False
#  bool can be used too!
print(list(filter(None, letters)))


#  keep only letters(alphabetic) items
items = ["sql", "123", "python", "42"]
print(list(filter(str.isalpha, items)))


#  filter() is perfect for cleaning up data structures
items = ["sql", "123", "python", "42"]
for i in filter(str.isalpha, items):
    print(i)




