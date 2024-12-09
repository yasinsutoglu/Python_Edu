# ERR_Handling-1
# Error types => ValueError, SyntaxError, NameError, ZeroDivisionError, TypeError,
# IndexError, KeyError etc...
# https://docs.python.org/3/library/exceptions.html (BUILT-IN Exceptions)

# EX-1;
# while True:
# 	try:
# 		age = int(input("Enter your age: "))
# 		age_in_dogs_year = 10 / age
#
#   except: # --> only except contains any ErrorType!!
#       #...codes
#
# 	except ZeroDivisionError:
# 		print("enter age greater than 0")
# 		continue
#
# 	except ValueError:
# 		print("Please enter a no.")
# 		break
#
# 	except TypeError:
# 		print("!!!!")
#       break
#
# 	else: # else--> If there is no error in try-block, DO this code block!!!
# 		print(f"thank you, and your age is {age}")
# 		break
#
# 	finally: # Always do this at the end of the program, in any case!!
# 		print("I will always get printed no matter what :)")
#
# 	print("can you hear me??????") -> this hasn't been printed!
'''-----------------------------'''
# EX-2;
# def division_fn(num1, num2):
#     try:
#         return num1/num2
#     except (ZeroDivisionError, TypeError) as err:
#         print(f'error: {err}')
#
# division_fn(1,'0') # error: unsupported operand type(s) for /: 'int' and 'str'
# division_fn(1,0) # error: division by zero
# print(division_fn(1,4)) # 0.25

# -----------RAISE AN ERROR----------
# we can stop the program by raising our own errors. It's useful while creating your own lib.

# Ex-1
# print("Hello!!!!")

# raise TypeError("yo")
# raise Exception("Any message!!")

# print("bye")

# Ex-2
# try:
#     age = int(input("age: "))
#     age = 10/age
#     raise ValueError("Ending the program")
#     # raise Exception("quit")
#
# except ValueError:
#     print("Please enter a no.")