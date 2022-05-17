# 럭키 스트레이트 
from time import time

def sum_part(x):
    sum = 0
    while(x>0):
        sum += x%10
        x = x/10
    return int(sum)


num = input()
start_time = time()
slicing = len(num)//2

first_part = int(num[:slicing])
second_part = int(num[slicing:])

if(sum_part(first_part)==sum_part(second_part)):
    print("LUCKY")
else:
    print("READY")

end_time = time()
range = end_time - start_time
print(range)