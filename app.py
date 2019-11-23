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

# Complete the method which accepts an array of integers, and returns one of the following:
# "yes, ascending" - if the numbers in the array are sorted in an ascending order
# "yes, descending" - if the numbers in the array are sorted in a descending order
# "no" - otherwise

def is_sorted_and_how(arr):
  if sorted(arr) == arr:
    return("yes, ascending")
  elif sorted(arr) == arr[::-1]:
    return("yes, descending")
  else:
    return("no")

is_sorted_and_how([3,2,1])

# Given a string, replace every letter with its position in the alphabet.
# If anything in the text isn't a letter, ignore it and don't return it.
# "a" = 1, "b" = 2, etc.

def alphabet_position(text):
  my_list = []
  for l in text:
    if l.lower() == "a":
      my_list.append("1")
    elif l.lower() == "b":
      my_list.append("2")
    elif l.lower() == "c":
      my_list.append("3")
    elif l.lower() == "d":
      my_list.append("4")
    elif l.lower() == "e":
      my_list.append("5")
    elif l.lower() == "f":
      my_list.append("6")
    elif l.lower() == "g":
      my_list.append("7")
    elif l.lower() == "h":
      my_list.append("8")
    elif l.lower() == "i":
      my_list.append("9")
    elif l.lower() == "j":
      my_list.append("10")
    elif l.lower() == "k":
      my_list.append("11")
    elif l.lower() == "l":
      my_list.append("12")
    elif l.lower() == "m":
      my_list.append("13")
    elif l.lower() == "n":
      my_list.append("14")
    elif l.lower() == "o":
      my_list.append("15")
    elif l.lower() == "p":
      my_list.append("16")
    elif l.lower() == "q":
      my_list.append("17")
    elif l.lower() == "r":
      my_list.append("18")
    elif l.lower() == "s":
      my_list.append("19")
    elif l.lower() == "t":
      my_list.append("20")
    elif l.lower() == "u":
      my_list.append("21")
    elif l.lower() == "v":
      my_list.append("22")
    elif l.lower() == "w":
      my_list.append("23")
    elif l.lower() == "x":
      my_list.append("24")
    elif l.lower() == "y":
      my_list.append("25")
    elif l.lower() == "z":
      my_list.append("26")

  li = " ".join(my_list)
  return(li)

# You are given an array (which will have a length of at least 3, but could be very large) containing integers. The array is either entirely comprised of odd integers or entirely comprised of even integers except for a single integer N. Write a method that takes the array as an argument and returns this "outlier" N.
def find_outlier(integers):
  even_list = []
  odd_list = []
  for i in integers:
    if i % 2 == 0:
      even_list.append(i)
    else:
      odd_list.append(i)
  if len(even_list) == 1:
    return(even_list[0])
  else:
    return(odd_list[0])

find_outlier([1,2,3,5,7,9])

# Given a number, write a function to output its reverse digits. (e.g. given 123 the answer is 321)
# Numbers should preserve their sign; i.e. a negative number should still be negative when reversed.
def reverse_number(n):
  if n < 0:
    n_pos = n * -1
    rev = str(n_pos)[::-1]
    reverse_num = int(rev)
    answer = reverse_num * -1
    return answer
  else:
    reverse_num = str(n)[::-1]
    answer = int(reverse_num)
    return answer

reverse_number(-1234)

# Create a function isDivisible(n, x, y) that checks if a number n is divisible by two numbers x AND y. All inputs are positive, non-zero digits.
def is_divisible(n,x,y):
  if n % x == 0 and n % y == 0:
    return "true"
  else:
    return "false"

is_divisible(12,6,3)

# You get an array of numbers, return the sum of all of the positives ones.
def positive_sum(arr):
  count = 0
  for i in arr:
    if i > 0:
      count = count + i
  return count


positive_sum([1,2,3,-4,-5,6,7])

# Write function RemoveExclamationMarks which removes all exclamation marks from a given string.
def remove_exclamation_marks(s):
  return(''.join(s.split("!")))

remove_exclamation_marks("wassup! you! are super! cool ma!n")

# Write a program that finds the summation of every number from 1 to num. The number will always be a positive integer greater than 0.
def summation(num):
  count = 0
  for i in range(1,num+1):
    count = count + i
  return count

summation(6)

# In this simple assignment you are given a number and have to make it negative. But maybe the number is already negative?
def make_negative( number ):
  if number > 0:
    return (number * -1)
  else:
    return number

# Create a function that takes an integer as an argument and returns "Even" for even numbers or "Odd" for odd numbers.
def even_or_odd(number):
  if number % 2 == 0:
    return "Even"
  else:
    return "Odd"

even_or_odd(69)