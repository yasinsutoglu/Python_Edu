# DEBUGGING
# Useful Advices:
# 1. Use Linting
# 2. Use IDE/Editor
# 3. Learn to Read Errors (EOL:endofline)
# 4. Use pdb:python_debugger (built-in module) - you can use pycharm pdb buttons at the top-right

'''
Some useful commands for pdb:
a : Print the argument list of the current function.
step: to run the current line of code, and stop at the first possible occasion
help: to list all the commands available
help <command>: to see what a command does
continue: to continue the program till the error comes
w: previous line, current line and next line content
next: Continue execution until the next line in the current function is reached or it returns.

We can change the variables value in the console window as well.
we can type in the variable name to get its value
'''

import pdb
def add(n1, n2):
    pdb.set_trace()  # flow of the program paused at this point. From consele, you can test
    # anything what you want in the name of debugging. Use "exit" to quit from pdb console mode.
    return n1+n2

add(4, 'five')