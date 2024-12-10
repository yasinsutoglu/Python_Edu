# In other languages, these might be called "Standard Libraries".
# We import and use them.
# https://docs.python.org/3/py-modindex.html
# When we install python, these automatically comes as standard. We can access freely.

import random
import email as my_email_module

print(random) # <module 'random' from 'C:\\Users\\ASUS\\anaconda3\\Lib\\random.py'>
# help(email) # shows the all documentation of built-in module
print(dir(random)) # shows the available all methods of this module
# ['BPF', 'LOG4', 'NV_MAGICCONST', 'RECIP_BPF', 'Random', 'SG_MAGICCONST', 'SystemRandom',
#  'TWOPI', '_ONE', '_Sequence', '_Set', '__all__', '__builtins__', '__cached__', '__doc__',
#  '__file__', '__loader__', '__name__', '__package__', '__spec__', '_accumulate', '_acos',
#  '_bisect', '_ceil', '_cos', '_e', '_exp', '_floor', '_index', '_inst', '_isfinite', '_log',
#  '_os', '_pi', '_random', '_repeat', '_sha512', '_sin', '_sqrt', '_test', '_test_generator',
#  '_urandom', '_warn', 'betavariate', 'choice', 'choices', 'expovariate', 'gammavariate',
#  'gauss', 'getrandbits', 'getstate', 'lognormvariate', 'normalvariate', 'paretovariate',
#  'randbytes', 'randint', 'random', 'randrange', 'sample', 'seed', 'setstate', 'shuffle',
#  'triangular', 'uniform', 'vonmisesvariate', 'weibullvariate']

print(random.randint(1,10))
print(random.random())
print(random.choice([1,44,6,898,12]))
my_list = [1,44,6,898,12]
random.shuffle(my_list) # pick with mouse + press 'F1' =>  shows the method details
print(my_list) #[12, 6, 1, 44, 898]

print(my_email_module.message_from_string('ss'))
# ------------------------
import sys

# terminal_arg_1 = sys.argv[1]
# terminal_arg_2 = sys.argv[2]
# we can add environment arguments while running a py file from terminal.
# So, "sys.argv" => makes these arguments reachable to us.

#EX
# import sys
# from random import randint
#
# first = sys.argv[1]
# last = sys.argv[2]
#
# random_num = randint(int(first), int(last))
#
# while True:
#     user_guess = int(input("Guess the random no.: "))
#     if user_guess == random_num:
#         print("Congratulations, You WON!!")
#         break
#     else:
#         print("You Lose! Guess again....")

# ------------------ PYPI ~~ (NPM) ---------------------
# https://pypi.org/ => python package index - open source libs developed by other developers
# After installing the pip, we can install any package by the command "pip/pip3 install ....." ;
# "pip3 uninstall ....";
# "pip list" (in terminal) --> show the all packages we have currently.

# ------------ VIRTUAL ENVIRONMENTS ---------
# Version Detail => 3.5.8 -> 3: major changes, 5: after adding modules, 8: bug-fix & minor changes
# pipenv --> it is useful to use "pip" for different projects. Because we may need same packages
# but in different version for the separated projects.
# "venv" Folder is virtual env created by python. While creating a new project, select "Virtualenv".
# After projects having been created like this, they don't affect each other using the different
# versions of the same packages.

# ------------ USEFUL MODULES ---------
# collections ,

from collections import Counter,defaultdict, OrderedDict

# li = [1,2,3,4,5,6,7,7]
# sentence = 'blah blah blah think about python'
# print(Counter(li)) # Counter({7: 2, 1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1})
# print(Counter(sentence)) # Counter({'h': 5, ' ': 5, 'b': 4, 'a': 4, 'l': 3, 't': 3, 'n': 2, 'o': 2,
## 'i': 1, 'k': 1, 'u': 1, 'p': 1, 'y': 1})
# count the no. of occurence of each iterable, and store them in a dict format,
# with highest count to lowest count order
# ----------------------------------------

#my_dict2 = {'a': 1, 'b': 2}
# print(my_dict2['c'])     # this gives error

# my_dict = defaultdict(lambda: 'enter_default_value_here',{'a':1, 'b':2})
# print(my_dict['c']) #enter_default_value_here
# print(my_dict['a']) #1
# defaultdict takes the first argument as a callable object (it is a function that can be called)
# ----------------------------------------

# d = dict()
# d['a'] = 4
# d['b'] = 45
#
# d2 = dict()
# d2['b'] = 45
# d2['a'] = 4
#
# d3 = dict()
# d3['b'] = 45
# d3['a'] = 4
#
# print(d == d2)      # Order doesn't matter here
# print(d2 == d3)
#
# dict1 = OrderedDict()
# dict1['a'] = 4
# dict1['b'] = 45
#
# dict2 = OrderedDict()
# dict2['b'] = 45
# dict2['a'] = 4
#
# dict3 = OrderedDict()
# dict3['b'] = 45
# dict3['a'] = 4
#
# print(dict1 == dict2)   # different order, hence False
# print(dict2 == dict3)   # same order, hence True

# *****************************
import datetime
from time import time
from array import array

print(datetime.time())
# print(datetime.time(55,45,2))   # hour must be between 0 to 23
print(datetime.time(5,45,2))

print(datetime.date.today()) #2024-12-10

print(time())   # time in unix code

arr = array('i', [1,2,3])
print(arr)
print(arr[0])
'''
# array in python are faster than list, and takes less memory.
# the first argument is the 'typecode'
'f' = float (4 byte)
'd' = double (8 byte)
'b' = signed char (1 byte)
'i' = signed int (2 byte)
'l' = signed long (4 byte)
etc.
'''