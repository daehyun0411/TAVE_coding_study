#https://programmers.co.kr/learn/courses/30/lessons/60061

Pillar = [[]]
Bar = [[]]

def checkPillar(x,y):
    if y == 0 or Pillar[x][y-1]: #바닥일 경우 or 아래에 기둥이 있는 경우
        return True
    if (x > 0 and Bar[x-1][y]) or Bar[x][y]: #기둥 아래에 보가 있을 경우
        return True
    return False

def checkBar(x,y):
    if Pillar[x][y-1] or Pillar[x+1][y-1]: #바로 아래 기둥있으면 설치 가능
        return True
    if x > 0 and Bar[x-1][y] and Bar[x+1][y]:
        return True
    return False

def canDelete(x,y): #삭제를 할 때 삭제하는 기둥 주변의 6개 좌표가 영향을 받으므로
    for i in range(x-1,x+2): # 주변 6개의 좌표를 for문으로 확인
        for j in range(y,y+2): 
            if Pillar[i][j] and checkPillar(i, j) == False:#기둥이 있다면 기둥이 존재할 수 있는지 확인
                return False
            if Bar[i][j] and checkBar(i, j) == False:
                return False
    return True
            
def solution(n, build_frame):
    global Pillar, Bar
    Pillar = [[0 for _ in range(n+2)] for _ in range(n+2)]
    Bar = [[0 for _ in range(n+2)] for _ in range(n+2)]
    
    for x, y, kind, cmd in build_frame:
        if kind == 0:
            if cmd == 1:
                if checkPillar(x,y):
                    Pillar[x][y] = 1
            else:
                Pillar[x][y] = 0 #건축물이 있으면 삭제하고
                if not canDelete(x,y): #삭제할 조건이 안되면 
                    Pillar[x][y] = 1 #다시 복원
        else:
            if cmd == 1:
                if checkBar(x,y):
                    Bar[x][y] = 1
            else:
                Bar[x][y] = 0
                if not canDelete(x,y):
                    Bar[x][y] = 1

    answer = []
    for x in range(n+1):
        for y in range(n+1):
            if Pillar[x][y]:
                answer.append([x,y,0])
            if Bar[x][y]:
                answer.append([x,y,1])
                
                
    
    return answer
