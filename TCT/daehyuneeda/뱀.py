n = int(input())
k = int(input())

array = [[0] * (n+1) for _ in range(n+1)] # 맵 정보

# 사과 입력
for _ in range(k):
    r,c = map(int, input().split())
    array[r][c] == 1
 
# 방향 회전 정보 입력  
info = []  
l = int(input())
for _ in range(l):
    x, c = input.split()
    info.append(int(x), c)

# 처음 오른쪽(동, 남, 서, 북)    
dx = [0,1,0,-1]
dy = [1,0,-1,0]    

def turn(direction, c):
    if c == "L":
        direction = (direction - 1) % 4
    else:
        direction = (direction + 1) % 4
    return direction

def simulation():
    x,y = 1, 1 # 뱀의 머리
    array[x][y] = 2 # 뱀의 존재 위치 2로 표시
    direction = 0
    time = 0
    index = 0
    q= [(x,y)] # 뱀이 차지하고 있는 위치 정보
    while True:
        nx = x + dx[direction]
        ny = y + dy[direction]
        # 맵 안에 존재, 뱀의 몸통이 없는 위치 
        if 1 <= nx and nx <= n and 1 <= ny and ny <= n and array[nx][ny] != 2:
            # 사과가 없다면 이동 후 꼬리 제거
            if array[nx][ny] == 0:
                array[nx][ny] = 2
                q.append((nx,ny))
                px, py = q.pop(0)
                array[px][py] = 0
            # 사과가 있다면 꼬리 그대로 두기
            if array[nx][ny] == 1:
                array[nx][ny] = 2
                q.append((nx, ny))
        else:
            time += 1
            break
        x,y = nx, ny
        time += 1
        if index < 1 and time == info[index][0]:
            direction = turn(direction, info[index][1])
            index += 1
    return time

print(simulation())
