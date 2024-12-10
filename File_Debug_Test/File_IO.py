# Read_Write_Append File Issues
'''
mode = 'w' : it creates a new file and write into it. If there is an exiting file with the same name, it replaces it.
mode = 'r' : it is used to read the file
mode = 'r+' : it is used to read and write into the file. but it writes from position 0, which might replace some existing text.
mode = 'a' : it appends to the existing file. meaning writing to the file keeping the old content intact.
             if the file doesn't exist, it creates a new one.

if we don't mention the mode, by default it will be considered 'r' mode.

with 'with' we don't need to close the file manually.
'''
# --------Reading File-------------
my_file = open('test.txt')
#print(my_file) # <_io.TextIOWrapper name='test.txt' mode='r' encoding='cp1254'>
print(my_file.read())

print(my_file.read())   # it won't be printing anything.
# because the cursor is at the end of the file.

print("Seek0-1")
my_file.seek(0)     # we reset the cursor to the initial position
print(my_file.read())   # and so we can now read the file from the initial position till end

print("Seek0-2")
my_file.seek(0)

print(my_file.readline())   # reads a line and stop the cursor
print(my_file.readline())
print(my_file.readline())
print(my_file.readline())

print("Seek0-3")
my_file.seek(0)

print(my_file.readlines()) # store all the lines in a list
#[ 'hello there....\n', 'how are you?\n', 'hope you are doing well.']
print(my_file.readlines()) #[]

my_file.close()

# -----------------------------------
with open("happy\happy.txt", mode='a') as my_file:
	text = my_file.write("I am HAPPY!")
	print(text)  # it prints the no. of letters written into the file

with open("happy\happy.txt", mode='r') as my_file:
	print(my_file.read())

'''
we can give absolute path or related path (wrt to the current folder)
../ means go back one folder
./ menas start from current folder

pathlib module: for windows, linex paths are different, so we can use this module 
so that our code works in all machines.
'''
with open(".\happy\happy.txt", mode='a') as my_file:
	text = my_file.write("I am HAPPY!")
	print(text)  # it prints the no. of letters written into the file

with open("D:\\MIUUL_AI\\Repos\\Python_Edu\\File_Debug_Test\\happy\\happy.txt",
          mode='r') as my_file:
	print(my_file.read())

# ----------TRANSLATOR------------
from translate import Translator

with open('.\\translate.txt', mode = 'r') as my_file:
    text = my_file.read()

translator= Translator(to_lang="es")
translation = translator.translate(text)

print(translation)

# -----FILE_IO ERRORS----------
try:
	with open(".\happy\h.txt", mode='r') as jess_file:
		print(jess_file.read())
except FileNotFoundError as err1:
	print('file does not exist')
	# raise err
except IOError as err2:
	print('IO Error')
	raise err2