from collections import deque


n, k = int(input()), int(input())
graph = [[0] * (n + 1) for _ in range(n + 1)] #맵정보

#동서남북
dy = [0,1,0,-1]
dx = [1,0,-1,0]

info = [] #방향회전정보

for _ in range(k): #사과가 있는 곳 1 표시
    a, b = map(int, input().split())
    graph[a][b] = 1

l = int(input())
for _ in range(l):
    x, c = input().split()
    x = int(x)
    info.append((x, c))

def turn(direction, c):
    if c == 'L':
        direction = (direction + 3) % 4
    else:
        direction = (direction + 1) % 4
    return direction

def simulate():
    x, y = 1, 1 #뱀 머리 위치
    graph[x][y] = 2 #뱀이 존재하는 위치는 2
    direction = 0
    time, index = 0, 0 #시작한 뒤에 지난 초시간, 다음에 회전할 정보
    q = deque([(x, y)]) #뱀이 차지하고 있는 위치
    
    while True:
        nx = x + dx[direction]
        ny = y +dy[direction]

        if 1<= nx <= n and 1 <= ny <= n and graph[nx][ny] != 2: #맵 몸통 안에 있고, 뱀의 몸통 안에 없다면 
            if graph[nx][ny] == 0:
                graph[nx][ny] = 2
                q.append((nx, ny))
                px, py = q.popleft()
                graph[px][py] = 0
            elif graph[nx][ny] == 1:
                graph[nx][ny] = 2
                q.append((nx, ny))

        else:
            time += 1
            break
        x, y = nx, ny
        time += 1

        if index < 1 and time == info[index][0]:
            direction = turn(direction, info[index][1])
            index += 1

    return time
    
print(simulate())
