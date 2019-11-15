# Given a number, write a function to output its reverse digits. (e.g. given 123 the answer is 321)
# Numbers should preserve their sign; i.e. a negative number should still be negative when reversed.

def reverse_number(n):
  if n > 0:
    n = str(n)
    reverse_str = n[::-1]
    return int(reverse_str)
  else:
    n = n * -1
    n = str(n)
    reverse_str = n[::-1]
    return int(reverse_str) * -1

# Write a function that takes an array of strings as an argument and returns a sorted array containing the same strings, ordered from shortest to longest.
# For example, if this array were passed as an argument:
# ["Telescopes", "Glasses", "Eyes", "Monocles"]
# Your function would return the following array:
# ["Eyes", "Glasses", "Monocles", "Telescopes"]
def sort_by_length(arr):
 arr.sort(key = len)
 return arr
 
sort_by_length(['hello', 'glasses', 'eye', 'word', ''])

# Write a function named sumDigits which takes a number as input and returns the sum of the absolute value of each of the number's decimal digits.
def sumDigits(number):
  li = []
  if number < 0:
    number = number * -1
    my_list = list(str(number))
    for value in my_list:
      li.append(int(value))
  else:
    my_list = list(str(number))
    for value in my_list:
      li.append(int(value))

  return(sum(li))

# Given two numbers and an arithmetic operator (the name of it, as a string), return the result of the two numbers having that operator used on them.
# a and b will both be positive integers, and a will always be the first number in the operation, and b always the second.
# The four operators are "add", "subtract", "divide", "multiply".

  def arithmetic(a, b, operator):
  if operator == 'add':
    return a + b
  elif operator == 'subtract':
    return a - b 
  elif operator == 'multiply':
    return a * b
  elif operator == 'divide':
    return a / b
  else:
    return("operator not valid")