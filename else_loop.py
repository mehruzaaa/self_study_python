#  ELSE IN LOOP
#  runs a block of code only if the loop finishes naturally

items = [1, 3, 4, 7]
for i in items:
    print(i)
else:
    print("Loop is completed")
#  this else runs no matter what so why not just write it after the loop?
#  use else this loops only when there's a break




# Else + break:::
items = [1, 3, 4, 7]
for i in items:
    if i % 2 == 0:
        print("Even number found", i)
        break
else:
    print("All numbers are odd")
#  else will run only if the loop is not interrupted




#  Else in loops, real-world applications:::
names = ["Kamara", "Tuba", None, "Mounika"]
for name in names:
    if name is None:
        print("Found a missing name")
        break
else:
    print("All names are available")



files = ["data1.csv",
         "report.pdf",
         "report2.csv"]
for file in files:
    if not file.endswith(".csv"):
        print(f"{file} is not CSV")
        break
else:
    print("All files are CSV")
#  it makes no sense to use else+continue



# CHALLENGE:
files = [
    "report.csv",
    "data.xlsx",
    "summary.docx",
    "report.csv",
    "data.csv"
]
for file in files:
    if len(files) != len(set(files)):
        print("Duplicate found!")
else:
    print("All files are unique")






