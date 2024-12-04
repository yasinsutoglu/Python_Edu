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

#terminalde =>  python extraNotes2.py

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

#  print , type, dir , len, help => playground için bilinmelidir
# ! bool, int, float, str, list, dict, tuple , set

first_name = "yasin"
last_name="sutoglu"
age = input("yasinizi giriniz:  ")

print(type(age))

if age.isdigit():
    print(int(age))

# ? tam bolme , mod alma
# 19 // 10
# 19 % 10

#? divmod
# divmod(19,10)
# print(divmod(-19,10))

#? arttırma / azaltma /çarpma /bolme
# age = age + 1
# age +=1
# age-=2
# age*=10
# age/=10

#? square
# age ** 2

#? boolean operatorler
# > , < , >= , <= , == , and , or , not , !=, is , is not , in , not in

# x **= 3 ==> x = x ** 3
# x ^= 3 ==> x = x ^ 3
# x >>= 3 ;	x = x >> 3
# x <<= 3 ;	x = x << 3
# not(x < 5 and x < 10)

# NA ==> None

# "" or "None" ==> "None" gelir
# "" and "None" ==> "" gelir

# ? Bool İşlemleri
# bool(0) => false
# bool("") => false
# bool(0 == 0) => True
# bool(None) => False
# bool(None == 0) => False
# bool(None == None) => True
# type(age) == int

#  not type(age) == int
#* 100 > age > 0 ==> age < 100 and age > 0

# ! Conditional
gender = "M"

if type(age) == int or type(age) == float or age.isdigit():
    if(age>=18 and gender == "M") or (gender == "F"):
        print("iceri girebilir")
    elif(age >= 16):
        print(f"{18-age} sene kaldı")
    else:
        print("sakjakjshflaskdşa")
else:
    print("Dogru bilgi vermedin sorry")

# ! Listeler - (Array gibi)
user_info = ["Yasin", "Sutoglu", 19, "male", "Python", "F1"]
print(user_info[0].upper())

print(
	type(user_info[1]) == str and user_info[3].upper())  # JS'teki "&&"" shortcut operatoru ile aynı
print(user_info.index("Sutoglu"))
print(user_info[0:3])
print(user_info[4:3])  # sacmalik
print(user_info[-1])  # en sondaki eleman
print(user_info[len(user_info) - 1])

# dir(user_info)
# ? doubleUnder (__) => "dunder" deniyormus

# if not 1 + 1 == 3:
#     print("Hello")

items = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print(items[::2])  # cıktı => [10, 30, 50, 70, 90]
print(items[1::2])  # cıktı => [20, 40, 60, 80, 100]
print(items[::-1])  # tersten yazdir
items.reverse()  # tersten yazdirip sonra items'a assign etti
print(items)

items.append(110)
items.insert(3, 5)  # 3. eleman yerine 5 sayısını ekle
print(items)  # cıktı => [100, 90, 80, 5, 70, 60, 50, 40, 30, 20, 10, 110]
items.insert(len(items) // 2, 550)
print(items)
items[3] = "yasin"
print(items)  # ? cıktı => [100, 90, 80, 'yasin', 70, 60, 550, 50, 40, 30, 20, 10, 110]
items[items.index(550)] += 10
print(items)

pop_item = items.pop()  # sondakini atar
print(pop_item)  # cıktı => 110
# ! reverse(), append() , insert() , pop() etc =>  transformative list methods

new_items = items  # shallow copy JS gibi id(items) = id(new_items) durumu var, aynı şey tuple'da ve dict'de de var
items.pop()
print(items)  # [100, 90, 80, 'yasin', 70, 60, 560, 50, 40, 30, 20]
print(new_items)  # [100, 90, 80, 'yasin', 70, 60, 560, 50, 40, 30, 20]

mm_items = items.copy()
mm_items[3] = 15
print(items)
print(mm_items)
del mm_items[0]  # pop gibi değil direkt siler

# 10 dahil değil
# ! for item in range(0,10):
#     print(item)


for index in range(len(mm_items)):
	# print(index)
	print(mm_items[index] * 1.1)

print(10 * "*")

for data in items:
	print(data)

print(10 * "*")

for index in range(10, 50, 5):  # 10 - 50 arası 5'er basamakla gitti
	print(index)

yasin_items = []
for data in mm_items:
	data += 20
	yasin_items.append(data)

# ! tuple'laştırma
for data in enumerate(mm_items):
	print(data)

# (0, 90)
# (1, 80)
# (2, 15)
# (3, 70)
# (4, 60)
# (5, 560)
# (6, 50)
# (7, 40)
# (8, 30)
# (9, 20)

for data in enumerate(mm_items):
	print(data[0])  # index bilgisi
	print(data[1])  # içeriğin(veri) kendi bilgisi

# ? items[data[0]] = data[1] + 20
# !destruct1(unpacking)
user = ["Yasin", "Sutoglu"]

first_name, last_name = user

print(first_name, last_name)
# !destruct2(unpacking)
user_info2 = ["Yasin", "Sutoglu", 19, "male", "Python", "F1"]

fst_name, lst_name, *others = user_info2

print(fst_name, lst_name, others)

# !destruct in list and tuple
for index, info in enumerate(mm_items):
	if 70 > info > 50:
		mm_items[index] = info + 20
		print(index, info)

print(mm_items)