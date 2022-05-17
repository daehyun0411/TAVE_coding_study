x = input()
list1 = []
list2 = []
total = 0
for i in x:
    if(i >= '0' and i <= '9'): #숫자
        list1.append(i)
    else:
        list2.append(i) #문자
for i in list1:
    total += int(i) 
list2.sort()
list2.append(str(total))
print(''.join(list2))
