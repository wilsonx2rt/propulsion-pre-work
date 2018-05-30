# def is_prime(x):
#     if x < 2:
#         return False
#     else:
#         for n in range(2, x-1):
#             if x % n == 0:
#                 return False
#         return True
# print(is_prime(4))
#
#
# def factorial(x):
#     num = x
#     result = 1
#     while num >= 1:
#         result *= num
#         num -= 1
#     return result
# print(factorial(1))
#
# def digit_sum(x):
#     total = 0
#     while x > 0:
#         total += x % 10
#         x = x // 10
#         print(x)
#     return total
#
# def is_int(x):
#     absoluteCount = abs(x)
#     typeCount =type(x)
#     roundCount = round(absoluteCount)
#     if typeCount and absoluteCount - roundCount == 0:
#         return True
#     else:
#         return False
#
# def reverse(text):
#   length = len(text) -1
#   reverse = ''
#   while length >= 0:
#       reverse += text[length]
#       length -= 1
#   return reverse
# reverse('abc')
#
# def anit_vowel(text):
#     newStr = text
#     for letter in text:
#         if letter in 'AEIOUaeiou':
#             newStr = newStr.replace(letter, '')
#     print(newStr)
# anit_vowel('abcde')
#
# score = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2,
#          "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3,
#          "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1,
#          "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4,
#          "x": 8, "z": 10}
#
# def scrabble_score(word):
#     testWord = word.lower()
#     wordScore = 0
#     for letter in testWord:
#         wordScore += score[letter]
#     print(wordScore)
# scrabble_score('constitution')
#
# def censor(text, word):
#   if word in text:
#     return text.replace(word, len(word)*"*")
# print(censor("this hack is wack hack", "hack"))
#
# def count(sequence, item):
#     count = 0
#     for num in sequence:
#         if num is item:
#             count += 1
#     return count
# print(count([1, 2, 1, 1], 1))
#
# def purify(x): #fails 4,5,5,4
#   for n in x:
#     if n % 2 != 0:
#       x.remove(n)
#   return x
# print(purify([4,5,5,4]))
#
# def purity(lst): #passes all tests
#     res = []
#     for n in lst:
#         if n % 2 is 0:
#             res.append(n)
#     return res
# print(purity([4,5,5,4]))
#
# def product(lst):
#   res = 1
#   for n in lst:
#     res *= n
#   return res
# print(product([2,3,4,5]))
#
# def remove_duplicates(lst):
#     newLst = []
#     for n in lst:
#         if n not in newLst:
#             newLst.append(n)
#     return newLst
# print(remove_duplicates([1, 1, 2, 2]))
#
# def median(lst):
#   lst.sort()
#   res = 0
#   l = len(lst)
#   m = int((l/2)-0.5)
#   if l % 2 != 0:
#       res = lst[m]
#   else:
#       res = (lst[int(l/2)] + lst[int((l/2)-1)])/2
#   return res
# # print(median([1, 1, 2]))
# print(median([4, 5, 5, 4]))
#
# # codecademy solution
#
#
# def median1(lst):
#     sorted_list = sorted(lst)
#     if len(sorted_list) % 2 != 0:
#         # odd number of elements
#         index = len(sorted_list) // 2
#         return sorted_list[index]
#     elif len(sorted_list) % 2 == 0:
#         # even no. of elements
#         index_1 = len(sorted_list) / 2 - 1
#         index_2 = len(sorted_list) / 2
#         mean = (sorted_list[index_1] + sorted_list[index_2]) / 2.0
#         return mean
#
#
# print(median1([4, 5, 5, 4]))
#
# # Pig Latin https://www.codecademy.com/courses/learn-python/lessons/pyglatin/exercises/testing-testing-is-this-thing-on-?action=lesson_resume
# # pyg = 'ay'
#
# original = input('Enter a word:')
#
# if len(original) > 0 and original.isalpha():
#   word = original.lower()
#   first = word[0]
#   new_word = word + first + pyg
#   new_word = new_word[1:len(new_word)]
#   print(new_word)
# else:
#     print('empty')



# Create a function is_string() that returns true when the parameter passed is a
# string and false otherwise.

def is_string(input):
    return isinstance(input, str)

    # other possibility
    # if type(input) == str: # isinstance
    #     return True
    # else:
    #     return False

print(is_string('hello'))  # True
print(is_string(['hello']))  # False
print(is_string('this is a long sentence'))  # True
print(is_string({'a': 2}))  # False


# Based on the is_string function create another function that check if the argument
# contains space & digits

def is_only_string(input):
    space = False
    number = False
    if not is_string(input):
        return False
    for i in input:
        if i == ' ':
            space = True
        elif i.isdigit():
            number = True
    if space == True and number == True:
        return True
    else:
        return False

print(is_only_string('11'))  # False
print(is_only_string(['hello']))  # ? Please handle this case!! Should return False
print(is_only_string('this is a long sentence'))  # False
print(is_only_string({'a': 2}))  # # ? Please handle this case!! Should return False
print(is_only_string('11 1')) # True

# modify the is_string function so now it returns true if all characters in the string are
# alphanumeric and there is at least one character, false otherwise.

def is_alphanumeric(input):
   if is_string(input) == True:
       if input is not '' and input is not ' ':
           if input.isalpha() or input.isnumeric():
               return True
           else:
               return False
   else:
       return False



print(is_alphanumeric('11'))  # True
print(is_alphanumeric('abc'))
print(is_alphanumeric(['hello']))  # False
print(is_alphanumeric('this is a long sentence'))  # False
print(is_alphanumeric({'a': 2}))  # False
print(is_alphanumeric("this is string....!!!"))  # False

# Create a function that returns true when the parameter passed is a list or a tuple and
# false otherwise.

def is_array_or_tuple(input):
    if type(input) == list or type(input) == tuple:
        return True
    else:
        return False

print(is_array_or_tuple('hello'))  # False
print(is_array_or_tuple(['hello']))  # True
print(is_array_or_tuple([2, {}, 10]))  # True
print(is_array_or_tuple({'a': 2}))  # False
print(is_array_or_tuple((1, 2)))  #
print(is_array_or_tuple(set()))

# Check for types in array. Create a function that checks whether all the element of an
# array are the same data type. For example, whether they are all a String or a number.

def are_same_type(input):
    if type(input) is not list:
        return 'argument should be a list'
    control_var = type(input[0])
    count = 0
    for each in input:
         if type(each) == control_var:
             count +=1
    if count == len(input):
        return True
    else:
        return False

print(are_same_type(['hello', 'world', 'long sentence']))  # True
print(are_same_type([1, 2, 9, 10]))  # True
print(are_same_type([['hello'], 'hello', ['bye']]))  # False
print(are_same_type([['hello'], [1, 2, 3], [{'a': 2}]]))  # True
print(are_same_type([['hello'], set('hello')]))  # False

# Sort and remove duplicates Take 2 strings s1 and s2 including only letters from a to z.
# Return a new string, longest possible, containing distinct letters,
#  - each taken only once - coming from s1 DO NOT USE set() ;)

a = 'xyaabbbccccdefww'
b = 'xxxxyyyyabklmopq'
x = 'abcdefghijklmnopqrstuvwxyz'

def longest_string(s1, s2):
    new_str = s1 + s2
    str_list =[]
    for each in new_str:
        if each not in str_list:
            str_list.append(each)
    return ''.join(sorted(str_list))

    # solution using set
    # new_str = set(s1+s2)
    # return ''.join(sorted(new_str))

print(longest_string(a, b))  # abcdefklmopqwxy
print(longest_string(a, x))  # abcdefghijklmnopqrstuvwxyz

# Convert a random number to reversed array of digits. Give a random number.
# You have to return the digits of this number an array in reverse order.

def convert(input):
    string = str(input)
    array = []
    for each in string:
        if each not in array:
            array.append(each)
    return sorted(array, reverse=True)

print(convert(429563))  # [9, 6, 5, 4, 3, 2]
print(convert(324))  # [4, 3, 2]

# Count repetitions! You will be given an array of string.
# ['kerouac', 'fante', 'fante', 'buk', 'hemingway', 'hornby', 'kerouac', 'buk', 'fante']
# DO NOT USE COUNTER from Collections module (that would be cheating 😁)

def count_repetition(input):
    counted_elements = {}
    for each in input:
        if each not in counted_elements:
            counted_elements[each] = 1
        else:
            counted_elements[each] = counted_elements[each] + 1
    return counted_elements

print(count_repetition(['kerouac', 'fante', 'fante', 'buk', 'hemingway', 'hornby', 'kerouac', 'buk', 'fante']))
# {'kerouac': 2, 'fante': 3, 'buk': 2, 'hemingway': 1, 'hornby': 1}

# Cat and Mouse You will be given a string featuring a cat 'C' and a mouse 'm'.
#  The rest of the string will be made up of '.'. You need to find out if the cat can
# catch the mouse from it's current position. The cat can jump three characters.

def is_caught(input):
    tom = input.find('C')
    jerry = input.find('m')
    if jerry - tom < 4:
        return True
    else:
        return False

print(is_caught('C.....m'))  # False
print(is_caught('C..m'))  # True
print(is_caught('..C..m'))  # True
print(is_caught('...C...m'))  # False
print(is_caught('C.m'))  # True

# Split the bill Write a function to balance who has overpaid and should be compensated
#  or who has paid less. The function should take one parameter: a dictionary which represents
#  the members of the group and the amount spent by each. The function should return an object
#  with the same names, showing how much money the members should pay or receive.
# Negative number means they should receive money.

group = {
    'Amy': 20,
    'Bill': 15,
    'Chris': 10
}

def split_the_bill(input):
 for key, value in input.items():
     input[key] = input[key] - 15
     if input[key] is not 0:
         input[key] = -input[key]
 return input

print(split_the_bill(group)) # { 'Amy': -5, 'Bill': 0, 'Chris': 5 }

# Exponentiation Write a function that takes two integers. The first one will be the
# base b and the second one n will be the exponent. The function should return the value
# of b raised to the power n. Try to solve it with recursion. You can try first with a
# while loop and then try to implement the recursive approach.

def exp_recursive(b, n):
    count = 1
    result = b
    while count < n:
        result *= b
        count += 1
    return result

    # recursive
    # if n == 1:
    #     return b
    # else:
    #     return b * pow(b, n -1)

print(exp_recursive(5, 3))  # 125
print(exp_recursive(2, 4))  # 16
print(exp_recursive(5, 1))  # 5
print(exp_recursive(6, 0))  # 1

# Zero Sum Write a function that expects an array of integers and returns an array of
# pairs with the indexes of two numbers that sum 0.

def zero_sum(input):
    results_array = []
    for i in input:
        for j in input:
            if i + j == 0:
                if sorted([input.index(i), input.index(j)]) not in results_array:
                    results_array.append(sorted([input.index(i), input.index(j)]))
    return results_array


print(zero_sum([1, 5, 0, -5, 3, -1]))  # [[0, 5], [1, 3], [2, 2]]
print(zero_sum([1, -1]))  # [[0, 1]]
print(zero_sum([0, 4, 3, 5]))  # [[0, 0]]

# Write a function that accepts a sentence and calculates the number of upper case letters
# and lower case letters. Use the input function providing the sentence from the console.
# Suppose the following input is supplied to the program: Hello world!
# Then, the output should be: UPPER CASE 1 LOWER CASE 9

def count_upper_lower():
    upper = 0
    lower = 0
    sentence = input('Write something: ')
    for el in sentence:
        if el.isalpha():
            if el == el.upper():
                upper += 1
            else:
                lower += 1
    return f'UPPER CASE {upper} LOWER CASE {lower}'

print(count_upper_lower())

# Convert a list into a nested dictionary of keys.

def new_dict(input):
    dict = current = {}
    for each in input:
        current[each] = {}
        current = current[each]
    return dict

print(new_dict([1, 2, 3, 4, 5])) # {1: {2: {3: {4: {5: {}}}}}}

# Write a function that computes the net amount of a bank account based a transaction
# log from console input. The transaction log format is shown as following:
# D 100
# W 200

# D means deposit while W means withdrawal.
# Suppose the following input is supplied to the program:
# D 300
# D 300
# W 200
# D 100
# Then, the output should be:
# 500

def account_balance():
    results = 0

    while True:
        log_entry = input("Log entry:  ").split()
        print(log_entry)
        if not log_entry:
            break;

        amount = int(log_entry[1])
        if log_entry[0] == 'D':
            results += amount
        elif log_entry[0] == 'W':
            results -= amount

    print(results)

account_balance()

# Function which can generate a dictionary where the keys are numbers between
# 1 and 20 (both included) and the values are square of keys. The function should just
# print the values only.

def print_dictionary():
    dict = {}
    for each in range(1,21):
        dict[each] = each**2
    print(dict.values())

print_dictionary()

# result
# 1
# 4
# 9
# 16
# 25
# 36
# 49
# 64
# ...

# Create all possible permutations from a given collection of distinct numbers.

def permute(input):
    pass

# print(permute([1, 2, 3])) # [[3, 2, 1], [2, 3, 1], [2, 1, 3], [3, 1, 2], [1, 3, 2], [1, 2, 3]]

# Create a function that returns based on a number between 0-99
# it's written value as string. Bonus points if you support even higher numbers!

def write_num(num):
    pass

# write_number(11) # "eleven"
# write_number(2) # "two"
# write_number(32) # "thirty-two"
