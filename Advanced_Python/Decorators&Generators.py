# DECORATORS
# In Python, Functions act like variables.
# They can be argument to another function.
# Functions can be assigned to another variable.
# Decorators supercharge our functions, add some extra functionalities to them.
# Remember! Higher Order Function (HOC) is a function which returns another function,
# or accepts another function

# A.
# def hello():
#     print("Hello!")
#
# greet = hello
# del hello => here the function is not deleted, just the keyword, because greet is still pointing
# to the function memory and python has not deleted it

# hello()  # this will give ERROR, because it has been deleted by the keyword
# print(greet) #<function hello at 0x00000223393904A0>
# greet() #Hello!

# B.
# def hello(func):
#     func()

# def greet():
# 	print('still here!')

# a = hello(greet)
# print(a)

# ------EX-1---------
# def my_decorator(func):
#     def wrap_func():
#         print("***********")
#         func()
#         print("***********")
#     return wrap_func
#
# @my_decorator
# def hello():
#     print("Hello!")
#
# hello()
# output ;
# ***********
# Hello!
# ***********
'''
 using decorator is same as doing the below:
my_decorator(hello)()
'''
# -------EX-2------------
# def my_decorator(func):
# 	def wrap_func(*args, **kwargs):
# 		func(*args, **kwargs)
# 	return wrap_func
#
# @my_decorator
# def hello(name, age):
# 	print(f"Hello {name}, your age is {age}.")
#
# @my_decorator
# def logged_in(username):
# 	print(f"{username} is logged in.")
#
# hello("saurabh", 21)
# logged_in("saurabh")

# -------EX-3--------
from time import time

# def performance(fn):
#     def wrap_fn(*args, **kwargs):
#         t1 = time()
#         fn(*args, **kwargs)
#         t2 = time()
#         print(f'It took {t2-t1} sec')
#     return wrap_fn
#
# @performance
# def long_fn():
#     for i in range(10000000):
#         i*5
#
# long_fn()

# EXERCISE
# user1 = {
#     'name': 'Sorna',
#     'valid': False #changing this will either run or not run the message_friends function.
# }
# def authenticated(fn):
#     # code here
#     def wrapper(*args, **kwargs):
#         if args[0]["valid"]:
#             return fn(*args, **kwargs)
#         else:
#             return print("invalid user")
#
#     return wrapper
#
#
# @authenticated
# def message_friends(user):
#     print("message has been sent")
#
# message_friends(user1)

# *******************************
# GENERATORS
# These allow us to generate sequence of values over time.
# range() --> built-in generator function
# range(100) creates items one by one in memeory. But, list(range(100)) creates all in once.
# range is much more performant than list.
# Generator is subset of Iterable.
'''
'yield' pauses the function and comes back to it when we do something to it, which is called 'next'.

if there is the keyword 'yield' written inside the function, then python recognises that its a 
generator function, and won't run the function until the function is being iterated.
'''
# here we are generating our own generator function, just like a range().

# def generator_fn(num):
#     print("check")
#     #yield
#     for i in range(num):
#         print("****")
#         yield i*2
#         print("####")

# -----
# g = generator_fn(3)
# print(g) # <generator object generator_fn at 0x000001C64DD3A6C0>
# print(next(g)) #0
# print(next(g)) #2
# print(next(g)) #4
#print(next(g))  # StopIteration error, because items number exceeded the range
# -----
# for item in generator_fn(5):
# 	print(item)

# here it goes to the generator_fn(), gets the 'i' value, pauses the function,
# until called for the 2nd time, and so on,
# it doesn't store all the no.s in the memory (just the most recent one).

# ------------------------
# Ex-1
#generators are much more performant than lists. (i.e range > list in performance.)
#So generators are really, really useful when calculating large sets of data.

# from time import time
# def performance(fn):
#     def wrapper(*args, **kwargs):
#         t1 = time()
#         result = fn(*args, *kwargs)
#         t2 = time()
#         print(f'took {t2-t1} s')
#         return result
#     return wrapper
#
# @performance
# def long_time():
#     print('1')
#     for i in range(1000000): #it finishes after.
#         i*5
#
# long_time()
# print()
#
# @performance
# def long_time2():
#     print('2')
#     for i in list(range(1000000)): #it took longer.
#         i*5
#
# long_time2()
# print()

# ------------------------
# Under-The-Hood-Of-Generators
# iter() --> Get an iterator from an object

# def special_for(iterable):
#   iterator = iter(iterable)
#   while True:
#     try:
#       iterator*5
#       next(iterator)
#       print(iterator)
# 		print(next(iterator))
#     except StopIteration:
#       break

# special_for([1,2,3])
# ************
# class MyGen:
#   current = 0
#   def __init__(self, first, last):
#     self.first = first
#     self.last = last
#     MyGen.current = self.first #this line allows us to use the current number as the starting point for the iteration
#
#   def __iter__(self):
#     return self
#   def __next__(self):
#     if MyGen.current < self.last:
#       num = MyGen.current
#       MyGen.current += 1
#       return num
#     raise StopIteration
'''
loops by default deal with StopIteration error. they have build in functionality to handle them.
'''
# gen = MyGen(1,100)
# for i in gen:
#     print(i)

# ********************
# Exercise
# Fibonacci-LIST (iterable)
# def fib(num):
#     a = 0
#     b= 1
#     li=[]
#     for i in range(num):
#         li.append(a)
#         temp = a
#         a = b
#         b = temp + b
#     print(li)
#
# num = int(input("Enter a number: "))
# fib(num)

# Fibonacci-RANGE (generator)
# def fib(num):
#     a = 0
#     b= 1
#     for i in range(num):
#         yield a
#         temp = a
#         a = b
#         b = temp + b
#
# num = int(input("Enter a number: "))
#
# for i in fib(num):
#     print(i)