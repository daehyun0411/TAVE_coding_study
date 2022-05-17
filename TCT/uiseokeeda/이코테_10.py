# 자물쇠와 열쇠 
# https://programmers.co.kr/learn/courses/30/lessons/60059

# 시계 방향 90회전 
def rotation(key):
    new_keys = []
    for i in range(len(key[0])):
        new_key = []
        for j in range(len(key[0])-1,-1,-1):
            new_key.append(key[j][i])
        new_keys.append(new_key)
    return new_keys

def check(board,n):
    for i in range(n):
        for j in range(n):
            if(board[n+i][n+j] != 1):
                return False
    return True


def move(lock,key):
    board = [[0] * (len(lock)*3) for _ in range(len(lock)*3)]
    n = len(lock)
    # 가운데만 lock으로 정렬시키겠다.
    for i in range(n):
        for j in range(n):
            board[i+n][j+n] = lock[i][j]
    # 왼쪽위부터 내려서 key와 대입해 보며 이동시키겠다. 
    for down in range(n*2):
        for right in range(n*2):
            for i in range(len(key)):
                for j in range(len(key)):
                    board[(down+i)][(right+j)] += key[i][j]
            if(check(board,len(lock))==True):
                return True
            for i in range(len(key)):
                for j in range(len(key)):
                    board[(i+down)][(j+right)] -= key[i][j]
    return False
    
def solution(key, lock):
    answer = False
    for i in range(4):
        key = rotation(key)
        if(move(lock,key)==True):
            answer = True
            break
    return answer

key = [[0,0,0],[1,0,0],[0,1,1]]
lock = [[1,1,1],[1,1,0],[1,0,1]]

print(solution(key,lock))
