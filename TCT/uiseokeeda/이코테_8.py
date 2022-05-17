# 문자열 재정렬
from time import time

input_str = input()
start_time = time()

num_list = ['1','2','3','4','5','6','7','8','9']
str_list = []
sum = 0

for i in range(len(input_str)):
    if(input_str[i] in num_list):
        sum += int(input_str[i])
    else:
        str_list.append(input_str[i])

str_list.sort()

new_str = ""
for i in str_list:
    new_str+=i

print(new_str + str(sum))

end_time = time()
range = end_time - start_time
print(range)

