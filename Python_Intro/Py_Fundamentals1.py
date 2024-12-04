#1.Fundamental Data Types
#int, float, bool, str, list, tuple , set , dict , complex - None(Null in other langs)

#2.Classes => custom types

#3.Specialized Data Types => special packages, modules
# Commenting => ctrl + /

# Math Functions => round, abs log10, exp, pow , sqrt ,
# factorial, ceil, floor, fmod , bin() => binary conversion ... etc.

# print(type(pow(10,2)))
# print(bin(12)) => 0b1100
# print(int('0b1100', 2)) => binary to decimal conversion

#operator precedence => (), **, * / , + -

# Variable Rules
# 1. snake_case
# 2. start with lowercase or underscore
# 3. letters, numbers,underscores
# 4. Case Sensitive
# 5. don't overwrite keywords(int, and, yield, finally, lambda, print, etc...)
# _varname => private variable name
# __ => dunder; In the form of "__name" variables must not be composed.
# a,b,c = 12,34,87 => OK

# Constants => all in capital letters , can't be changed
# PI = 3.14

# Expressions VS Statements
# Expression => piece of code produces a value => (person_length / 12)
# Statement => It is an entire line of code performs some sort of action => (per_len =
# person_length / 12)

# Augmented Assignment Operator
# some_value = 5  => some_value += 2 (+=, -=, *= ...)

# STRINGS
# type('asdaksfjafa') => str
# type("sdaksfjafa") => str
# docString(long_string) => """......""" => (multiple lines)
# print('jess' + 'foster') => concatination
# str(100); int('15'); float(12) => type conversion

# Formatted Strings (JS => template literals)
# name,age = 'Jess' , 55
# print(f'Hi {name}. You are {age} years old') => PYTHON3
# print('Hi {}. You are {} years old'.format(name, age)) => PYTHON2

#String Indexes
# 'me me me'
# -01234567-
# selfish = 'me me me'
# print(selfish[0]) => 'm'
# print(selfish[-1]) => 'e'
# [start:stop:stepover] => selfish[0:8:2] :string_slicing
# Ex: print(selfish[::-1]) => reverse string
# selfish[0] = '8' => ERROR. Because, strings are immutable. But, reassign is OK.

#Escape Sequence
# ('\' + 'char'): \t , \n ...
# weather = 'It\'s sunny'

# Built-In Functions+Methods
# int(), str(), print(), etc... => built-in function examples
# len('asdafas') => length of str
# String Methods => '...'.upper() ; '....'.capitalize() ;  etc...
# quote = 'to be or not to be'
# print(quote.find('be')) => 3

# BOOLEANS
# bool => True/False
# is_cool = False
# print(bool(1)) => True

#LISTS (arrays in other programming langs)
# Lists => ordered sequence of object that can be of any type
# Lists are mutable apart from strings.
# amazon_cart[0] = 'laptop' => OK
# li = [1,'asd', 12.3, True , [1,24]]
# amazon_cart = ['notebooks', 'sunglasses','toys','grapes']

#List slicing => make new copy of list, doesn't change original list.
# amazon_cart[0::2]

# amazon_cart = ['notebooks', 'sunglasses','toys','grapes']
# new_cart = amazon_cart =>  (shallow copy)
# new_cart = amazon_cart[:] =>  (deep copy)
# new_cart = amazon_cart.copy() => (deep copy)
# new_cart[0] = 'gum'
# print(new_cart)
# print(amazon_cart)

# Matrix (multidimensional List)
# matrix = [[...],[...],[...]]
# a = matrix[0][1]

#List Methods
# len(list) , append(obj), insert(index, obj),extend(), clear(), ...
# amazon_cart.append('ball') => append() => changes the original list
# amazon_cart.extend([100,122])
# amazon_cart.pop()
# Also, you can use as => pop(index) => poped value can be caught by assigning
# amazon_cart.remove(value)
# amazon_cart.index(value,start,stop)
# print(100 in amazon_cart) => True
# amazon_cart.count(value)
# amazon_cart.sort() == sorted(amazon_cart) ; -> default asc
# sorted() -> doesn't modify the original list
# amazon_cart.reverse() == amazon_cart[::-1]
# print(list(range(start,end)))
# list(range(2,7)) => [2,3,4,5,6]
# sentence.join(iterable)
# sentence = ' '
# sentence.join(['hi', 'my', 'name', 'is', 'jess'])

# List Unpacking (Destructuring)
# a, b, c , *others , d= [1,2,3, 4, 5, 6, 7]
# print(a) , print(b), print(c) , print(others) , print(d)

# DICTIONARY
# python 3.7+ => https://medium.com/junior-dev/python-dictionaries-are-ordered-now-but-how-and-why-5d5a40ee327f
# Unordered KEY(any immutable type(even tuple) generally string) - VALUE pair
# Key has to be unique
# Hash Table/Map(in other langs)
# Both DataType and DataStructure(a way of organizing datatype)
# dictionary = {'a':[1,33] , 'b':'hello', 'x':3 , 'd': True}
# print(dictionary['a'][1]) -> 33

# my_list = [
# {'a':[1,33] , 'b':'hello', 'x':3 , 'd': True} ,
# {'a':[3,44] , 'b':'hello', 'x':3 , 'd': True}
# ]
#print(my_list[1]['a'][0]) => 3

# Dictionary Methods
# user = { 'basket':[1,2,3] , 'greet': 'hello' , 'my_age': 20 }
# print(user.get('age')) --> None
# print(user.get('age',55)) --> 55
# print(user.get('my_age',55)) --> 20
# print('basket' in user) --> True
# print('greet' in user.keys()) --> True
# print('hello' in user.values()) --> True
# print(user.items()) --> items:keys+values are shown in Tuples covered by List;
# [ (...,...) , (...,...) , ]
# dict(key=value) ---> defining new dictionary
# user2 = dict(name='Jess')
# user2.clear()
# user3 = user.copy() ---> deep copy
# print(user.pop('my_age')) --> 20
# print(user.popitem()) --> ('my_age',20)
# user.update({'greet':'hiii!'}) --> if the key doesnt exist, update() will add it on dictionary


#TUPLES
# Similar to lists but, we can not modify them. (Immutable Lists)
# more organized and predictable, safer ,faster than Lists
# Less flexible than Lists
# No sort, reverse
# my_tuple = (1,2,3,4,5)
# my_tuple[1] = 'z' --> ERROR
# print(my_tuple[1]) --> 2
# print(5 in my_tuple) --> True
# new_tuple = my_tuple[2:4] ---> slicing
# x,y,z,*other = (1,2,3,4,5,6) ---> Destruct; other-> [4,5,6] :LIST
# Tuple Methods => count(), index()
# print(len(my_tuple)) --> 5

# SETS (kümeler)
# Unordered collections of unique objects - there is no duplicates
# Doesn't support indexing
# my_set={1,2,3,4,5}
# print(my_set[0]) --> ERROR
# print(5 in my_set) --> True
# print(len(my_set)) --> 5
# print(list(my_set)) --> [1,2,3,4,5]
# my_set.add(100) --> OK
# my_list = [1,2,3,4,5,5,5]
# print(set(my_list)) --> {1,2,3,4,5}
# new_set = my_set.copy() ---> deep copy
# my_set.clear()
# print(new_set) ---> {1,2,3,4,5}
# print(my_set) ---> set()

# Sets Methods
# .difference(), .discard(), .difference_update(), .intersection() == &,
# .isdisjoint(), .isubset(), .issuperset(), .union() == |
# print(my_set.union(your_set)) == print(my_set | your_set)
# print(my_set.intersection(your_set)) == print(my_set & your_set)
# https://www.w3schools.com/python/python_ref_set.asp












