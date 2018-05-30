# Python Exercises
# Any of these exercises can be completed using a standard text editor and the command line; however, it is recommended that you make use of the features of a powerful IDE (integrated development environment) such as PyCharm.
#

# 1. Command Line Arguments
# Now that you're familiar with the standard "Hello, World!" application in Python, let's take it to the next level.
#
# Instead of printing "Hello, World!" to the console, we would like to say hello to a person whose name is supplied as a command line argument to our application.
#
# Tasks
# Create a copy of the HelloWorld application named Hello.
# Construct a String from "Hello, ", the first command line argument supplied to the application, and "!".
# Print that concatenated string to the console.
# Verify the expected behavior as outlined in the examples below.
# Example Output
# Hello World prints out the familiar "Hello, World!" text.
# Hello Dilbert prints "Hello, Dilbert!" to the console.
# If no command line arguments are supplied, the application should print "Hello, Unknown!".
# Bonus Work
# If multiple command line arguments are supplied to our Hello application, say hello to each of the named persons. For example, executing Hello Dogbert Catbert Ratbert should result in the following output.
#
# Hello, Laurent!
# Hello, Bogdan!
# Hello, Simon!
# But...when no command line arguments are supplied should still print out "Hello, Unknown!".
#
# hint: use input() 🤓
#
def printNames(names):
    for each in names:
        print('Hello,', each, '!')

def hello_world():
    name = input("Whom would you like to greet ? ")
    if ',' in name:
        name = name.replace(',', '').split()
        printNames(name)
    elif ' ' in name:
        name = name.split()
        printNames(name)
    elif len(name) > 0:
        print('Hello,', name, '!')
    elif len(name) is 0:
        name = 'Unknown'
        print('Hello,', name, '!')

# hello_world()

# 2. List of all files and directories names
# hint: use import os
#
# Write a function to print a list of all file/directory names from the working directory.
#
import os

def files_and_dirlist(path):
    res = os.listdir(path)
    for i in res:
        print(i)

# files_and_dirlist('/')
# Bonus Work
# Write a function to print a list of all file/directory names from the given path pass as an argument. (use listdir() from os)

# 3. Arrays are equal
# Write a function to test if two arrays contain the same integers:

arr1 = [2, 5, 7, 9, 11]
arr2 = [2, 5, 7, 8, 11]
arr3 = [2, 5, 11, 9, 7]

def are_two_arrays_equal(arg1, arg2):
    # note: .sort() returns none
    lst1 = sorted(arg1)
    lst2 = sorted(arg2)
    # if len(lst1) == len(lst2):
    if lst1 == lst2:
        print(lst1, lst2)
        return True
    else:
        print(lst1, lst2)
        return False


# print(are_two_arrays_equal(arr1, arr2))  # false
# print(are_two_arrays_equal(arr1, arr3))  # true

# 4. Middle character of a string
# Write a function to display the middle character of a string. Note:
#
# If the length of the string is even there will be two middle characters.
# If the length of the string is odd there will be one middle character.

def get_middle_character(args):
    index1 = int(len(args)/2)
    index2 = int(len(args)/2 -1)
    #print(index1, index2)
    if len(args) % 2 != 0:
        return args[index1]
    else:
        return args[index2], args[index1]

# print(get_middle_character("35100"))
# hint: pay attentions to the values that have floating point, not integers!

# 5. Vowels in a string
# Write a function to count all vowels in a string.

def count_of_vowels(args):
  count = 0
  vowels = 'aeiouAEIOU'
  for letter in args:
      if letter in vowels:
          count += 1
  return count

# print(count_of_vowels("Propulsion Academy"))

# 6. Check valid password
# Write a function to checks the users input and validates it based on the notes below. Notes:
#
# A password must have at least ten characters.
# A password consists of only letters and digits.
# A password must contain at least a capital letter in it.

def is_valid_password(input):
  if len(input) > 9 and input.isalpha() and any(x.upper() for x in input):
      return 'Password is valid'
  else:
      return 'you fucked up'

# print(is_valid_password('simpleMind'))

# 7. Find the second smallest element in an array
# Write a function to find the second smallest element in an array:

def find_second_smallest(args):
  args.sort()
  return args[1]

# print(find_second_smallest([0, 3, -2, 4, 3, 2]))  #0
# print(find_second_smallest([10, 22, 10, 20, 11, 22]))  #10

# 8. Remove duplicate elements from an array
# Write a function that removes duplicates entries in an array:

def unique_array(args):
    # return list(set(args))
# the other way
    newArray = []
    for i in args:
        if i not in newArray:
            newArray.append(i)
    return newArray

# print(unique_array([0, 3, -2, 4, 3, 2]))   # [0, 3, -2, 4, 2]
# print(unique_array([10, 22, 10, 20, 11, 22]))  #[10, 22, 20, 11]
# Food for Thought: in this case we are changing the original array, but what would happen if instead we will return a new array with the unique values. Can you think of any benefit by doing it in this way?
#
# 9. 50 pentagonal numbers
# Write a function to display the first 50 pentagonal numbers. Note: A pentagonal number is a figurate number that
# extends the concept of triangular and square numbers to the pentagon, but, unlike the first two, the patterns
# involved in the construction of pentagonal numbers are not rotationally symmetrical.

def get_pentagonal_number(n):
    for i in range(1,50):
        print(int(i*(i*3 -1)/2))

# get_pentagonal_number(50)

# Sample output:
# 1     5     12    22    35    51    70    92    117   145
# 176   210   247   287   330   376   425   477   532   590
# 651   715   782   852   925   1001  1080  1162  1247  1335
# 1426  1520  1617  1717  1820  1926  2035  2147  2262  2380
# 2501  2625  2752  2882  3015  3151  3290  3432  3577  3725


# 10. Length of the longest sequence of zeros in binary representation of an integer
# Write a function to find the length of the longest sequence of zeros in binary representation of an integer.

def get_size_of_longest_sequence_of_zeros(args):
  binary = bin(args)[2::1] # list comprehesnsion
  return max(len(i) for i in binary.split('1'))

# print(get_size_of_longest_sequence_of_zeros(7)) # binary representation: 111 - 0
# print(get_size_of_longest_sequence_of_zeros(8)) # binary representation: 1000 - 3
# print(get_size_of_longest_sequence_of_zeros(457)) # binary representation: 111001001 - longest 2
# print(get_size_of_longest_sequence_of_zeros(40)) # binary representation: 101000 - longest 3
# print(get_size_of_longest_sequence_of_zeros(12546)) # binary representation: 11000100000010 - longest 6

# 11. Fibonacci
# Write a function that computes the nth Fibonacci number, where f(n) = f(n-1) + f(n-2), given n >= 0, f(0) = 1, and f(1) = 1.

def fibonacci(args):
    if args is 0:
        return 0
    elif args is 1:
        return 1
    elif args > 1:
        return fibonacci(args - 1) + fibonacci(args - 2)

def fibonacciBonus():
    num = input('number pls')
    args = 0
    if num == '':
        return 'Error: you must supply which Fibonacci number to compute'
    else:
        args = int(num)
    if args is 0:
        return 0
    elif args is 1:
        return 1
    elif args > 1:
        return fibonacci(args - 1) + fibonacci(args - 2)

# print(fibonacciBonus())
# print(fibonacci(1))
# print(fibonacci(2))
# print(fibonacci(3))
# print(fibonacci(4))
# print(fibonacci(5))
# print(fibonacci(6))
# print(fibonacci(12)) # 144
# Bonus work
# Modify the Fibonacci application so that it computes the Fibonacci number for a number supplied as a
# command line argument and prints the Fibonacci number to the console.
# For example, executing Fibonacci 12 should print 144 to the console.
# If no command line argument is supplied, the application should print "Error: you must supply which Fibonacci number to compute".
#
# 12. Factorial
# Write a function that computes the factorial of a non-negative integer (denoted n!), where f(n) = n * f(n-1),
#  given n >= 0 and f(0) = 1.

def factorial(n):
    i = 1
    res = 1
    if n < 1:
        return 1
    else:
        while i <= n:
            res *= i
            i += 1
    return res

    # recursive solution
    # i = 1
    # res = 1
    # if n < 1:
    #     return 1
    # else:
    #     res = n * factorial(n - 1)
    #     return res

# print(factorial(5))
# Example Output
# Executing the Factorial application should print the following to the console.
#
# 0! = 1
# 1! = 1
# 2! = 2
# 3! = 6
# 4! = 24
# 5! = 120
# Bonus Work
# If you implemented factorial() using recursion, comment out your solution and implement factorial() using an iterative loop.
#
# If you implemented factorial() using an iterative loop, comment out your solution and implement factorial() using recursion.
#

# 13. Prime Numbers
# Write a function that determines if a given number is a prime number using an iterative loop.

def prime_number(n):
    if n < 2:
        return False
    else:
        for i in range(2, n-1):
            if n % i == 0:
                return False
        return True


# print(prime_number(11))
# print(prime_number(9))
# Example Output
# Executing the Primes application should print the following to the console.
#
# # Prime numbers between 1 and 20 are:
# [2, 3, 5, 7, 11, 13, 17, 19]

# 14. Sorting an Array
# Given an array of numbers, sort them in such a manner that all the odd numbers in the array are
#  sorted in ascending order and the even numbers are sorted in descending order after the last odd number.
# For example [1,2,3,4,5,6,7,8,9] produces the output [1,3,5,7,9,8,6,4,2].
# If the array contains decimals, round them down while checking for odd/even.

import math
def sort_it(theArray):
    ods = []
    evens = []
    theArray.sort()
    for i in theArray:
        if math.floor(i) % 2 == 0:
            evens.append(i)
        else:
            ods.append(i)
    reversed = evens[::-1]
    return ods + reversed

# print(sort_it([1, 2, 3, 4, 5, 6, 7, 8, 9]))
# print(sort_it([26.66, 24.01, 52.00, 2.10, 44.15, 1.02, 11.15]))
# Example Output
# Executing the Sorting application should print the following to the console.
#
# [1.0, 3.0, 5.0, 7.0, 9.0, 8.0, 6.0, 4.0, 2.0]
# [1.02, 11.15, 52.0, 44.15, 26.66, 24.01, 2.1]
# Tip: from math import floor can be used to round a double value down.
#

# 15. Find the Digit
# Write a function that takes a positive number as a parameter (n) and
# returns the number of times you must multiply its digits until you reach a single digit.
#
# For example: find(57) == 3, because 5 * 7 = 35, 3 * 5 = 15, and 1 * 5 = 5.
import functools

def find(number, count=0):
     if number < 10:
         return count
     else:
         while number >= 10:
             number = functools.reduce(lambda x, y: x * y, [int(i) for i in str(number)])
             count += 1
         return count

# print(find(57)) # 3
# print(find(5923)) # 2
# print(find(90)) # 1
# print(find(7)) # 0
# print(find(999)) # 4

# Example Output
# Executing the DigitFinder application should print the following to the console.
#
# 3 // because 5*7 = 35, 3*5 = 15, 1*5 = 5
# 2 // because 5*9*2*3 = 270, 2*7*0 = 0
# 1 // because 9*0 = 0
# 0 // because 7 is already a single digit
# 4 // because 9*9*9 = 729, 7*2*9 = 126, 1*2*6 = 12, 1*2 = 2
