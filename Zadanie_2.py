s = input("Введите строку: ")
temp_i = -1
length = 0
for i in range(len(s)):
    counter = 0
    if length == 1:
        temp_i = i - 1
    if s[i].isdigit() == True:
        length = length + 1
        counter = counter + 1
        if len(s) == i + 1:
            counter = 0
    if counter == 0:
        if temp_i != -1:
            print(s[temp_i:temp_i + length])
            temp_i = -1
        length = 0
