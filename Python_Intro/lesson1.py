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

#terminalde =>  python lesson1.py

#int , bool , string, float
x=1

proper_value = 12

camelCase = 'yaso' # camelCase kullanılamıyor pythonda
SERVER_API = "127.0.0.1" # pascal case constant için değişmeyecekler için

unit_price = 2.39 #float
is_published = False #boolean
is_publishedMi = True #boolean
course_my = "aaaaa"
full_name = "{} {}".format(unit_price , course_my) #format yöntemi
print(full_name)
print("Merhaba %s, bugun haftanin %d. gunu" %(full_name, unit_price))#veri biliminde kullanırken cok karsılasılıyor
print("Merhaba %s, bugun haftanin %f. gunu" %(full_name, unit_price))

print("*" * 30)

#Indeksleme
course_name = 'Python Programming' # 9,223,372,036,854,775,758 characters => string limit
print(course_name[0:3]) #Pyt
print(course_name[-1]) #g
print(course_name[-5:])

# title() => her kelimenin ilk harfi büyük , capitalize() => string ifadenin ilk harfi büyük



