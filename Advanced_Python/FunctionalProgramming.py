# WHAT IS FUNCTIONAL PROGRAMMING?
# It is about separation of concerns as OOP. But, Separate data and functions.
# Instead of combining methods and attributes, we separate them apart.
# Functions use lists, dictionaries instead of Class(Objects)
# Packaging our codes to make it well-organized.
# Objectives:
# Clear + Understandable Codes, Easy to Extend, Easy to Maintain, Memory Efficient, DRY
# One Pillar ==> Pure Functions
# ---------------------------------------
# PURE FUNCTIONS
# More pure functions => less fault in your code. We can test our code more easily. Easier to
# understand our code.
# Two Rules:
# 1. Giving the same data, always return the same output.
# 2. Function should not produce any side effects(any things effect outside world).
# def multiply_by2(li):
#     new_li = []
#     for item in li:
#         new_li.append(item)
#     return new_li
#
# print(multiply_by2([5,6,8]))
'''
If we define 'new_li' outside the function, or print something inside the function,
then it is no longer a pure function.
'''
# -------------- MAP, FILTER, ZIP, REDUCE-------------------------
# MAP(func, *iterables) --> make an iterator that computes the function using arguments from each
# of the iterables. Stops when  the shortest iterable is exhausted.
# def multiply_by2(item):
#     return item*2
#
# my_list = [5,8,9]
#
# print(map(multiply_by2, my_list))  # it returns a map object, which then we can convert to a
# # list/tuple/set -->  <map object at 0x0000028B04D899F0>
# print(list(map(multiply_by2, my_list))) # notice that we just write the function name without the
# # curly braces --> [10, 16, 18]
# print(my_list) # [5, 8, 9]
'''
notice that map is not modifying anything, and creating a new list. 
it is also using separate data and function to work upon them.
it's a nice concept of Functional programming and pure function.
'''
# ***************
# FILTER(func, *iterables) --> Filtering function by using map format.
# def only_even(item):
#     return item % 2 == 0
#
# my_list = [5,8,9,2,5,6,98,56,62]
#
# print(filter(only_even, my_list)) # <filter object at 0x000002004F497250>
# print(list(filter(only_even, my_list))) # [8, 2, 6, 98, 56, 62]
# print(list(map(only_even, my_list))) # [False, True, False, True, False, True, True, True, True]
# print(my_list) # [5, 8, 9, 2, 5, 6, 98, 56, 62]

# ***************
# REDUCE(func, sequence/data, initial) --> reduce as JS language
# from functools import reduce

# def accumulator(acc, item):
#     print(f'acc: {acc}, item: {item}')
#     return acc+item
#
# my_list = [1,2,3,4,5]
# print(reduce(accumulator, my_list)) # by default takes '0'(acc initial value)
# as the 3rd argument --> result: 15

# print(reduce(accumulator, my_list, 10)) # (acc=10)--> result: 25
# print(my_list) # [1, 2, 3, 4, 5]
'''
acc is nothing but the return of the last iteration.
'''
# EX:
# from functools import reduce
# my_numbers = [5,4,3,2,1]
# scores = [73, 20, 65, 19, 76, 100, 88]
# def accumulator(acc, item):
#     return acc + item
#
# print((my_numbers + scores)) # [5, 4, 3, 2, 1, 73, 20, 65, 19, 76, 100, 88]
# print(reduce(accumulator, (my_numbers + scores))) #456
# ***************
# ZIP() --> work kind of like a zipper. Takes the same indexed values and create tuples in a list.
# li1 = [1,2,3]
# set1 = {4,5,6}
# tuple1 = (7,8,9)
#
# print(zip(li1, set1, tuple1)) #<zip object at 0x0000019AB1102B40>
# print(list(zip(li1, set1, tuple1)))  # combines the items sequence wise into a sequence of tuples
# # [(1, 4, 7), (2, 5, 8), (3, 6, 9)]
# print(li1, set1, tuple1) # [1, 2, 3] {4, 5, 6} (7, 8, 9)
'''
use the same no.s of items in all the iterables, otherwise it can ruin the sequence.
'''
# Ex:
# my_strings = ['a', 'b', 'c', 'd', 'e']
# my_numbers = [5,4,3,2,1]
#
# print(list(zip(my_strings, sorted(my_numbers))))
# ---------------------------------------
# LAMBDA EXPRESSIONS
#