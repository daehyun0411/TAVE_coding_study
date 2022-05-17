# 문자열 압축 
# https://programmers.co.kr/learn/courses/30/lessons/60057

def solution(s):
    # 1 부터 길이 절반까지 반복 
    length = len(s)
    for i in range(1,(len(s)//2)+1):
        index = 0   # 문자열 index
        temp = ""   # 문자열 저장
        count = 1   # 같은게 있는지 파악
        none = True # 생성가능 여부 파악
        while(index+i+i<len(s)+1):
            if(s[index:index+i]==s[index+i:index+i+i]):
                count+=1
                # 같을 경우에는 index가 i만큼 증가 
                index+=i
            else:
                if(i>1 and index==0): # 못만드는경우 break
                    none = False
                    break
                
                if(count>1):
                    temp += str(count)+ s[index:index+i]
                    index+=i
                    count=1
                else:
                    temp += s[index]
                    index+=1
        if(none==False):
            temp = s
        else:
            if(count>1):
                temp += str(count)+ s[index:index+i]
                temp += s[index+i:len(s)]
            else:
                temp+= s[index:len(s)]
        print(temp)
        if(len(temp)<length):
            length = len(temp)
    answer = length
    return answer

print(solution("xababcdcdababcdcd"))