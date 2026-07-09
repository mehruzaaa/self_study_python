#  BOOLEAN EXPRESSIONS
print(True)
print(False)
print(type(True))

#  bool(value) built-in function, output: boolean, 
#  True-> if the value in non-empty or non-zero
#  Fallse-> if the value id empty or zero
print(bool(123))
print(bool("Hi"))
print(bool())
print(bool(0))
print(bool(""))

#  None isn't empty - it's missing! None means no value. "" Empty means the value exists, but empty string
print(bool(None))


email = ""
phone = "0176-123456"
username = ""
print(any([email, phone, username]))
print(all([email, phone, username]))


#  isinstance(value, type) built-in function, output: bool, checks if a value belongs to a certain data type
print(isinstance(123, int))
print(isinstance(True, str))


#  endswith(substring) str method, output: bool, checks if the string ends with a specific word
print("Hello".endswith("o"))

