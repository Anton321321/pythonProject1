ch = 2
counter = 0
while counter != 1001:
    counter_test = 0
    i = 2
    while i <= ch / 2:
        if ch % i == 0:
            counter_test = counter_test + 1;
        i = i + 1
    if counter_test == 0:
        counter = counter + 1;
    if counter == 1001:
        print("1001-ое простое число:", ch)
        break
    ch = ch + 1
