#1.Fundamental Data Types
#int, float, bool, str, list, tuple , set , dict , complex - None

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

# Strings
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

# Booleans
# bool => True/False
# is_cool = False
# print(bool(1)) => True

# Lists => ordered sequence of object that can be of any type
# li = [1,'asd', 12.3, True , [1,24]]
# amazon_cart = ['notebooks', 'sunglasses']









