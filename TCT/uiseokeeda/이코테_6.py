# 무지의 먹방 라이브 
# https://programmers.co.kr/learn/courses/30/lessons/42891

def solution(food_times, k):    
    rest_time = k
    foods = len(food_times)

    while(rest_time>0):
        food_index = 0
        for i in range(foods):
            if(rest_time==0):
                break
            if (food_times[i]==0):
                food_index += 1
                continue
            food_times[i] -= 1
            rest_time -= 1   
            food_index += 1    

    # 더이상 먹을 것이 없을 경우
    if(sum(food_times)==0):
        return -1

    # 마지막 먹은 것의 다음것을 출력해야한다.         
    if(food_index==foods):
        food_index = 1
    else:
        food_index += 1
    answer = food_index
    return answer

test = solution([3,1,2],5)
print(test)