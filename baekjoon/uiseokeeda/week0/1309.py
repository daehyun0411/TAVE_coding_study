# 백준 1309
from time import time

column = int(input())
start_time = time()
cage = [0]*column

cage[0] = 3
cage[1] = 7

for i in range(2,column):
    cage[i] = 2*cage[i-1] + cage[i-2]

print(cage[column-1]%9901)
end_time = time()

range = end_time-start_time
print(range)
