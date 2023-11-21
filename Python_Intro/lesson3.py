#LESSON3
#! Listeler - (Array gibi)
user_info = ["Yasin" , "Sutoglu" , 19 , "male", "Python" , "F1"]
print(user_info[0].upper())

print(type(user_info[1]) == str and user_info[3].upper()) # JS'teki "&&"" shortcut operatoru ile aynı
print(user_info.index("Sutoglu"))
print(user_info[0:3])
print(user_info[4:3]) # sacmalik
print(user_info[-1]) # en sondaki eleman
print(user_info[len(user_info) - 1])

#dir(user_info)
#? doubleUnder (__) => "dunder" deniyormus

if not 1 + 1 == 3: 
    print("Hello")
    
items = [10 , 20 ,30 , 40 , 50 , 60 , 70 , 80 , 90 , 100]
print(items[::2]) # cıktı => [10, 30, 50, 70, 90]
print(items[1::2]) # cıktı => [20, 40, 60, 80, 100]
print(items[::-1]) # tersten yazdir
items.reverse() # tersten yazdirip sonra items'a assign etti
print(items) 

items.append(110)
items.insert(3,5) #3. eleman yerine 5 sayısını ekle
print(items)  # cıktı => [100, 90, 80, 5, 70, 60, 50, 40, 30, 20, 10, 110]
items.insert(len(items)//2 , 550)
print(items)
items[3] = "yasin"
print(items) # ? cıktı => [100, 90, 80, 'yasin', 70, 60, 550, 50, 40, 30, 20, 10, 110]
items[items.index(550)] +=10
print(items)

pop_item = items.pop() #sondakini atar
print(pop_item) # cıktı => 110
#! reverse(), append() , insert() , pop() etc =>  transformative list methods

new_items = items #shallow copy JS gibi id(items) = id(new_items) durumu var, aynı şey tuple'da ve dict'de de var
items.pop()
print(items) # [100, 90, 80, 'yasin', 70, 60, 560, 50, 40, 30, 20]
print(new_items) # [100, 90, 80, 'yasin', 70, 60, 560, 50, 40, 30, 20]

mm_items = items.copy()
mm_items[3] = 15
print(items)  
print(mm_items)
del mm_items[0] # pop gibi değil direkt siler

# for item in range(0,10): # 10 dahil değil
#     print(item)


for index in range(len(mm_items)): 
    # print(index)
    print(mm_items[index] * 1.1)