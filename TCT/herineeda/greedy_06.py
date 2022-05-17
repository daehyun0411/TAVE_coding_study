def solution(food_times, k):
    answer = 0
    i = 0
    time = 0
    while time <= k:
        if sum(food_times) == 0: #더 섭취할 음식이 없으면 1 반환
            return -1
        if food_times[i] > 0:
            food_times[i] -= 1 #1씩 감소 
            answer = i + 1 # 인덱스(몇번째 음식인지) 출력
            time += 1
        i = (i + 1) % len(food_times) #인덱스 범위를 넘지 않게 리스트 크기로 한 번 나눠주기
    
    return answer
