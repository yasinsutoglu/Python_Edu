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
# ---------------------------------------
# https://pypi.org/ => python package index - open source libs developed by other developers