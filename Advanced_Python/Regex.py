#([A-Za-z0-9$%#@]{7,}[0-9]) --> password validation regex
import re

string = "this is a really cool string really!"

a = re.search('really',string)
print(a)

# the below 4 commands will give error if the searching string does not exist.
print(a.span())
print(a.start())
print(a.end())
print(a.group())

pattern = re.compile('really')

b = pattern.search(string)
c = pattern.findall(string)

pattern = re.compile('this is a really cool string really!')
d = pattern.fullmatch('this is a really cool string really!')
e = pattern.fullmatch('hello this is a really cool string really!')
# this should be exact match, otherwise returns none

pattern = re.compile('really')
f = pattern.match('really cool feature')
# it starts matching from the first character otherwise returns none
g = pattern.match('yo really')

print(f"b: {b}")
print(f"c: {c}")
print(f"d: {d}")
print(f"e: {e}")
print(f"f: {f}")
print(f"g: {g}")

# ------------EMAIL-PASSWORD-REGEX---------------
# import re

email_pattern = re.compile(r"([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
check_email = email_pattern.fullmatch('saurabh_1089@gmail.com')

password_patter = re.compile(r"([a-zA-Z0-9@#$%]{8,}$)")
check_password = password_patter.fullmatch('12345678')

if check_email and check_password:
    print("Both email and password are correct.")
else:
    print("Try again.")

'''
password is also checking for minimum 8 chars
'''