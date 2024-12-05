# ---------------------------------------------------------------
# CONDITIONAL LOGIC
# is_old = True
# is_licenced = False

# if is_old and True:
# 	print('you are old enough to drive!')
# elif is_licenced:
# 	print('jump')
# else:
#   print('check')

# INDENTATION => 4 spaces

# TRUTHY and FALSY in python --> bool(any_value) : T/F
# if any_value:  ----> any_value is automatically converted to T/F in IF Statement.
# Accepted Falsy Values: None, False, 0, 0.0, 0j, Decimal(0), Fraction(0,1), [], {}, (), '', b'',
# set(), range(0), obj__bool__() returns False, obj__len__() returns 0.

# TERNARY OPERATOR
# USAGE FORMAT ----> (do_if_true IF condition ELSE do_if_false)
# is_friend = True
# can_message = "message allowed" if is_friend else "not allowed to message"

# SHORT CIRCUITING
# AND/OR usage for python interpreter
# LOGICAL OPERATORS
# <, >, ==, >=, <=, !=, not(1==1), not, is.
# print(True == 1) --> True
# print(10 == 10.0) --> True
# print('1' == 1) --> False
# IS --> check both value and type ('===' in JS). Also, checks the value in memory location
# print([1,2] is [1,2]) ---> False - This issue is valid for dict, set, tuple. Because, they are
# created in different memory space.

# ---------------------------------------------------------------
# FOR LOOPS
# Iterables - list, dictionary, tuple, set, string (one by one check each item in the collection)
# for variable_name in any_iterable:
#   operational issues
#   ....
# Ex.1:
# for item in 'Python Programming':
# 	print(item)
# Ex.2:
# user = {
# 	'name': 'jason',
# 	'age': 35,
# 	'can_swim': True
# }
# for key,value in user.items():
# 	print(key,value)
#
# for item in user.values():
# 	print(item)
#
# for item in user.keys():
# 	print(item)

# range(start,stop,step_over) ==> Return an "object" that produces a sequence of integers from
# start (inclusive) to stop(exclusive) by step.
# list(range(5)) --> [1,2,3,4,5] ||| range(5) --> range(0,5): Special Object
# Ex.3:
# for num in range(3,20):
# 	print(num)
# Ex.4:
# for _ in range(10,4,-1):
# 	print(_)

# enumerate() ==> Return an enumerate "object".Iterable must be another object that supports
# iteration.The enumerate object yields pairs containing an index_counter and a value yielded by the
# iterable argument.
# Ex.5:
# for i,char in enumerate('helloooo'):
# 	print(f'{i}.index ---> {char}')
# Ex.6:
# for i,item in enumerate((1,33,54)):
# 	print(f'{i}.index ---> {item}')
# Ex.7:
# for i,item in enumerate(list(range(20))):
# 	print(f'{i}.index ---> {item}')
# 	print('|||||||||||') if i==13 else None
# ---------------------------------------------------------------
# WHILE LOOPS
# while loops are more flexible and powerful than for loops.
# But, for-loops are simpler and more readable.
# while condition:
#   do_something

# Ex.1:
# my_list = [1, 2, 3]
# i = 0
# while i < len(my_list):
#     print(my_list[i], end='\t')
#     i += 1
# else:
#     print('\nDone with all the work.')
# Ex.2:
# while True:
#     response = input('Say Something: ')
#     if response == 'bye':
#         break

# Break, Continue, Pass
# 'continue' will skip the lines below it and continue to loop.
# for i in range(0, 5):
# 	print(i)
# 	continue
# 	print("I will never be printed")
#
# for i in range(10):
# 	pass  # it can be used to avoid error and when we have not yet decided on the code to write.

# Examples;
# my_list = [1, 2, 3]
# i = 0
# while i < len(my_list):
#     print(my_list[i])
#     i += 1
#     continue
#
# i = 0
# while i < len(my_list):
#     print(my_list[i])
#     i += 1
#     break
#
# i = 0
# while i < len(my_list):
#     i += 1
#     pass
# print("No error")

# Exercise-1
# Display the image below to the right hand side where the 0 is going to be ' ', and the 1 is
# going to be '*'. This will reveal an image!
# picture = [
#   [0,0,0,1,0,0,0],
#   [0,0,1,1,1,0,0],
#   [0,1,1,1,1,1,0],
#   [1,1,1,1,1,1,1],
#   [0,0,0,1,0,0,0],
#   [0,0,0,1,0,0,0]
# ]
#
# fill = '*'
# empty = ' '
# for image in picture:
#   for pixel in image:
#     if pixel:
#       print(fill, end ="")
#     else:
#       print(empty, end ="")
#   print('')

# Exercise-2
# some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']
# duplicates = []
#
# for value in some_list:
#     if some_list.count(value) > 1:
#         if value not in duplicates:
#             duplicates.append(value)
#
# print(duplicates)

# CleanCode --> readability, predictablity, DRY(use functions).

# ---------------------------------------------
# FUNCTIONS --> modifies in it OR return something after works done.
# Should do one issue very well OR should return something
# Functions & Methods are used to take actions on data types.
# -Function Definition-
# def func_name():
# 	....
#   return ...

# -Funciton Call-
# func_name()

# Example-1:
# def show_pic():
# 	fill = '*'
# 	empty = ' '
# 	for image in picture:
# 	  for pixel in image:
# 	    if pixel:
# 	      print(fill, end ="")
# 	    else:
# 	      print(empty, end ="")
# 	  print('')

# show_pic() -- calling the func. should be after definition
# print(show_pic) --> <function show_pic ar 0x7ff8....>

# PARAMETERS & ARGUMENTS
# Used to make functions dynamic
# Rule( def. order) : params, *args, default parameters, **kwargs

# -----Positional Parameters------
# def say_hello(name,emoji):
#   print(f'hiiii {name} {emoji}')

# ---Default Parameters---
# def say_hello(name='Jason',emoji=':(('):
#   print(f'hiiii {name} {emoji}')

# -----positional arguments------
# say_hello('jess',':)')

# Default Arguments
# say_hello("saurabh")
# say_hello() --> functions works with default parameters

# -----keyword arguments------
# argument positions are not important!
# say_hello(emoji=':)',name='Babe' )

# -----return: similar to break in functions for interpreter operation------
# Void functions don't use 'return' keyword and returns 'None'!!!
# def adding(num1,num2):
# 	return num1+num2
#
# total = adding(3,5)
# print(total)
# print( adding(10,adding(4,7)) )

# -----SpecialCase1---
# def sum_func(num1,num2):
#   def another_func(n1,n2):
#       return n1+n2
#   return another_func -----> !!!!!!

# total = sum_func(10,20)
# print(total(10,20)) -----> ****
# print(sum_func(7,3)(10,20)) -----> ****
# print(sum_func(10,5))    # this will just return the address of the function

# -----SpecialCase2---
# def sum_func(num1,num2):
#   def another_func(n1,n2):
#       return n1+n2
#   return another_func(num1,num2) -----> !!!!!!

# total = sum_func(10,20)
# print(total) -----> ****

# print(another_func(45, 55))
# This will give error, becuase the function is actually undefined, and to call this function,
# First we will have to call the parent function. So we can get the memory location of the function.

# Methods are functions owned by an object or a data type.

# DOCSTRING ---> '''function info section'''
# def test(a):
# 	'''
# 	 Info: this function for test
# 	:param a:
# 	:return:
# 	'''
# 	print(a)
# --Dunder Method--
# print(test.__doc__)

# Exercise-1
# def highest_even(li):
#     evens = []
#     for item in li:
#         if not item % 2 and item not in evens:
#             evens.append(item)
#     return max(evens)
#
# print(highest_even([10, 2, 3, 4, 8, 11]))

# ------- *args & **kwargs ----------
# *args ---> can accept any number of positional argument
# **kwargs --> keyword arguments

# def super_func(name, *args, i='hi', **kwargs):
# 	print(*args) # shown as 1 2 3 4 5
# 	print(args) # in tuple form: (1,2,3,4,5)
# 	print(kwargs) # in dict form: {'num1': 7, 'num2': 10}
# 	total=0
# 	for items in kwargs.values():
# 		total += items
#
# 	return sum(args) + total
#
# print(super_func('Andy',1,2,3,4,5, num1=7, num2=10))

# ---------------------------------------------

# WALRUS OPERATOR --> ':='
# That assigns values to variables as part of a larger expression
# a = 'helloooooooooo'

# if (len(a) > 10):
#     print(f"too long {(len(a)} elements")

# EX:
# if ((n := len(a)) > 10):
#     print(f"too long {n} elements")

# A similar benefit arises during regular expression matching where match objects are needed twice,
# once to test whether a match occurred and another to extract a subgroup
# discount = 0.0
# if (mo := re.search(r'(\d+)% discount', advertisement)):
#     discount = float(mo.group(1)) / 100.0

# The operator is also useful with while-loops that compute a value to test loop termination
# and then need that same value again in the body of the loop:
# while ((n := len(a)) > 1):
#     print(n)
#     a = a[:-1]
# print(a)

# Another motivating use case arises in list comprehensions
# where a value computed in a filtering condition is also needed in the expression body:
# EX:
# [clean_name.title() for name in names if (clean_name := normalize('NFC', name)) in allowed_names]

# ---------------------------------------------
# SCOPE -->It is what variables I have access to!
# Using scope is useful for effective usage of Garbage Collector.
# global scope - local scope (inside function, conditionals, loops etc.)
# Variable Check Rules in PY:
# 1 - start with local
# 2 - Parent local?
# 3 - global
# 4 - is built-in python functions

# Ex:
# total = 0
# def count():
# 	global total # If you don't use "global" --> UnboundLocalError: cannot access local variable
# 				 # 'total' where it is not associated with a value
# 	total+=1
# 	return total
#
# count()
# count()
# print(count())

# Dependency Injection is simplified version of this usage.
# Ex:
# total = 0
# def count(total):
# 	total+=1
# 	return total

# print(count(count(count(total))))

# ---nonlocal keyword--- Closures---
# def outer():
#     x = "local"
#     def inner():
#         nonlocal x
#         x = "nonlocal"
#         print("inner:", x)
#     inner()
#     print("outer:", x)
# outer()

# inner: nonlocal
# outer: nonlocal

# ---------------------
# PEP (Python Enhancement Proposals) - PEP 8 is most popular one.
