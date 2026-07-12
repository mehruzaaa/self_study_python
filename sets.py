#  PYTHON SETS
#  unordered collection of unique values

my_set = {10, 30, 20, 10}
print(my_set)   # unordered   # no duplicated are allowed
#  the set in not indexed!
my_set.remove(20)
print(my_set)  # mutable




#  Set methods:::

#  index-based methods do not work with sets

#  add() - inserts the item somewhere in the set, but onlt if it is new
a = {10, 20, 30, 40}
a.add(50)
print(a)


#  update() - merges another group of values (iterable) into new ser
a.update("Hi")
print(a)

#  you can use math operators as quick shortcuts: |&-^
#  |=   works like update for sets
a |= {1, 2}
print(a)


#  How to remove values from set
a.remove(10)
print(a)
#  remove throws an error if the value is missing


#  discard()   removes the item if it exists and does nothing if it does not
a.discard(100)
print(a)
#  pop()  removes and returns a random item from a set




#  Set math methods:::
a = {10, 20, 30, 40}
b = {30, 40, 50, 60}

#  union()   combines all unique items from both sets
print(a.union(b))
print(a | b)
#  math operators return a new set and leave the originals untouched


#  intersection()  retirns only the shared items
print(a.intersection(b))
print(a & b)

#  difference()  returns items in a, but not in b
print(a.difference(b))
print(a - b)


#  find non-shared values
print(a.symmetric_difference(b))




#  Set relationship methods

#  issubset()   returns true if all items in this set exist in the order
print(a.issubset(b))

#  issuperset()  returns true when it includes all items of the other set
print(b.issuperset(a))


#  isdisjoint()   returns true if both sets share no items(no overlapping)
print(a.isdisjoint(b))

