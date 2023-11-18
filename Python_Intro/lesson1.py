print("hello")
print(2+2) #comment
print("""nabiyon lan docString bu""")

name = str(input())
age = int(input())
print('Hi,{name}, you are {age}.') #template literal

""" MULTILINE COMMENT -
"Hi {}, you are {}".format(name, age)
 "Hi {name}, you are {age}".format(name=name, age=age)
 "Hi %s, you are %d" % (name, age)
 """
 
""" Farklı type'larda oto string concatination pythonda yok typecasting yada template literal kullanırız"""

""" dir=> tüm methodları göstermek için kullanılır."""

email= "yasin@gmail.com"
print(email[::-1]) #stringi tersten yazdırma
print(email[3:])
print(email[::2])

number = "1234"
print(number.lower())
print(number.islower())
print(number.isnumeric())

first_name = "yasin"
last_name = "sutoglu"
age = 19
# fstring diye geçiyor js template literal ile aynı
full_name = f"{first_name} {last_name} {age} yasindadir. Seneye {age + 1} yasinda olacaktir."
print(full_name)