# 단위를 하나씩 늘려가며 압축
def solution(s): 
    answer=[] 
    if len(s)==1: 
        return 1 
    for step in range(1, (len(s)//2)+1): 
        result = '' 
        cnt = 1 
        tmp=s[:step] 
        for j in range(step, len(s), step): 
            if tmp==s[j:step+j]: 
                cnt+=1 
            else: 
                if cnt!=1: 
                    result = result + str(cnt)+tmp 
                else: 
                    result = result + tmp 
                # 초기화 
                tmp=s[j:j+step] 
                cnt = 1 
        if cnt!=1:  
            result = result + str(cnt) + tmp 
        else: 
            result = result + tmp 
            
        answer.append(len(result)) 
    
    return min(answer)
