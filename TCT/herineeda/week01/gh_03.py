
def solution(s):
    answer = len(s);
         
    for cnt in range(1, len(s)//2+2): 
        string = "";
        now = s[:cnt];
        count = 0;
        
        for i in range(0, len(s), cnt):
            if s[i:cnt+i] == now: 
                count += 1;
            else: 
                if count < 2:
                    string += now;
                    count = 1
                else:
                    string += str(count) + now;
                    count = 1
                now = s[i:cnt+i];
        
        if count < 2:
            string += now;
            count = 1
        else:
            string += str(count) + now;
            count = 1
        
        if len(string) < answer:
            answer = len(string);
            
    return answer;

print(solution("aaaabbabbabb"))
