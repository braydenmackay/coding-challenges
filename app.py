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

# Your task is to make a function that can take any non-negative integer as a argument and return it with its digits in descending order. Essentially, rearrange the digits to create the highest possible number.
def Descending_Order(num):
  ascending_num = ''.join(sorted(str(num)))
  return(int(ascending_num[::-1]))
  
Descending_Order(7893546)

# For example, if we run 9119 through the function, 811181 will come out, because 92 is 81 and 12 is 1.
def square_digits(num):
  my_list = []
  str_num = str(num)
  for i in str_num:
    squared_val = int(i)**2
    my_list.append(str(squared_val))
  return(int(''.join(my_list)))

square_digits(3113)

# Write a function to convert a name into initials. This kata strictly takes two words with one space in between them. The output should be two capital letters with a dot separating them.
def abbrevName(name):
  answer = []
  split_name = (name.split())
  for word in split_name:
    answer.append(word[0])
  first_letter = answer[0].upper()
  second_letter = answer[1].upper()
  return(f'{first_letter}.{second_letter}')

abbrevName('brayden mackay')

# Given a set of numbers, return the additive inverse of each. Each positive becomes negatives, and the negatives become positives.
def invert(lst):
  my_list = []
  for i in lst:
    my_list.append(i * -1)
  return(my_list)

invert([-1,2,3,-4,5,6,-7])

# Write a function that returns both the minimum and maximum number of the given list/array.
def min_max(lst):
  my_lst = []
  my_lst.append(min(lst))
  my_lst.append(max(lst))
  return my_lst

min_max([1,2,3,4,5,11,7,8])

# Make a program that filters a list of strings and returns a list with only your friends name in it. If a name has exactly 4 letters in it, you can be sure that it has to be a friend of yours! Otherwise, you can be sure he's not...
def friend(x):
  my_friends = []
  for name in x:
    if len(name) == 4:
      my_friends.append(name)
  return my_friends
    

friend(['kyle', 'brayden', 'tim', 'cole'])

# Complete the method that takes a boolean value and return a "Yes" string for true, or a "No" string for false.
def bool_to_word(boolean):
  if boolean == True:
    return 'Yes'
  else:
    return 'No'

bool_to_word(True)

# Check to see if a string has the same amount of 'x's and 'o's. The method must return a boolean and be case insensitive. The string can contain any char.
def xo(s):
  x_arr = []
  o_arr = []
  for char in s:
    if char.lower() == 'x':
      x_arr.append(char)
    elif char.lower() == 'o':
      o_arr.append(char)
  if len(x_arr) == len(o_arr):
    return True
  else:
    return False

xo('xxoOxo')

# create a function that takes a list of non-negative integers and strings and returns a new list with the strings filtered out.
def filter_list(l):
  num_arr = []
  for char in l:
    if type(char) == int:
      num_arr.append(char)
  return num_arr

filter_list([1,2,3,'a','b',3,5])

# Build a function that takes in two arguments (salary, bonus). Salary will be an integer, and bonus a boolean. If bonus is true, the salary should be multiplied by 10. If bonus is false, the fatcat did not make enough money and must receive only his stated salary.
def bonus_time(salary, bonus):
  if bonus == True:
    salary = salary * 10
    return('$' + str(salary))
  else:
    return('$' + str(salary))

bonus_time(1000, True)

# Given an array of numbers (a list in groovy), determine whether the sum of all of the numbers is odd or even. Give your answer in string format as 'odd' or 'even'. If the input array is empty consider it as: [0] (array with a zero).
def oddOrEven(arr):
  total_sum = sum(arr)
  num_items = len(arr)
  if  num_items == 0:
    return 'odd'
  elif total_sum % 2 == 0:
    return 'even'
  else:
    return 'odd'

oddOrEven([])

# Given an array of integers, return a new array with each value doubled.
def maps(a):
    my_arr = []
    for num in a:
      my_arr.append(num * 2)
    return my_arr

# There is a bus moving in the city, and it takes and drop some people in each bus stop. You are provided with a list (or array) of integer arrays (or tuples). Each integer array has two items which represent number of people get into bus (The first item) and number of people get off the bus (The second item) in a bus stop. Your task is to return number of people who are still in the bus after the last bus station (after the last array). Even though it is the last bus stop, the bus is not empty and some people are still in the bus, and they are probably sleeping there. Please keep in mind that the test cases ensure that the number of people in the bus is always >= 0. So the return integer can't be negative. The second value in the first integer array is 0, since the bus is empty in the first bus stop.
def number(bus_stops):
  total = []
  for arr in bus_stops:
    total.append(arr[0] - arr[1])
  return sum(total)

# Take 2 strings s1 and s2 including only letters from ato z. Return a new sorted string, the longest possible, containing distinct letters, Each taken only once - coming from s1 or s2.
def longest(s1, s2):
  combined_s = s1 + s2
  new_s = (set(combined_s))
  return ''.join(sorted(new_s))

# Return the number (count) of vowels in the given string. We will consider a, e, i, o, and u as vowels
def getCount(inputStr):
  num_vowels = 0
  for l in inputStr:
    if l == 'a' or l == 'e' or l == 'i' or l == 'o' or l == 'u':
      num_vowels = num_vowels + 1
  return num_vowels

# Usually when you buy something, you're asked whether your credit card number, phone number or answer to your most secret question is still correct. However, since someone could look over your shoulder, you don't want that shown on your screen. Instead, we mask it. Your task is to write a function maskify, which changes all but the last four characters into '#'.
def maskify(cc):
  my_list = []
  char_len = len(cc)
  count = 0
  for char in cc:
    if count < (char_len - 4):
      my_list.append('#')
      count = count + 1
    else:
      my_list.append(char)
  return(''.join(my_list))

# Get the number n (n>0) to return the reversed sequence from n to 1. Example : n=5 >> [5,4,3,2,1]
def reverse_seq(n):
  my_list = []
  for n in range(1,n+1):
    my_list.append(n)
  return(my_list[::-1])

# Alex just got a new hula hoop, he loves it but feels discouraged because his little brother is better than him. Write a program where Alex can input (n) how many times the hoop goes round and it will return him an encouraging message :) -If Alex gets 10 or more hoops, return the string "Great, now move on to tricks". -If he doesn't get 10 hoops, return the string "Keep at it until you get it".
def hoop_count(n):
    if n >= 10:
      return "Great, now move on to tricks"
    else:
      return "Keep at it until you get it"

# The male gametes or sperm cells in humans and other mammals are heterogametic and contain one of two types of sex chromosomes. They are either X or Y. The female gametes or eggs however, contain only the X sex chromosome and are homogametic. The sperm cell determines the sex of an individual in this case. If a sperm cell containing an X chromosome fertilizes an egg, the resulting zygote will be XX or female. If the sperm cell contains a Y chromosome, then the resulting zygote will be XY or male. Determine if the sex of the offspring will be male or female based on the X or Y chromosome present in the male's sperm. If the sperm contains the X chromosome, return "Congratulations! You're going to have a daughter."; If the sperm contains the Y chromosome, return "Congratulations! You're going to have a son.";
def chromosome_check(sperm):
    if sperm == 'XY':
      return 'Congratulations! You\'re going to have a son.'
    else:
      return 'Congratulations! You\'re going to have a daughter.'