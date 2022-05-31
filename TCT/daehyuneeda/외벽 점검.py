# week/list 의 개수가 매우 작아 완전 탐색으로 해결 가능

from itertools import permutations

def solution(n, week, dist):
    # 길이를 2배로 늘려서 원형 > 일자
    length = len(week)
    for i in range(length):
        week.append(week[i] + n)
    answer = len(dist) + 1
    
    for start in range(length):
        for friends in list(permutations(dist, len(dist))):
            count = 1
            position = week[start] + friends[count -1] # 점검할 수 있는 마지막 위치
            for index in range(start, start + length): # 시작점부터 모든 취약 지점을 확인
                # 점검할 수 있는 위치를 벗어나는 경우
                if position < week[index]:
                    count += 1 # 추가
                    if count > len(dist): # 더 투입이 불가능하다면 종료
                        break
                    position = week[index] + friends[count - 1]
            answer = min(answer, count) # 최솟값
    
    # 예외        
    if answer > len(dist):
        return -1
    
    return answer
                    