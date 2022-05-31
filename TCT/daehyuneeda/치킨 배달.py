# 13Cm
from itertools import combinations

n,m = map(int, input().split())
chicken, house = [],[]

# 정보 입력
for r in range(n):
    data = list(map(int, input().split()))
    for c in range(n):
        if data[c] == 1:
            house.append((r,c))
        elif data[c] == 2:
            chicken.append((r,c))

# 치킨 집을 뽑는 경우의 수            
candidates = list(combinations(chicken,m))

# 집으로부터 치킨집까지의 거리의 합
def get_sum(candidate):
    result = 0
    for hx, hy in house:
        temp = 1e9
        for cx, cy in candidate:
            temp = min(temp, abs(hx-cx) + abs(hy-cy))
        result += temp
    return result

# 거리의 합이 최소인 경우를 출력
result = 1e9
for candidate in candidates:
    result = min(result, get_sum(candidate))
    
print(result)