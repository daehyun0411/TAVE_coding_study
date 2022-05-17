#  k값이 충분하다면 음식을 다 먹을만큼 회전 가능
# 우선순위 큐(가장 우선순위가 높은 데이터를 가장 먼저 삭제)
import heapq

def solution(food_times, k):
    # 중단 전 음식을 다 먹는 경우
    if sum(food_times) <= k:
        return -1
    
    q = []
    length = len(food_times) # 음식 개수
    for i in range(length):
        heapq.heappush(q, (food_times[i], i+1))
    
    time = 0    
    while (q[0][0] - time) * length < k:
        k -= (q[0][0] - time) * length
        time += (q[0][0] - time)
        length -= 1
        heapq.heappop(q)
        
    result = sorted(q, key = lambda x: x[1])
    answer = result[k % length][1]
    return answer