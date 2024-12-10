# MODULES
# While project is getting bigger and bigger, we need to link files together.
# Each of .py files is module. In these files, we can create different classes, functions etc.
# So, we use "import ... from ...."  format.
# .pyc (cachepython)--> compiled python file

# PACKAGES
# It is a folder in the project.
# Include multiple modules inside it.
# ------------------
# import utilities  # file completely imported
# print(utilities.mult(2,7))
# print(utilities.divide(2,7))
#
# import shopping.shopping_cart
# print(shopping.shopping_cart.buy('shoe'))

# ------------------------------------------
# from utilities import *  # all includings of the file imported
# from Python_Edu.Modules.shopping import shopping_cart
#
# # print(utilities)    # gives error
# print(mult(4,10))
# print(divide(52,3))
#
# # print(shopping)    # gives error
# print(shopping_cart)
# print(shopping_cart.buy('banana'))

# ------------------------------------------
from utilities import mult, divide , jas1
from Python_Edu.Modules.shopping.shopping_cart import buy
# Below 2 lines are the output of imported modules "print(__name__)" :
# utilities
# Python_Edu.Modules.shopping.shopping_cart

# print(utilities)  # gives error
print(mult)

print(mult(44,5))
print(divide(115,3))

# print(shopping)  # gives error
# print(shopping.shopping_cart)  # gives error
print(buy('apple'))
#-------------------
# print(__name__) => '__main__'
# If we rename this file, we get the same print output anyway.

# EX:
# if __name__ == '__main__':
# 	print('Main module is running now...')
#--------------------------------
# class Student():
# 	pass
#
# st1 = Student()
# print(type(st1)) # <class '__main__.Student'>
# print(type(jas1)) # <class 'utilities.Jason'>