#  LOOP
#  Contoll the flow of code, repeat a block of code over and over until a condition is met

#  for loop:::
#  go through a group of items one by one to do something for each item

#  python iterator - an object that lets you go thhrough items one by one in a sequence. remembers what's done. knows what's next

print("Round: 1")
print("Round: 2")
print("Round: 3")
print("Round: 4")
print("Round: 5")

for i in (1, 2, 3, 4, 5):
    print(f"Round: {i}")

#  use the same word, variable -> singular, sequence -> plural
items =  (1, 2, 3, 4, 5)
for item in items:
    print(f"Round: {item}")



#  for loops, sequences you can loop
#  list:
items =  (1, 2, 3, 4, "Hi")
for item in items:
    print(f"Round: {item}")


#  string:
items =  ("Python")
for item in items:
    print(f"Round: {item}")


#  range:
for item in range(10):      # default start is 0, doesn't include stop
    print(f"Round: {item}")

for item in range(1, 5):       # you choose the start, stop will not be included
    print(f"Round: {item}")

for item in range(1, 10, 2):       # you choose the start, stop will not be included, can skip numbers
    print(f"Round: {item}")


# tuple, file, dictionary can also be used as a sequence!




#  for loops real-world applications:::
#  we use for loops to go through values and aggregate data like summing, counting, or averaging

scores = [80, 50, 60, 75]
total = 0
for score in scores:
    total += score
    print("Current Total:", total)
print("Final Total:", total)


#  we use for loops to transform data like cleaning data before processing
files = [ ' Report.csv ', 'Data.cvs ', 'final.TXT']
for file in files:
    file = file.strip().lower().replace('.txt', '.csv')
    print(f"Processing {file}")
#  clean first, transform second - always in that order



#  CHALLENGE:
for i in range(1, 11):
    print(f"7 * {i} = {7 * i}")



for i in range(1, 7):
    print("*" * i)