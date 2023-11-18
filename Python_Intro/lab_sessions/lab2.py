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



