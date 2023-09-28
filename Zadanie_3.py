elem=[]
length=int(input("Введите длину одномерного целочисленного списка: "))
for i in range(length):
    value=int(input("Введите элемент списка: "))
    elem.append(value)
min=elem[0]
print("Список:")
print(elem)
counter=0
for i in range(length):
    if elem[i]%2!=0:
        if counter==0:
            max=elem[i]
            counter = counter + 1
        if elem[i]>max:
            max=elem[i]
    if abs(elem[i])<min:
        min=elem[i]
if counter==0:
    print("Нет нечетных элементов")
else:
    print("Макс. нечет. эл. = ",max)
print("Мин. по модулю эл. = ",min)





