#  WHILE LOOP
#  repeats a block of code - over and over as long as condition is True

#  While condition:::

count = 1   # initialization
while count <= 5:  #condition
    print(count)
    count += 1    #update

count = 1   # initialization
while count <= 10:  #condition
    print(count)
    count += 2    #update


answer = ""
while answer != "yes":
    answer = input("Do you agree?(yes/no): ")
print("Thank you")




#  While True:::
#  only run the following statement if you have a powerful PC and you've saved all your work

while answer != "yes":
    answer = input("Do you agree?(yes/no): ")
    if answer == "yes":
        break
print("Thank you")


#  CHALLENGE:
#  if you know how many times to loop use while condition - not while True

attempts = 0
while attempts < 3:
    answer = input("Do you agree? (yes/no): ")
    if answer == "yes":
        print("Glad we're on the same page")
        break 
    attempts += 1
else:
    print("3 strikes. You're out!")




#  While condition vs True?:::
