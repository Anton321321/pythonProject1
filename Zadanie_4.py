str='Enjoy every moment'
d={}
for i in range(len(str)):
    if str[i]==' ':
        continue
    counter=0
    temp_i=i
    for i in range(len(str)):
        if str[temp_i]==str[i]:
            counter=counter+1
    i=temp_i
    d[str[i]]=counter
print(d)