#([A-Za-z0-9$%#@]{7,}[0-9]) --> password validation regex
import re

my_string = "this is a really cool string really!"

a = re.search('really',my_string)
print(a) # <re.Match object; span=(10, 16), match='really'>

# the below 4 commands will give error if the searching string does not exist.
print(a.span()) # (10, 16)
print(a.start()) # 10
print(a.end()) # 16
print(a.group()) # really
# group() is used for multiple search in one line.

# ---pattern----
pattern = re.compile('really')
b = pattern.search(my_string)
print(f"b: {b}") # b: <re.Match object; span=(10, 16), match='really'>
c = pattern.findall(my_string)
print(f"c: {c}")  # c: ['really', 'really']

pattern = re.compile('this is a really cool string really!')
d = pattern.fullmatch('this is a really cool string really!')
print(f"d: {d}") # d: <re.Match object; span=(0, 36), match='this is a really cool string really!'>
e = pattern.fullmatch('hello this is a really cool string really!') # e: None
print(f"e: {e}")
# this should be exact match, otherwise returns none

pattern = re.compile('really')
f = pattern.match('really cool feature')
print(f"f: {f}") # f: <re.Match object; span=(0, 6), match='really'>
# it starts matching from the first character otherwise returns none
g = pattern.match('yo really')
print(f"g: {g}") # g: None

# ------------EMAIL-PASSWORD-REGEX---------------
# import re
email_pattern = re.compile(r"([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
check_email = email_pattern.fullmatch('saurabh_1089@gmail.com')

password_pattern = re.compile(r"([a-zA-Z0-9@#$%]{8,}$)")
check_password = password_pattern.fullmatch('12345678')

if check_email and check_password:
    print("Both email and password are correct.")
else:
    print("Try again.")

'''
password is also checking for minimum 8 chars
'''