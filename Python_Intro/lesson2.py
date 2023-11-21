#  print , type, dir , len, help => playground için bilinmelidir
# ! bool, int, float, str, list, dict, tuple , set

first_name = "yasin"
last_name="sutoglu"
age = input("yasinizi giriniz:  ")

print(type(age))

if age.isdigit():  
    print(int(age))

# ? tam bolme , mod alma
19 // 10
19 % 10

#? divmod
divmod(19,10)
print(divmod(-19,10))

#? arttırma / azaltma /çarpma /bolme
# age = age + 1
# age +=1
# age-=2
# age*=10
# age/=10

#? square
# age ** 2

#? operatorler
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