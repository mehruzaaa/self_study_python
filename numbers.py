#  NUMBERS
#  Types:::
x = 5
y = 5.7
z = 2 + 3j
print(type(x))
print(type(y))
print(type(z))

x = "24"
print(type(x))
print(x * 3)

#  int(value) built-in function, output: int, converts compatible value into int value
x = int(x)
print(type(x))
print(x * 3)
x = 3.14
print(int(x))

#  float(value) built-in function, output: float, converts compatible value into float value
x = 3
print(float(x))
x = "3.14"
print(float(x))

#  complex(real, imag) built-in function, output: complex, creates a complex number using real and imaginary parts
x = 3 #real
y = 4 #imaginary
print(complex(x,y))




#  Math operators:::
print(2 + 3)
print(5 - 3)
print(4 * 2)
print(7 / 2)
print(7 // 2)  #  // floor division, output: int, divides two numbers and rounds down
print(7 % 2)   #  %  remainder, output: 0 or 1, the leftover part after division - used to check if a number is even
print(2 ** 3)  #  ** exponentiation, it raises a number to the power of another number

#  <operator>=   shorthand assignment, apply an operator and reassign the result in one step
x = 2
x += 3
print(x)
x -= 1
print(x)




import math
#  Rounding:::
#  abs(value) built-in function, output: int, returns the absolute(non-negative) value of a number
print(abs(2-10))

price = 35.54879865
print(round(price))

#  floor() is not a built-in function, fllor() belongs to the math module - import it before using
print(math.floor(price))
print(math.ceil(price))

#  round(number, ndigits), rounds the number to the specified number of decimal places
print(round(price, 2))

#  math.trunc(x) - cuts off the decimall part and keeps the whole number (no rounding)
#  int() vs trunc()   if you're not using math already, just use int() it's simple and built-in; if you've already imported math, use trunc() it makes your intent clearer
print(math.trunc(price))
print(int(price))

#  when to use which?
#  round()  handy in data analysis to clean up numbers for reports or save space
#  ceil()  perfect for data engineering - like splitting data into pages or batches




import random
#  Random:::
#  random() random function, output: float, returns a random float between 0.0 and 1.0
print(random.random())

#  randint(start, end) random function, output: int, gets a random whole number from start to end (both included)
print(random.randint(1,6))




# Validation:::
#  is_integer()  float class method, output: bool, checks if a float has no decimals parts(is a whole number)
x = 7.0
print(x.is_integer())

#  isinstance(value, type) built-in function, output: bool, checks if a value belongs to a certain data type
x = 70
print(isinstance(x, int))


#  CHALLENGE
number = random.randint(1, 100)
print(number)
result  = (random.randint(1, 100) % 2 == 0)
print(result)