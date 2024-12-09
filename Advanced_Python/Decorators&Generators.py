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